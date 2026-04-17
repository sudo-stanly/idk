# print("wtf")


# def HAKDOG():
#     return f"HAKDOG"
    
# print(HAKDOG())


nums = input("Enter a number: ")
# print(user.split())

newList = [int(char) for char in nums]
# print(newList)

# for i in range(len(newList)):
#     print(newList[i])
    
total = 0
for i in range(len(newList)):
    print(f"{newList[i]}",end="")
    currentNum = newList[i]
    total += currentNum
    
    if i < len(newList) - 1:
        print(" + ", end="")
print(f" = {total}")