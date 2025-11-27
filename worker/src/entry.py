# worker/src/entry.py

from workers import Response, WorkerEntrypoint
from pyodide.code import run_code
import json
import traceback
import sys
from urllib.parse import urlparse, parse_qs

# --- DYNAMIC CODE MAPPING (The Programs to Run) ---
# NOTE: In a production version, you would load these file contents dynamically.
# For simplicity, we hardcode the paths to the code strings here.
DYNAMIC_CODE_MAPPING = {
    "day1/hello_world.py": "print('Day 1 Program Ran Successfully!')\nprint('Total: ' + str(2 + 2))",
    "day2/example.py": "x = 10\nif x > 5:\n    print('The logic is correct.')\nelse:\n    raise Exception('Test Failure')\nprint('Done.')"
}

# Custom stream class to capture output from the Python execution
class OutputCapturer:
    def __init__(self):
        self.buffer = ""
    def write(self, s):
        self.buffer += s
    def flush(self):
        pass

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        # 1. Parse Request to get the program path
        parsed_url = urlparse(request.url)
        query_params = parse_qs(parsed_url.query)
        program_path = query_params.get("path", [None])[0]

        if not program_path:
            return Response.json({"error": "Missing 'path' query parameter."}, status=400)
        
        python_code = DYNAMIC_CODE_MAPPING.get(program_path)
        if not python_code:
            return Response.json({"error": f"Program not found: {program_path}"}, status=404)

        # Execution Setup
        capturer = OutputCapturer()
        sys.stdout = capturer
        status = "Success"
        
        try:
            # 2. RUN THE PYTHON CODE using Pyodide's run_code
            run_code(python_code)
            output = capturer.buffer
        except Exception:
            status = "Error"
            output = traceback.format_exc() # Capture the full error
        finally:
            sys.stdout = sys.__stdout__ # Restore standard output

        try:
            # 3. Log the result to D1 (using the LOG_DB binding from wrangler.toml)
            await self.env.LOG_DB.prepare(
                "INSERT INTO execution_logs (program_path, run_timestamp, status, output) VALUES (?, datetime('now'), ?, ?)"
            ).bind(
                program_path,
                status,
                output
            ).run()
        except Exception as d1_error:
            # Log D1 error but still return execution output
            output += f"\n\n--- D1 LOGGING ERROR ---\nCould not log to database: {str(d1_error)}"

        # 4. Return the result to the frontend
        return Response.json({
            "status": status,
            "program": program_path,
            "output": output.strip()
        })
