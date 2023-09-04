# 1267 핸드폰 요금


def call_fee(call_time, fee_per_unit_timespan, unit_timespan):
    timespan_count = call_time // unit_timespan + 1
    return timespan_count * fee_per_unit_timespan


_ = int(input())
call_time_list = list(map(int, input().split()))
yongsik_fee = sum([call_fee(i, 10, 30) for i in call_time_list])
minsik_fee = sum([call_fee(i, 15, 60) for i in call_time_list])
if yongsik_fee > minsik_fee:
    print(f"M {minsik_fee}")
elif yongsik_fee == minsik_fee:
    print(f"Y M {minsik_fee}")
else:
    print(f"Y {yongsik_fee}")
