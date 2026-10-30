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


if __name__ == "__main__":
    packages_to_check = ["pandas", "numpy", "matplotlib",]
    if not overall_checker(packages_to_check):
        print("To install with pip: pip install -r requirements.txt")
        print("To install with poetry: poetry install")
        sys.exit(1)

