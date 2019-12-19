# List- Mutable - can change value
nums=[12,23,42,33,55]
print (nums)

nums.append(75)
print(nums)

nums.insert(2,77)
print(nums)

nums.remove(77)
print(nums)

nums.pop(2)
print(nums)

nums.pop()
print(nums)

del nums[2:]
print(nums)

nums.extend([22,32,42,56])
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))
nums.sort()
print(nums)