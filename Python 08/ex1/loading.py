import importlib
import sys


def package_checker(package: str) -> bool:
    try:
        module = importlib.import_module(package)
        print(f"Everything is fine, {package} with "
              f"{module.__version__} has installed.")
        return True
    except ImportError as e:
        print(e)
        return False


def overall_checker(packages_to_check: list[str]) -> bool:
    my_bool = True
    for item in packages_to_check:
        if not package_checker(item):
            my_bool = False
    return (my_bool)


def generate_data() -> "numpy.ndarray":
    import numpy
    ran = numpy.random.default_rng()
    values = ran.normal(50, 10, 1000)
    return (values)


def data_processor(data: list[int]) -> DataFrame:
    import pandas
    data_frame = pandas.DataFrame({"signal": data})
    print(data_frame["signal"].mean())
    print(data_frame["signal"].min())
    print(data_frame["signal"].max())
    return (data_frame)


def png_visualizer(data: "DataFrame") -> None:
    import matplotlib.pyplot
    matplotlib.pyplot.plot(data["signal"])
    matplotlib.pyplot.savefig()


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")
    packages_to_check = ["pandas", "numpy", "matplotlib",]
    if not overall_checker(packages_to_check):
        print("To install with pip: pip install -r requirements.txt")
        print("To install with poetry: poetry install")
        sys.exit(1)

    print()
    print("Analyzing Matrix data...")
    print("Processing 1000 data points")
    data_points = generate_data()
    data_frame = data_processor(data_points)
    print("Generating visualization...")
    png_visualizer(data_frame)
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
