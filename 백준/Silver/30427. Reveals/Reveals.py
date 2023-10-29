# C번 - Reveals

_ = input()
N = int(input())
person_at_swi_home = set(["swi"] + [input() for _ in range(N)])
M = int(input())
person_seen = set([input() for _ in range(M)])
person_at_home_not_seen = person_at_swi_home.difference(person_seen)
# print(person_at_home_not_seen, person_seen, person_at_swi_home)
if "dongho" in person_at_swi_home:
    print("dongho")
elif len(person_at_home_not_seen) == 1:
    print(list(person_at_home_not_seen)[0])
elif "bumin" in person_at_home_not_seen:
    print("bumin")
elif "cake" in person_at_home_not_seen:
    print("cake")
elif "lawyer" in person_at_home_not_seen:
    print("lawyer")
else:
    person_at_home_not_seen.discard("swi")
    print(sorted(person_at_home_not_seen)[0])
