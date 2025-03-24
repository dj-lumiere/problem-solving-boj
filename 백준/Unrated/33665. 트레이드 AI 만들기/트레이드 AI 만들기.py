def calculate_trade_score(
    properties, mortgage, cash, property_weight, mortgage_penalty, cash_percentage
):
    property_score = 0
    for i in range(10):
        property_count_in_same_color = 0
        for j in range(4):
            if properties[4 * i + j]:
                property_count_in_same_color += 1
        property_score += property_weight[i][property_count_in_same_color]
    property_score += cash * cash_percentage // 100
    mortgage_penalty_count = sum(mortgage)
    property_score -= mortgage_penalty_count * mortgage_penalty
    return property_score


def trade( 
    my_wanted,
    opponent_wanted,
    my_property,
    opponent_property,
    my_mortgage,
    opponent_mortgage,
    my_cash,
    opponent_cash,
    my_trade_cash,
    opponent_trade_cash,
 ):
    for i in range(39, -1, -1):
        if my_wanted[i]:
            my_property[i] ^= True
            opponent_property[i] ^= True
            if opponent_mortgage[i]:
                opponent_mortgage[i] ^= True
                my_mortgage[i] ^= True
            my_wanted[i] ^= True
        if opponent_wanted[i]:
            my_property[i] ^= True
            opponent_property[i] ^= True
            if my_mortgage[i]:
                my_mortgage[i] ^= True
                opponent_mortgage[i] ^= True
            opponent_wanted[i] ^= True
    my_cash -= my_trade_cash
    my_cash += opponent_trade_cash
    opponent_cash -= opponent_trade_cash
    opponent_cash += my_trade_cash
    return (
        my_property,
        opponent_property,
        my_mortgage,
        opponent_mortgage,
        my_cash,
        opponent_cash,
    )


property_weight = [[0] + list(map(int, input().split(" "))) for _ in range(10)]
_property = input()
request = input()
mortgage = input()
my_property = [i == "1" for i in _property]
opponent_property = [i == "2" for i in _property]
my_request = [i == "1" for i in request]
opponent_request = [i == "2" for i in request]
my_mortgage = [i and j == "1" for i, j in zip(my_property, mortgage)]
opponent_mortgage = [i and j == "1" for i, j in zip(opponent_property, mortgage)]
my_cash = int(input())
opponent_cash = int(input())
my_trade_cash = int(input())
opponent_trade_cash = int(input())
cash_percentage = int(input())
mortgage_penalty = int(input())
 
my_property_score_before_trade = calculate_trade_score(
    my_property,
    my_mortgage,
    my_cash,
    property_weight,
    mortgage_penalty,
    cash_percentage,
)
opponent_property_score_before_trade = calculate_trade_score(
    opponent_property,
    opponent_mortgage,
    opponent_cash,
    property_weight,
    mortgage_penalty,
    cash_percentage,
)
 
(
    my_property,
    opponent_property,
    my_mortgage,
    opponent_mortgage,
    my_cash,
    opponent_cash,
) = trade(
    my_request,
    opponent_request,
    my_property,
    opponent_property,
    my_mortgage,
    opponent_mortgage,
    my_cash,
    opponent_cash,
    my_trade_cash,
    opponent_trade_cash,
)
 
my_property_score_after_trade = calculate_trade_score(
    my_property,
    my_mortgage,
    my_cash,
    property_weight,
    mortgage_penalty,
    cash_percentage,
)
opponent_property_score_after_trade = calculate_trade_score(
    opponent_property,
    opponent_mortgage,
    opponent_cash,
    property_weight,
    mortgage_penalty,
    cash_percentage,
)
 
if (my_property_score_after_trade - opponent_property_score_after_trade) >= (
        my_property_score_before_trade - opponent_property_score_before_trade
):
    print("YES")
else:
    print("NO")
