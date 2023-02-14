# 1253 좋다

N = int(input())
A = list(map(int, input().split(" ")))
A.sort()

good_number = 0

for i, j in enumerate(A):
    target_number = j
    ptr_a = 0
    ptr_b = N - 1
    while ptr_a < ptr_b:
        if A[ptr_a]+A[ptr_b] > target_number:
            ptr_b -= 1
        elif A[ptr_a]+A[ptr_b] < target_number:
            ptr_a += 1
        else:
            if ptr_a == i:
                ptr_a += 1
                if A[ptr_a-1] == A[ptr_a] and ptr_a < ptr_b:
                    good_number += 1
                    break
            elif ptr_b == i:
                ptr_b -= 1
                if A[ptr_b+1] == A[ptr_b] and ptr_a < ptr_b:
                    good_number += 1
                    break
            else:
                good_number += 1
                break
print(good_number)