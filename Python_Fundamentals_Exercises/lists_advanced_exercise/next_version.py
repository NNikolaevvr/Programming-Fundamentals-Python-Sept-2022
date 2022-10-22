version = [int(x) for x in input().split(".")]

version[2] += 1

if version[2] > 9:
    version[2] = 0

if version[2] == 0:
    version[1] += 1
    if version[1] > 9:
        version[1] = 0


if version[2] == 0:
    if version[1] == 0:
        version[0] += 1


print(*version, sep=".")


# another solution

version = [int(number) for number in input().split(".")]
version[-1] += 1
for index in range(len(version) - 1, -1, -1):
    if version[index] > 9:
        version[index] = 0
        if index - 1 >= 0:
            version[index - 1] += 1
print('.'.join(str(number) for number in version))