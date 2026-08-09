def input_temperature(temp_str: str) -> int:
	temper = int(temp_str, 10)
	return temper

def test_temperature() -> None:
	print()
	print("Welcome to incy's Garden!")
	print()
	print("It's gettin' hot in here...")
	print("Let's check out the temperature:")
	print()

	to_test: list[str] = ["42", "incisozluk", "?", "-5"]
	for test in to_test:
		print(f"-For {test} input value:")
		try:
			print(input_temperature(test))
			print(f"Everything is fine! The temperature is {test} degree.")
		except Exception as a:
			print("Opps! Calm down.")
			print("There is an error: ", end = "")
			print(a)
		print()

	print("Goodbye! We will miss you...")

if __name__ == "__main__":
	test_temperature()
