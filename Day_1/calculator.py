x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
o = input("Enter operator[eg. +-/*]: ")
operations = {
	"+":x+y,
	"-":x-y,
	"/":x/y,
	"*":x*y
}
print("result:",operations.get(o, "Invalid"))
