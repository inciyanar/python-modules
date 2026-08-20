def garden_operations(operation_number: int) -> None:
	if operation_number == 0:
		int("ft")
	if operation_number == 1:
		test: int = 5
		test / 0
	if operation_number == 2:
		open("file.txt", "r")
	if operation_number == 3:
		num: int = 5
		num + "five"
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
		garden_operations(1)
	except ZeroDivisionError:
		print("Dude... there is an ZeroDivision Error.")

	print()
	print("For int(ft):")
	try:
		garden_operations(0)
	except ValueError:
		print("Dude... there is an Value Error.")
	print()
	print("For open():")
	try:
		garden_operations(2)
	except FileNotFoundError:
		print("Dude... there is an FileNotFound Error.")
	print()
	print("For 5 + five:")
	try:
		garden_operations(3)
	except TypeError:
		print("Dude... there is an Type Error.")
	print()


	try:
		garden_operations(0)
		garden_operations(3)
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


