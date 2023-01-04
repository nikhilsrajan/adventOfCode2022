class F(object):
    NODE_COUNTER = 0
    def __init__(self, name, is_file:bool, parent=None, size:int=-1):
        self.name = name
        self.parent = parent
        self.children = {}
        self.is_file = is_file
        self.size = size
        self.id = F.NODE_COUNTER
        F.NODE_COUNTER += 1
    
    def add_child(self, name, is_file, size:int=-1):
        self.children[name] = F(name=name, is_file=is_file, parent=self, size=size)
        return self.children[name]


class FileSystem(object):
    def __init__(self):
        self.root = F(name='/', is_file=False)
        self.pointer = self.root
    
    def make_directory(self, name):
        self.pointer.add_child(name=name, is_file=False)

    def make_file(self, name, size):
        self.pointer.add_child(name=name, is_file=True, size=size)
    
    def cd(self, name):
        if name == '..':
            self.pointer = self.pointer.parent
        else:
            self.pointer = self.pointer.children[name]


def F_to_dict(f:F, _dict:dict={}):
    if f.is_file:
        _dict[f.name] = f.size
    else:
        _dict[f.name] = {}
        for child_f in f.children.values():
            F_to_dict(f=child_f, _dict=_dict[f.name])
    return _dict


def get_size(f:F):
    size = 0
    if f.is_file:
        size += f.size
    else:
        for child in f.children.values():
            size += get_size(f=child)
    return size


def get_size_of_all_folders(f:F, dir_size={})->dict:
    if not f.is_file:
        dir_size[f.id] = get_size(f)
        for child in f.children.values():
            dir_size = get_size_of_all_folders(f=child, dir_size=dir_size)
    return dir_size


def create_fs_from_input_txt(input_filepath):
    with open(input_filepath, 'r') as h:
        lines = [line.replace('\n', '') for line in h.readlines()]

    fs = FileSystem()

    i = 1
    while i < len(lines):
        line = lines[i]
        splits = line.split(' ')
        if splits[0] != '$':
            raise ValueError('something is wrong [1]')
        if splits[1] == 'ls':
            i += 1
            while i < len(lines) and lines[i].split(' ')[0] != '$':
                splits = lines[i].split(' ')
                if splits[0] == 'dir':
                    fs.make_directory(name=splits[1])
                else:
                    fs.make_file(name=splits[1], size=int(splits[0]))
                i += 1
        elif splits[1] == 'cd':
            fs.cd(name=splits[2])
            i += 1
        else:
            raise ValueError('something is wrong [2]')
    
    return fs


fs = create_fs_from_input_txt(input_filepath='input.txt')

dir_size_dict = get_size_of_all_folders(f=fs.root, dir_size={})

dir_size_sum_lte_100000 = 0
for dir_id, dir_size in dir_size_dict.items():
    if dir_id == dir_size_dict[fs.root.id]:
        continue
    if dir_size <= 100000:
        dir_size_sum_lte_100000 += dir_size
    
print('task 1:', dir_size_sum_lte_100000)


total_disk_space = 70000000
space_required_for_update = 30000000
occupied_space = dir_size_dict[fs.root.id]
space_to_free_up = space_required_for_update - (total_disk_space - occupied_space)


dir_size_list = list(dir_size_dict.values())
dir_size_list.sort()


for dir_size in dir_size_list:
    if dir_size >= space_to_free_up:
        break

print('task 2:', dir_size)