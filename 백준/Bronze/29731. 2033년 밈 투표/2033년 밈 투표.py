meme_set = {"Never gonna give you up",
"Never gonna let you down",
"Never gonna run around and desert you",
"Never gonna make you cry",
"Never gonna say goodbye",
"Never gonna tell a lie and hurt you",
"Never gonna stop"}

n = int(input())
changed_meme_list = [input() for _ in range(n)]
if all(i in meme_set for i in changed_meme_list):
    print("No")
else:
    print("Yes")