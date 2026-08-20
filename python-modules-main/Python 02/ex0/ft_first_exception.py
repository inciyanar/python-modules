def input_temperature(temp_str: str) -> int:
	try:
		temper = int(temp_str, 10)
		print(f"Everything is fine! The temperature is {temper} degree.")
	except Exception as a:
		print("Opps! Calm down.")
		print("There is an error: ", end = "")
		print(a)

def test_temperature() -> None:
	print()
	print("Welcome to incy's Garden!")
	print()
	print("It's gettin' hot in here...")
	print("Let's check out the temperature:")
	print()

	to_test: list[str] = ["42", "incisozluk", "?", "-5"]
	for path in to_test:
		print(f"-For {path} input value:")
		input_temperature(path)
		print()

	print("Goodbye! We will miss you...")

if __name__ == "__main__":
	test_temperature()

