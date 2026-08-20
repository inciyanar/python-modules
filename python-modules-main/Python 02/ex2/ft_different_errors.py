def garden_operations(operation_number: int) -> None:
	if operation_number == 0:
		return ValueError
	if operation_number == 1:
		return ZeroDivisionError
	if operation_number == 2:
		return FileNotFoundError
	if operation_number == 3:
		return TypeError
	else:
		return

def test_error_types() -> None:
	print()
	print("Welcome to incy's Garden!")
	print()
	print("There are some problems...")
	print("We're here to solve 'em:")
	print()

	print("For 5 / 0 :")
	try:
		test: int = 5
		test / 0
	except garden_operations(1):
		print("Dude... there is an ZeroDivision Error.")

	print()
	print("For int(ft):")
	try:
		int("ft")
	except garden_operations(0):
		print("Dude... there is an Value Error.")
	print()
	print("For open():")
	try:
		open("file.txt", "r")
	except garden_operations(2):
				print("Dude... there is an FileNotFound Error.")
	print()
	print("For 5 + five:")

	try:
		num: int = 5
		num + "five"
	except garden_operations (3):
		print("Dude... there is an Type Error.")
	print()

	try:
		num: int = 5
		num + "five"
		int("ft")
	except TypeError:
		print("This is TypeError")
	except ValueError:
		print("Well, this is ValueError")

	print()
	print("FYI , all errors handled beautifully...")
	print("Thanks for the help, we will miss you!!")
	print()

if __name__ == "__main__":
	test_error_types()


