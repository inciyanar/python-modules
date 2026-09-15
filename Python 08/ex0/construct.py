import sys
import os
import site



def venv_checker() -> bool:
    if sys.base_prefix == sys.prefix:
        return False
    return True


def main() -> None:
    if venv_checker():
        print("Congrats! There is an virtual enviroment.")
        nameof_env = os.path.basename(sys.prefix)
        print("Name of this enviroment is:", end=" ")
        print(nameof_env)
        pathof_env = sys.prefix
        print("Path of this enviroment is:", end=" ")
        print(pathof_env)
        print("Package installation path:", site.getsitepackages()[0])
    else:
        print("There is NO virtual enviroment..")
        print("Current Python:", sys.executable)
        print("Try getting in one: python -m venv {name_of_the_environmet}")
        print("source {name_of_the_environmet}/bin/activate")
    print(site.getsitepackages())
    print(site.getsitepackages()[0])
    print(site.getsitepackages()[1])



if __name__ == "__main__":
    main()
