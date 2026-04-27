# 28463 Toe Jumps


def rotate_90_degrees_clockwise(trace: list[list[str]]) -> list[list[str]]:
    result = [["", ""] for _ in range(2)]
    result[0][0], result[0][1], result[1][0], result[1][1] = (
        trace[0][1],
        trace[1][1],
        trace[0][0],
        trace[1][0],
    )
    return result


def make_foot_configuration_dict() -> dict[tuple[str, str], list[list[str]]]:
    foot_configuration: dict[tuple[str, str], list[list[str]]] = {
        ("T", "S"): [[".", "O"], ["P", "."]],
        ("F", "S"): [["I", "."], [".", "P"]],
        ("Lz", "S"): [["O", "."], [".", "P"]],
    }
    direction = "SENW"
    for i in range(3):
        foot_configuration[("T", direction[i + 1])] = rotate_90_degrees_clockwise(
            foot_configuration[("T", direction[i])]
        )
        foot_configuration[("F", direction[i + 1])] = rotate_90_degrees_clockwise(
            foot_configuration[("F", direction[i])]
        )
        foot_configuration[("Lz", direction[i + 1])] = rotate_90_degrees_clockwise(
            foot_configuration[("Lz", direction[i])]
        )
    return foot_configuration


foot_configuration = make_foot_configuration_dict()
direction_target = input().strip()
trace_target = [list(input().strip()) for _ in range(2)]
result = "?"
for (jump_type, direction), trace in foot_configuration.items():
    if direction != direction_target:
        continue
    if trace == trace_target:
        result = jump_type
print(result)