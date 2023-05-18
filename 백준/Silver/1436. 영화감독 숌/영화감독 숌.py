# 1436 영화감독 숌

movie_title_number = [666]

for i in range(4):
    movie_title_sub = []
    for j in range(0, 10):
        for k in movie_title_number:
            movie_title_sub.append(str(j) + str(k))
            movie_title_sub.append(str(k) + str(j))
    movie_title_number += movie_title_sub
movie_title_number = list(set(map(int, movie_title_number)))
movie_title_number.sort()
print(movie_title_number[int(input()) - 1])