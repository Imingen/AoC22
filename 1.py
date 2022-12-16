
print(f"Solving AoC day 1 part 1")

max_val = 0

with open("1.txt") as f:
    lines = f.read().splitlines()
    current_elf = 0
    for line in lines:
        if line.strip() == "":
            if(current_elf > max_val):
                max_val = current_elf
            current_elf = 0
        else:
            current_elf += int(line)
print(f"Answer to part 1:")            
print(f"Maximum value is {max_val}")

print(f"Solving part 2 ")

first = 0
second = 0
third = 0

with open("1.txt") as f:
    lines = f.read().splitlines()
    current_elf = 0
    for line in lines:
        if line.strip() == "":
            if(current_elf > first):
                third = second
                second = first
                first = current_elf
            elif(current_elf > second):
                third = second
                second = current_elf
            elif(current_elf > third):
                third = current_elf
            current_elf = 0
        else:
            current_elf += int(line)

total = (first + second + third)
print(f"Answer to part 2:")            
print(f"total is {total}")





