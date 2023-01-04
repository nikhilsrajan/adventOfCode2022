import copy
import typing


def move(
    crates:typing.Dict[int, typing.List[str]],
    move_reverse:bool,
    from_crate_id, 
    move_count, 
    to_crate_id,
):
    crates = copy.deepcopy(crates)
    from_crate = crates[from_crate_id]
    to_crate = crates[to_crate_id]
    to_move = from_crate[-move_count:]
    if move_reverse:
        to_move.reverse()
    to_crate += to_move
    from_crate = from_crate[:-move_count]
    crates[from_crate_id] = from_crate
    crates[to_crate_id] = to_crate
    return crates


def parse(instruction:str):
    splits = instruction.split(' ')
    return {
        'from_crate_id': int(splits[3]),
        'to_crate_id': int(splits[5]),
        'move_count': int(splits[1]),
    }


def get_output(
    crates:typing.Dict[int, typing.List[str]], 
    input_filepath:str, 
    move_reverse:bool,
):
    with open(input_filepath, 'r') as h:
        for line in h.readlines():
            instruction = line.replace('\n', '')
            crates = move(
                crates=crates,
                move_reverse=move_reverse,
                **parse(instruction=instruction)
            )
    output = ''
    keys = list(crates.keys())
    keys.sort()
    for key in keys:
        output += crates[key][-1]
    return output


crates = {
    1: ['Z', 'T', 'F', 'R', 'W', 'J', 'G'],
    2: ['G', 'W', 'M'],
    3: ['J', 'N', 'H', 'G'],
    4: ['J', 'R', 'C', 'N', 'W'],
    5: ['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M'],
    6: ['S', 'R', 'T', 'D', 'V', 'W', 'C'],
    7: ['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V'],
    8: ['S', 'J', 'N', 'M', 'G', 'C'],
    9: ['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L'],
}


output_task_1 = get_output(
    crates=crates,
    input_filepath='input.txt',
    move_reverse=True,
)

output_task_2 = get_output(
    crates=crates,
    input_filepath='input.txt',
    move_reverse=False,
)


print('task 1:', output_task_1)
print('task 2:', output_task_2)