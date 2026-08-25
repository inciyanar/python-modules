class GardenError (Exception):
	def __str__(self):
		return ("Fix the garden issue please...")

class PlantError (GardenError):
	def __init__(self, plant: str):
		self.plant = plant
	def __str__(self):
		return(f"Do you think {self.plant} is a plant?!?")

class WaterError (GardenError):
	def __init__(self, ml: int):
		self.ml = ml

	def __str__(self):
		if self.ml > 1000:
			return("Thhaaaat is a lot of water.")
		if self.ml < 0:
			return("Girl..")


def water_checker(ml: int) -> None:
	if ml < 0:
		raise WaterError(ml)
	if ml > 1000:
		raise WaterError(ml)
	else:
		print("This amount of water is fine!")

def plant_checker(test: str) -> None:
	if test == "lily" or test == "rose" or test == "sunflower" or test == "orchid" or test == "tulip" or test ==  "daisy":
		print(f"Can you guess how many {test} do we have?")
	else:
		raise PlantError(test)

def garden_checker(key: bool) -> None:
	if key == True:
		print("Everything is fine.")
	if key == False:
		raise GardenError

def error_handler():
	print()
	print("---Welcome to incy's Garden!----")
	print()
	print("There are some problems...")
	print("We're here to solve 'em:")
	print()

	print("----Let's check the water milliliter:")
	to_test: list[int] = [-5, 45, 5000]
	for test in to_test:
		print()
		print(f"For {test}:")
		try:
			water_checker(test)
		except WaterError as response:
			print(response)

	print()
	print("----What about the plants:")
	to_test: list[str] = ["chair", "rose", "lily", "pearl"]
	for test in to_test:
		print()
		print(f"For {test}:")
		try:
			plant_checker(test)
		except PlantError as response:
			print(response)

	print()
	print("----Let's check the garden")
	try:
		garden_checker(True)
		garden_checker(False)
	except GardenError as response:
		print(response)

	print()
	print("----Let's prove the inheritince")
	try:
		water_checker(1000000)
	except GardenError as response:
		print(response)

	print()
	print("Take care...")

if __name__ == "__main__":
	error_handler()


