def twoSum(nums, target):
    seens = {}

    for i in range(len(nums)):
        now = target - nums[i] # (7)
        if now in seens: # is 7 in seens?
            return [seens[now], i]
        else:
            seens[nums[i]] = i # {2, 0}



print(twoSum(nums = [3,2,4], target = 6))
