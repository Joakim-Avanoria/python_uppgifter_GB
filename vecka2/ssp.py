import random

beats = {"sten": "sax", "sax": "påse", "påse": "sten"}

def winner(p1, p2):
    if p1 == p2: return "oavgjort"
    if beats[p1] == p2: return "p1"
    else: return "p2"

N = 100
random.seed(42)
stat = {"p1": 0, "p2": 0, "oavgjort": 0}
for _ in range(N):
    p1 = random.choice(list(beats.keys()))
    p2 = random.choice(list(beats.keys()))
    w = winner(p1, p2)
    stat[w] += 1
print(stat)











# score = {"spelare": 0, "dator": 0, "oavgjort": 0}
# while True:
#     val = input("sten/sax/påse eller 0 för att avsluta: ")
#     if val == "0": break
#     if val not in beats:
#         print("Ogiltigt val")
#         continue

#     dator = random.choice(list(beats.keys()))
#     w = winner(val, dator)
#     if w == "p1": score["spelare"] += 1
#     elif w == "p2": score["dator"] += 1
#     else: score["oavgjort"] += 1
#     print(f"Datorn valde {dator}")
#     print(score)