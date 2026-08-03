import sys

if __name__ == "__main__":
	print()
	print("---Command Quest----")
	print()
	print("Name of the program:", sys.argv[0])
	length: int = len(sys.argv)
	for i in range (1, length):
		print(f"Argument {i}:", sys.argv[i])
	print(f"Total arguments: {length}")
