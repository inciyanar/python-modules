import math


def get_player_pos() -> tuple:
    answer = input("New coordinates please in (x, y, z) format:")
    try:
        send: tuple[float, float, float] = float(answer)
    except ValueError as response:
        print(response)
        return ()
    return ()


if __name__ == "__main__":
      math.sqrt(22)
