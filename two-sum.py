# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


idx = defaultdict(int)
        n = len(nums)
        for i in range(n):
            if target - nums[i] in idx:
                return [i, idx[target-nums[i]]]
            else:
                idx[nums[i]] = i