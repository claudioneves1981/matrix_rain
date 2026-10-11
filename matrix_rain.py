import time, random as r

print("\033[32m]")
d = [0] * 40
while True:
    d[r.randrange(40)]= 9
    row = "".join(r.choice(
        "ABCDEFGHIJKLMNOPQRSTUVXYWZ" if c else " ")
        for c in d)
    print("\033[H\033[L" + row)
    d = [c and c-1 for c in d]
    time.sleep(0.04)