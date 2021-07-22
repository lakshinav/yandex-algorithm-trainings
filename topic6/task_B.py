n,k = tuple(map(int, input().split()))
sorted_nums = list(map(int, input().split()))
nums_to_find = list(map(int, input().split()))

def nearest_value(sorted_nums, num):
    left = 0
    right = len(sorted_nums)
    while left < right:
        mid = (left + right) // 2
        if sorted_nums[mid] == num:
            return sorted_nums[mid]
        elif num < sorted_nums[mid]:
            right = mid
        else:
            left = mid + 1

    if left != len(sorted_nums) and (left == 0 or abs(sorted_nums[left] - num) < abs(sorted_nums[left - 1] - num)):
        return sorted_nums[left]
    return sorted_nums[left - 1]


def nearest_value_for_list(sorted_nums, nums_to_find):
    results = []
    for num in nums_to_find:
        results.append(nearest_value(sorted_nums, num))
    return results


results = nearest_value_for_list(sorted_nums, nums_to_find)
for result in results:
    print(result)
