n, s, e = map(int, input().split())
deal = 0
for _ in range(n):
    r, a, d = map(int, input().split())
    deal_times_end, remainder_end = divmod(e, r+a)
    deal_times_start, remainder_start = divmod(s, r+a)
    remain_deal_end = max(0, remainder_end-r)
    remain_deal_start = max(0, remainder_start-r)
    deal += (deal_times_end-deal_times_start)*d + (remain_deal_end-remain_deal_start)/a*d
print(deal/(e-s))