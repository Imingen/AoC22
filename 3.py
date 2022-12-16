import string
from itertools import zip_longest


alph = string.ascii_letters
total_score = 0

total_score_2 = 0

print(alph)
with open(r"datasets\3.txt")as f:
    lines = f.read().splitlines()

    lines_by_3 = [lines[n:n+3] for n in range(0, len(lines), 3)]

    for line in lines:
        line_length = int(len(line)/2)
        part_one = line[:line_length]
        part_two = line[line_length:]

        x = list(set(part_one).intersection(part_two))
        score = int(alph.find(x[0]))+1
        total_score += score


    for l in lines_by_3:
        y = set(l[0]) & set(l[1]) & set(l[2])
        y = list(y)
        s = int(alph.find(y[0]))+1
        total_score_2 += s



print(total_score)
print(total_score_2)

