# 30793 gahui and sousenkyo 3

p_x, r_x = map(int, input().split(" "))
character_type = (
    ["weak"] * 20 + ["normal"] * 20 + ["strong"] * 20 + ["very strong"] * 100
)
print(character_type[p_x * 100 // r_x])