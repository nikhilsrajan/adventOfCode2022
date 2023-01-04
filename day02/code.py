ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN = 6


elf_move_map = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
}

my_move_map = {
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS,
}

elf_move_my_move_outcome_map = {
    ROCK: {
        PAPER: WIN,
        SCISSORS: LOSE,
    },
    PAPER: {
        ROCK: LOSE,
        SCISSORS: WIN,
    },
    SCISSORS: {
        ROCK: WIN,
        PAPER: LOSE
    }
}

outcome_map = {
    'X': LOSE,
    'Y': DRAW,
    'Z': WIN,
}

elf_move_outcome_my_move_map = {
    elf_move : {
        outcome: my_move
        for my_move, outcome in my_move_outcome_dict.items()
    }
    for elf_move, my_move_outcome_dict in elf_move_my_move_outcome_map.items()
}


def get_score_1(elf_move, my_move):
    shape_score = my_move

    if elf_move == my_move:
        outcome_score = DRAW
    else:
        outcome_score = elf_move_my_move_outcome_map[elf_move][my_move]
    
    return shape_score + outcome_score


def get_score_2(elf_move, outcome):
    output_score = outcome

    if outcome == DRAW:
        shape_score = elf_move
    else:
        shape_score = elf_move_outcome_my_move_map[elf_move][outcome]
    
    return shape_score + output_score


game_score_1 = 0
game_score_2 = 0
with open('input.txt', 'r') as h:
    for line in h.readlines():
        line = line.replace('\n', '')
        L, R = line.split(' ')
        elf_move = elf_move_map[L]
        my_move = my_move_map[R]
        outcome = outcome_map[R]
        game_score_1 += get_score_1(
            elf_move=elf_move, my_move=my_move,
        )
        game_score_2 += get_score_2(
            elf_move=elf_move, outcome=outcome,
        )

print('task 1 :', game_score_1)
print('task 2 :', game_score_2)