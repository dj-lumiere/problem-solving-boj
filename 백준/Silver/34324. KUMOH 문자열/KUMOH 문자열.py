n = int(input())
start = [(i, 0) for i in range(n)]
strings = [input() for _ in range(n)]
start.pop()
start.extend([(n-1, i) for i in range(1000)])
words = []
for y, x in start:
	word = ""
	ny, nx = y, x
	while True:
		word += strings[ny][nx] if 0 <= nx < len(strings[ny]) else ""
		ny, nx = ny-1, nx+1
		if 0<=ny<n and 0<=nx<1000:
			continue
		break
	words.append(word)
	words.append(word[::-1])
answer = 0
for word1, word2 in zip(words[::2], words[1::2]):
	if len(word1)<5:
		continue
	answer1 = 0
	answer2 = 0
	for i in range(len(word1)-4):
		if word1[i:i+5] == "KUMOH":
			answer1 += 1
	for i in range(len(word2)-4):
		if word2[i:i+5] == "KUMOH":
			answer2 += 1
	answer += max(answer1, answer2)
print(answer)