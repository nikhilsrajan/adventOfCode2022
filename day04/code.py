def parse(line):
    elf_assignment = []
    for elf_n_str in line.split(','):
        splits = elf_n_str.split('-')
        elf_n = (int(splits[0]), int(splits[1]))
        elf_assignment.append(elf_n)
    return tuple(elf_assignment)


def is_fully_overlapping(elf_1, elf_2):
    return (elf_1[0] <= elf_2[0] and elf_2[1] <= elf_1[1]) \
        or (elf_2[0] <= elf_1[0] and elf_1[1] <= elf_2[1])
    

def is_overlapping(elf_1, elf_2):
    return (elf_1[0] <= elf_2[0] and elf_2[0] <= elf_1[1]) \
        or (elf_1[0] <= elf_2[1] and elf_2[1] <= elf_1[1]) \
        or is_fully_overlapping(elf_1=elf_1, elf_2=elf_2)


is_fully_overlapping_list = []
is_overlapping_list = []
with open('input.txt', 'r') as h:
    for line in h.readlines():
        line = line.replace('\n', '')
        is_fully_overlapping_list.append(
            is_fully_overlapping(*parse(line=line))
        )
        is_overlapping_list.append(
            is_overlapping(*parse(line=line))
        )


print('task 1:', sum(is_fully_overlapping_list))
print('task 2:', sum(is_overlapping_list))