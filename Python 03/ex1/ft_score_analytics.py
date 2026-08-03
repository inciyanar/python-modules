import sys

class NumberError (Exception):
	def __init__(self, string: str):
		self.string = string
	def __str__(self):
		return print(f"{self.string} is not a number. Provide a number.")

class ArgumentError (Exception):
	def __str__(self):
		return ("No argument provided")

if __name__ == "__main__":
	print()
	print("Create your own sudoku!")
	print()

	try:
		if len(sys.argv) <= 1:
			raise ArgumentError()
	except ArgumentError as response:
		print(response)
	for number in sys.argv[1:]:
		try:
			int(number)
		except ValueError:
			print(f"{number} is not a number. Provide a number.")


	print("Your numbers:", end = " ")
	print(*sys.argv[1:])
	print(f"Min value of the numbers is: {min(sys.argv[1:])}")
	print(f"Max value of the numbers is: {max(sys.argv[1:])}")
	print(f"Total of the numbers is: {sum(sys.argv[1:])}")

