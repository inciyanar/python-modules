import math


def get_player_pos() -> tuple[float, float, float]:
    answer = input("New coordinates please in (x, y, z) format:")
    try:
        splited: list[str] = answer.split(",")
        print(f"{splited[0]}")
        i = 0
        for _ in splited:
            i += 1
        if (len(splited)) != 3:
            print("Invalid syntax, try another coordinates.")
            get_player_pos()
        return (float(splited[0]), float(splited[1]), float(splited[2]))

    except ValueError:
        try:
            for test in splited:
                float(test)
        except ValueError as a:
            print(f"Error on parameter '{test}': {a} ")
            get_player_pos()
    return()


def dis_finder(node1: tuple[float, float, float], node2: tuple[float, float, float]) -> float:
    result = math.sqrt((node2[0]-node1[0])**2 + (node2[1]-node1[1])**2 + (node2[2]-node1[2])**2)
    return result


if __name__ == "__main__":
    coordinates = get_player_pos()
    print(f"Got a first tuple {coordinates}")
    print(f"It includes: X={coordinates[0]},"
          f"Y={coordinates[1]}, Z={coordinates[2]}")
    print(f"Distance to center: {dis_finder(coordinates, (0,0,0))}")
    print("Get a second set of coordinates")
    coordinates2 = get_player_pos()
    print(f"Distance between{coordinates2}")

    #   math.sqrt(22)
