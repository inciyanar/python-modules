def ft_plot_area() -> None:
    len: str = input("Enter length: ")
    wid: str = input("Enter width: ")
    length: int = int(len, 10)
    width: int = int(wid, 10)
    print(f"Plot area: {length * width}")
