
line = None

with open(r"datasets\6.txt") as f:
    line = ''.join(f.read().splitlines())

for i, letter in enumerate(line):
    word = set(line[i:i+4])
    if len(word) == 4:
        print(f"GOAL! {word} at {i+4}")
        break

for i, l in enumerate(line):
    word = set(line[i:i+14])
    if len(word) == 14:
        print(f"GOAL! {word} at {i+14}")
        break






