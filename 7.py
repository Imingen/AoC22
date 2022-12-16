from file_reader import read_file


class Folder:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []
        self.curr_node = self
        self.total = 0
        self.smallest = []
        

    def find_smallest(self):
        smallest = Folder("Max", None)
        smallest.bigness = 9999999999999999999999999
        for s in self.smallest:
            if int(s.bigness) <= int(smallest.bigness):
                smallest = s

        x = [s.bigness for s in self.smallest]
        print(f"Smallest: {smallest.name} with size {smallest.bigness}")
        print(min(x))



    def find_size_of_dir(self):
        self.bigness = 0
        for child in self.children:
            child.find_size_of_dir()
        self.size(self.bigness)
    
    def size(self, bigness):
        s = bigness
        for si in self.files:
            s += int(si.size)
        print(f"Size of dir {self.name} is: {s}")
        if s <= 100000:
            root.total += s
        self.bigness = s
        if s >= 2750324:
            root.smallest.append(self)

        if self.parent:
            self.parent.bigness += s

    def print(self):
        for child in self.children:
            child.print()
        self.pprint()

    def pprint(self):
        print(f"Current dir: {self.name}")
        for file in self.files:
            print(f"{file.name}. Size: {file.size}")
        for child in self.children:
            print(f"dir {child.name}")



    def do_ls(self, commands):
        assert self.curr_node is not None
        for cmd in commands:
            if not cmd.startswith("$"):
                if cmd.startswith("dir"):
                    self.curr_node.children.append(Folder(cmd.split()[1], parent=self.curr_node))
                else:
                    self.curr_node.files.append(File(cmd.split()[1], cmd.split()[0]))
            else:
                break
        return
        
    def do_cd(self, command):
        dest_folder = command.split()[2]
        tmp = None
        assert self.curr_node is not None
        for child in self.curr_node.children:
            if child.name == dest_folder:
                tmp = child
                self.curr_node = child
                break
        return tmp

    def do_cd_up(self):
        assert self.curr_node is not None
        return self.curr_node.parent

    def parse_commands(self, commands):
        for i, cmd in enumerate(commands):
            if cmd == "$ ls":
                self.do_ls(commands[i+1:])
            if cmd.startswith("$ cd"):
                if cmd == "$ cd ..":
                    self.curr_node = self.do_cd_up()
                else:
                    self.curr_node = self.do_cd(cmd)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


if __name__ == "__main__":
    commands = read_file(r"C:\Users\marisi\source\repos\AdventOfCode2022\datasets\7.txt")
    root = Folder("/", None)
    curr_node = root
    root.curr_node = root
    root.parse_commands(commands[1:])
    root.print()
    print("XD")
    root.find_size_of_dir()
    print(f"Total is {root.total}")
    x = 30000000 - (70000000 - root.bigness)
    print(x)
    root.find_smallest()
