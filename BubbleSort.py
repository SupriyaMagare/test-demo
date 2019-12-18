def sort(nums):
    for i in range(len(nums)-1,0,-1):
     for j in range(i):
         if nums[j]>nums[j+1]:
             temp= nums[j]
             nums[j]=nums[j+1]
             nums[j+1]= temp


nums= [12,88,35,15,46,34,5,66]
sort(nums)
print (nums)