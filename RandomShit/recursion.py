def eme(nums):
    nums_str = str(nums)
    
    total = 0
    for char in nums_str:
        total += int(char)
    print(f"Calculated sum: {total}")

    if total < 10:
        return total
    
    return eme(total)

print(f"Final Result: {eme('492')}")