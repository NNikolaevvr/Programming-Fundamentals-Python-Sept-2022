items = input()
resources = {}
while items != 'stop':

    quantity = int(input())

    if items not in resources.keys():
        resources[items] = 0
    resources[items] += int(quantity)

    items = input()

for current_resource, quantity in resources.items():
    print(f"{current_resource} -> {quantity}")
