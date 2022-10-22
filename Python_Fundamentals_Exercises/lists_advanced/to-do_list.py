to_do_list = input()
tasks = []
while to_do_list != 'End':
    to_do_list = to_do_list.split("-")
    priority = int(to_do_list[0])
    task = to_do_list[1]

    tasks.append((priority, task))
    to_do_list = input()

sorted_list = [x[1] for x in sorted(tasks)]

print(sorted_list)
