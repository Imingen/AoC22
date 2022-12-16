from file_reader import read_file
import numpy as np
import math

def compute_scenic_score(tree_value, left, right, up, down):
    
    numbers = []
    nums_l = 0
    nums_r = 0
    nums_d = 0
    nums_u = 0
    for elem in reversed(left):
        if elem < tree_value:
            nums_l += 1
            continue
        if elem == tree_value:
            nums_l += 1
            break
        else:
            nums_r += 1
            break
    
    for elem in right:
        if elem < tree_value:
            nums_r +=1
            continue
        if elem == tree_value:
            nums_r += 1
            break
        else:
            nums_r += 1
            break

    for elem in reversed(up):
        if elem < tree_value:
            nums_u += 1
            continue
        if elem == tree_value:
            nums_u += 1
            break
        else:
            nums_u += 1
            break

    for elem in down:
        if elem < tree_value:
            nums_d += 1
            continue
        if elem == tree_value:
            nums_d += 1
            break
        else:
            nums_u += 1
            break
    
    return (nums_l * nums_r * nums_d * nums_u)
    
    


if __name__ == "__main__":
    
    lines_raw = read_file(r"datasets\8.txt")
    lines_raw = np.array([list(n) for n in lines_raw])

    lines = lines_raw.astype(np.int)
    print(lines)

    scenic_scores = []
    counter = 0
    for i, line in enumerate(lines):
        for y, l in enumerate(line):

            curr_col = lines[:,y] #Returns column
            up = list(curr_col[:-(len(curr_col)-i)])
            down = curr_col[i+1:]

            row = [x for x in line]
            left = row[:-(len(row)-y)]
            right = row[y+1:]
            
            ri = [x for x in right if x <= l]
            le = [x for x in left if x <= l]
            up = [x for x in up if x <= l]
            do = [x for x in down if x <= 1]
            
            beb = compute_scenic_score(l, left, right, up, down)
            scenic_scores.append(beb)
            if i == 0 or i == (len(lines) -1):



                counter += 1
                continue
            elif y == 0 or y == (len(line) - 1):
                counter += 1
                continue
            else: 
                #Check left 
                if all(x < l for x in left):
                    counter += 1
                    print(l)
                    continue
                #Check right
                if all(x < l for x in right):
                    counter += 1
                    print(l)
                    continue
                #check down
                if all(x < l for x in up):
                    counter += 1
                    print(l)
                    continue
                #Check up 
                if all(x < l for x in down):
                    counter += 1
                    print(l)
                    continue

    print(f"Part one: {counter}")
    print(f"Part two: {max(scenic_scores)}")

