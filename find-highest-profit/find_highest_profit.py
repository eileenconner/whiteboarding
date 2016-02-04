# interview cake problem
# input: list of stock prices (ints) at time corresponding to index by minute
# find greatest diff
# what is greatest profit you could make (buy at index lower than you sell)
# example input: [6,3,10,12,3,11] output: return 12-3, which is 9
# example input: [100, 98, 50] output: 100-98, which is -2


def find_highest_profit(nums):
    """Find highest profit - O(N^2)"""
    difference = None
    temp = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                temp = nums[j] - nums[i]
                if difference is None or temp > difference:
                    difference = temp
    return difference


def find_highest_profit_2(nums):
    """Find highest profit - one pass through list, O(N)"""
    minimum = nums[0]
    maximum = nums[1] - nums[0]
    for i in range(1, len(nums)):
        current_diff = nums[i] - minimum
        if current_diff > maximum:
            minimum = current_diff
        if nums[i] < minimum:
            minimum = nums[i]
    return maximum
