def is_palindrome_list(nums):
    if len(nums) <= 1:
        return True
    if nums[0] != nums[-1]:
        return False
    return is_palindrome_list(nums[1:-1])

print(is_palindrome_list([1,2,3,4,4,3,2,1]))