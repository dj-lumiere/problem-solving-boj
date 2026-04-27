# 29699 Welcome to SMUPC!

pattern = "WelcomeToSMUPC"
N = int(input())
print(pattern[(N - 1) % len(pattern)])
