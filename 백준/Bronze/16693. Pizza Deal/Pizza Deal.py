# 16693 Pizza Deal

from math import pi

A, P1 = list(map(int, input().split()))
R, P2 = list(map(int, input().split()))
pizza_slice_cost_ratio = P1 / A
whole_pizza_cost_ratio = P2 / (pi * R**2)
if pizza_slice_cost_ratio < whole_pizza_cost_ratio:
    print("Slice of pizza")
else:
    print("Whole pizza")