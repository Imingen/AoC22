
crates = [
		["S", "L", "F", "Z", "D", "B", "R", "H"],
		["R", "Z", "M", "B", "T"],
		["S", "N", "H", "C", "L", "Z"],
		["J", "F", "C", "S"],
		["B", "Z", "R", "W", "H", "G", "P"],
		["T", "M", "N", "D", "G", "Z", "J", "V"],
		["Q", "P", "S", "F", "W", "N", "L", "G"],
		["R", "Z", "M"],
		["T", "R", "V", "G", "L", "C", "M"]
]


with open("datasets\\5.txt") as f:
	lines = f.read().splitlines()
	for line in lines:
		line = line.split()
		amount = int(line[1])
		source = int(line[3])
		dest = int(line[5])

		tmp = crates[source-1]
		t = tmp[:amount]

		for el in t:
			crates[dest-1].insert(0, el)
			crates[source-1].pop(0)


result = ""
for elem in crates:
	result += elem[0]


print(result)