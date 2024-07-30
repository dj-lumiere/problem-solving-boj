def solution(players, callings):
    answer = players
    player_rank_list = {value: index for index, value in enumerate(players)}
    for player in callings:
        current_rank = player_rank_list[player]
        rank_swap_target = answer[current_rank - 1]
        answer[current_rank - 1], answer[current_rank] = (
            answer[current_rank],
            answer[current_rank - 1],
        )
        player_rank_list[player], player_rank_list[rank_swap_target] = (
            player_rank_list[rank_swap_target],
            player_rank_list[player],
        )
    return answer