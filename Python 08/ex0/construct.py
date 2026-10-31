import sys
import os
import site


def venv_checker() -> bool:
    if sys.base_prefix == sys.prefix:
        return False
    return True


def main() -> None:
    if venv_checker():
        nameof_env = os.path.basename(sys.prefix)
        pathof_env = sys.prefix
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print("Current Python:", sys.executable)
        print("Virtual Environment:", nameof_env)
        print("Environment Path:", pathof_env)
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print(site.getsitepackages()[0])
    else:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate  # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
