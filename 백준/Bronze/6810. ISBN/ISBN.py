# 6810 ISBN

isbn_weight = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
isbn = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]
for _ in range(3):
    isbn.append(int(input()))
print(f"The 1-3-sum is {sum(a * b for a, b in zip(isbn, isbn_weight))}")