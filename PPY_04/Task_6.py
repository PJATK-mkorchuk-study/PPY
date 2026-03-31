lst = []

while True:
    user_input = input("Enter sizes: ")
    temp_tupl = ()
    
    if user_input == "":
        break
    nums = tuple(int(x) for x in user_input.split())
    if len(nums) == 1:
        temp_tupl = ("S", nums, nums[0]**2)
    elif len(nums) == 2:
        temp_tupl = ("R", nums, nums[0] * nums[1])
    else:
         temp_tupl = ("C", nums, nums[0] * nums[1] * nums[2])
    lst.append(temp_tupl)
print(lst)