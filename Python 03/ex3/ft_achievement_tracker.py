import random


def gen_player_achievements() -> tuple[set[str], list[str]]:
    achievement_list: list[str] = ["negotiator", "fighter", "actor", "singer"]
    num = random.randint(1, len(achievement_list))
    selected = random.sample(achievement_list, num)
    return (set(selected), achievement_list)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    player_list: list[str] = ["john", "mark", "bob", "harvey"]
    player_stock: dict[str, set[str]] = {}

    for player in player_list:
        player_stock[player], all_achs = gen_player_achievements()
        print(f"Player {player}: {player_stock[player]}")
    print()
    achievements_list: set[str] = set()
    for player in player_list:
        achievements_list = achievements_list.union(player_stock[player])
    print(f"All distinct achievements: {achievements_list}")
    print()

    common_achs: set[str] = set(all_achs)
    for player in player_list:
        common_achs = common_achs.intersection(player_stock[player])
    print(f"Common achievements: {common_achs}")
    print()

    for player in player_list:
        others: set[str] = set()
        for next_player in player_list:
            if next_player != player:
                others = others.union(player_stock[next_player])
        just_this_player = player_stock[player].difference(others)
        print(f"Only {player} has: {just_this_player}")
    print()

    for player in player_list:
        missing = set(all_achs).difference(player_stock[player])
        print(f"{player} is missing: {missing}")
