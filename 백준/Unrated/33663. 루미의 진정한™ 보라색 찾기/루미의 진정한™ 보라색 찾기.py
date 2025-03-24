def rgb_to_hsv(r, g, b):
    v = max(r, g, b)
    color_min = min(r, g, b)
    s = (v - color_min) * 255 / v
    h = 0
    if v == r:
        h = 60 * (g - b) / (v - color_min)
    elif v == g:
        h = 120 + 60 * (b - r) / (v - color_min)
    else:
        h = 240 + 60 * (r - g) / (v - color_min)
    if h < 0:
        h += 360
    return h, s, v
 

# Read input
h_low, h_high = map(int, input().split())
s_low, s_high = map(int, input().split())
v_low, v_high = map(int, input().split())
r, g, b = map(int, input().split())
 
h, s, v = rgb_to_hsv(r, g, b)
 
if h_low <= h <= h_high and s_low <= s <= s_high and v_low <= v <= v_high:
    print("Lumi will like it.")
else:
    print("Lumi will not like it.")
