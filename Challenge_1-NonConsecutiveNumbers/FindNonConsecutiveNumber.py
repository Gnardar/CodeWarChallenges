def findNonConsecNum(nums=[]):
    print("Checking ", nums)
    x = 0
    for num in nums:
        if (x+1) < len(nums):
            if int(nums[x+1])-int(num) > 1:
                return nums[x+1]
            elif int(nums[x+1])-int(num) < -1:
                return nums[x+1]
            else:
                x += 1
        else:
            return



numList=[-1,-2,-3,-5,-6,-7]
print(findNonConsecNum(numList))