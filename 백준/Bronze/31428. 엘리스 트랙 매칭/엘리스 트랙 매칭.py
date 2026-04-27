_ = int(input())
friend_tracks = list(input().split())
hellobit_track = input()
print(sum(i == hellobit_track for i in friend_tracks))