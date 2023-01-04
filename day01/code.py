current_elf_stack = []
all_elves = []
max_elf = 0
N = -1
elf_count = 0
to_print = False
with open('input.txt', 'r') as h:
    for line in h.readlines():
        line = line.replace('\n', '')
        if line == '':
            current_elf = sum(current_elf_stack)
            all_elves.append(current_elf)
            if to_print:
                print(current_elf)
            if current_elf > max_elf:
                max_elf = current_elf
            current_elf_stack = []
            elf_count += 1
            if elf_count == N:
                break
        else:
            count = int(line)
            current_elf_stack.append(count)

all_elves.sort(reverse=True)

print('task 1:', all_elves[0])
print('task 2:',sum(all_elves[:3]))