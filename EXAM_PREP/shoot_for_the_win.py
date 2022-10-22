def shot_targets(targets, index):
    value = targets[index]
    targets[index] = -1

    for i in range(len(targets)):
        if targets[i] == -1:
            continue
        if value < targets[i]:
            targets[i] -= value

        else:
            targets[i] += value

    return targets


targets = [int(x) for x in input().split(" ")]
command = input()
counter_of_shot_targets = 0

while command != 'End':
    index = int(command)

    if 0 <= index < len(targets) and targets[index] != -1:
        counter_of_shot_targets += 1
        shot_targets(targets, index)

    command = input()

final_list = [str(x) for x in targets]
print(f"Shot targets: {counter_of_shot_targets} -> {' '.join(final_list)}")