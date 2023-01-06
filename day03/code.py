import string


item_value = {item: value for value, item in enumerate(string.ascii_letters, start=1)}


def get_compartment_intersection(rucksack:str):
    compartment_1 = set(rucksack[:len(rucksack)//2])
    compartment_2 = set(rucksack[len(rucksack)//2:])
    return list(compartment_1.intersection(compartment_2))


def get_intersection_value(intersection:list):
    return sum([item_value[item] for item in intersection])


def get_group_intersection(group:list):
    intersection = None
    for rucksack in group:
        if intersection is None:
            intersection = set(rucksack)
        else:
            intersection = set(rucksack).intersection(intersection)
    return intersection


total_sum = 0
group_badges = []
i = 0
with open('input.txt', 'r') as h:
    group = []
    for line in h.readlines():
        rucksack = line.replace('\n', '')
        group.append(rucksack)
        total_sum += get_intersection_value(
            intersection=get_compartment_intersection(
                rucksack=rucksack
            ),
        )
        i += 1
        if i == 3:
            group_badges.append(get_group_intersection(group=group))
            del group
            group = []
            i = 0


print('task 1:', total_sum)

sum_of_group_badge_values = sum([get_intersection_value(intersection=group_badge) for group_badge in group_badges])
print('task 2:', sum_of_group_badge_values)