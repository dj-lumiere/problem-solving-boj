n1 = int(input())
n2, n3, n4, n5 = list(map(int, input().split(" ")))

def continuity_check(k:int, a:int, b:int, c:int, d:int) -> str:
    left_limit = a*k+b
    right_limit = c*k+d
    function_value = left_limit
    if left_limit == right_limit:
        return f"Yes {function_value}"
    else:
        return "No"

print(continuity_check(n1, n2, n3, n4, n5))