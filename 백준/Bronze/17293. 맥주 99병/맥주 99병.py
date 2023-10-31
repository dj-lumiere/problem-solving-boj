# 17293 맥주 99병


def bottle_count_in_english(n: int):
    if n == 0:
        return "no more bottles"
    if n == 1:
        return f"{n} bottle"
    return f"{n} bottles"


def format_in_front_of_sentence(target: str):
    if "a" <= target[0] <= "z":
        return target[0].upper() + target[1:]
    return target


def beer_sentence(initial_value: int):
    result: str = ""
    for current_value in range(initial_value, -1, -1):
        current_count = bottle_count_in_english(current_value)
        next_count = bottle_count_in_english(
            initial_value if current_value == 0 else current_value - 1
        )
        if current_value == 0:
            return (
                result
                + format_in_front_of_sentence(
                    f"{current_count} of beer on the wall, {current_count} of beer."
                )
                + "\n"
                + format_in_front_of_sentence(
                    f"Go to the store and buy some more, {next_count} of beer on the wall."
                )
            )
        result += (
            format_in_front_of_sentence(
                f"{current_count} of beer on the wall, {current_count} of beer."
            )
            + "\n"
            + format_in_front_of_sentence(
                f"Take one down and pass it around, {next_count} of beer on the wall."
            )
            + "\n\n"
        )


n = int(input())
print(beer_sentence(n))