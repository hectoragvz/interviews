def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    sol = []
    nums.sort

    for index, value in enumerate(nums):
        if index > 0 and value == nums[index-1]:
            continue
        
        left, right = index+1, len(nums) - 1
        while left < right:
            sum = value + nums[left] + nums[right]
            if sum < 0:
                left += 1
                print("less")
            elif sum > 0:
                right -= 1
                print("More")
            else:
                print("Found")
                sol.append([value, nums[left], nums[right]])   
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left +=1
    return sol
            
print(threeSum(nums=[-1, 0, 1, 2, -1, -4]))