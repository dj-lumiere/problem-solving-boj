# 2108 통계학

from statistics import mean, median, multimode
from sys import stdin

N = int(stdin.readline().strip())
number_list = [int(stdin.readline().strip()) for _ in range(N)]
mean_value = round(mean(number_list))
median_value = median(number_list)
multimode_list = multimode(number_list)
multimode_list.sort()
multimode_value = multimode_list[0]
if len(multimode_list) > 1:
    multimode_value = multimode_list[1]
peak_to_peak = max(number_list) - min(number_list)
print(mean_value, median_value, multimode_value, peak_to_peak, sep="\n")
