
total_full = 0
total_part = 0

with open(r"datasets\4.txt") as f:
    lines = f.read().splitlines()

    for line in lines:
        x, y = line.split(",")
        x = x.split("-")
        y = y.split("-")

        x = list(map(int, x))
        y = list(map(int, y))

        x_range = [x for x in range(x[0], x[1]+1)]
        y_range = [y for y in range(y[0], y[1]+1)]

        if set(x_range).intersection(set(y_range)):
            total_part += 1



        if max(x) <= max(y) and min(x) >= min(y):
            total_full += 1
        elif max(y) <= max(x) and min(y) >= min(x):
            total_full +=1


print(total_full)
print(total_part)








