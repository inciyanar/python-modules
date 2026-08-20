class PlantError (Exception):
	def __init__(self, plant: str):
		self.plant = plant
	def __str__(self):
		return(f"There is a PlantError! Change the input {self.plant}.")


def water_plant(plant_name: str) -> None:
	if plant_name == plant_name.capitalize():
		print("Success")
	else:
		raise PlantError(plant_name)


def test_watering_system(to_test: list[str]) -> None:
	print("----Opening watering system...")
	try:
		for test in to_test:
			print(f"Testing {test}")
			water_plant(test)
			print()
	except PlantError as response:
		print(response)
		return
	finally:
		print()
		print("----Closing the watering system...")
		print("Even there is an error, always clean up son.")
	print("no output error")


if __name__ == "__main__":
	print()
	print("---Welcome to incy's Garden!----")
	print()

	to_test: list[str]= ["Tomato", "Cucumber", "sUNFLOWER"]
	test_watering_system(to_test)


