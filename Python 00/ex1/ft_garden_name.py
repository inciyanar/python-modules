import ft_hello_garden


def ft_garden_name() -> None:
    gardenname: str = input("Enter garden name:")
    print(f"Garden:{gardenname}")
    print("Status: Growing well!")


if __name__ == "__main__":
    ft_hello_garden.ft_hello_garden()
