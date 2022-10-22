def sorting_numbers(nums):
    nums = [int(x) for x in nums]
    current_group = 0
    max_value = max(nums)
    group_of = []
    while max_value > current_group:
        current_group += 10
        group_of.clear()
        if len(nums) != 0:
            for i in nums:
                if int(i) <= current_group:
                    group_of.append(i)
            for o in group_of:
                nums.remove(o)

        print(f"Group of {current_group}'s: {group_of}")


numbers = input().split(", ")

sorting_numbers(numbers)
