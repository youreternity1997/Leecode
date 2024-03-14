#%% list copy pass by reference
a = [1,2,3]
a_ref = a
a_ref.append(4)
print("a: ", a)
print("a_ref: ", a_ref)
print("{}{}".format("a:", f"id:{id(a)}"))
print("{}{}".format("a_ref:", f"id:{id(a_ref)}\n"))


#%% list copy
a_list = list(a)
a_index = a[:]
a_copy = a.copy() # 淺複製Shallow copy
a.append(5)
print("Shallow copy")
print("{:<15}{:<20}{}".format("a:", f"{a}", f"id:{id(a)}"))
print("{:<15}{:<20}{}".format("a_list:", f"{a_list}", f"id:{id(a_list)}"))
print("{:<15}{:<20}{}".format("a_index:", f"{a_index}", f"id:{id(a_index)}"))
print("{:<15}{:<20}{}".format("a_copy:", f"{a_copy}", f"id:{id(a_copy)}\n"))

print("Deep copy")
# 深複製 deep copy 
import copy
a = [1, [2,3]]
a_deepcopy = copy.deepcopy(a)


#%% Shallow copy and deep copy
import copy
a = [1, [2,3]]
a_ref = a
a_shallowcopy = copy.copy(a)
a_deepcopy = copy.deepcopy(a)

print("{:<15}{:<20}{}".format("a:", f"{a}", f"id:{id(a_ref)}"))
print("{:<15}{:<20}{}".format("a_shallow_copy:", f"{a_shallowcopy}", f"id:{id(a_shallowcopy)}"))
print("{:<15}{:<20}{}".format("a_deepcopy:", f"{a_deepcopy}", f"id:{id(a_deepcopy)}"))

a[0] = 4
print("\nChange immutable part: a[0] = 4")
print("{:<15}{:<20}{}".format("a:", f"{a}", f"id:{id(a_ref)}"))
print("{:<15}{:<20}{}".format("a_shallow_copy:", f"{a_shallowcopy}", f"id:{id(a_shallowcopy)}"))
print("{:<15}{:<20}{}".format("a_deepcopy:", f"{a_deepcopy}", f"id:{id(a_deepcopy)}"))
print("其中 a[0] 為數字，即為不可變型別，則深／淺複製沒有差別")


a[1][1] = 5
print("\nChange mutable part: a[1][1] = 5")
print("{:<20}{:<20}{}".format("a:", f"{a}", f"id:{id(a_ref)}"))
print("{:<20}{:<20}{}".format("a_shallow_copy:", f"{a_shallowcopy}", f"id:{id(a_shallowcopy)}"))
print("{:<20}{:<20}{}".format("a_deepcopy:", f"{a_deepcopy}", f"id:{id(a_deepcopy)}"))
print("其中 a[1][1] 為list，即為可變型別，可以發現淺複製 (shallow copy) 被改變了，而深複製 (deep copy) 則沒有被改變")

print("\nCheck variable id at deep level")
print("{:<20}{:<20}{}".format("a[1][1]:", f"{a[1][1]}", f"id:{id(a[1][1])}"))
print("{:<20}{:<20}{}".format("a_shallowcopy[1][1]:", f"{a_shallowcopy[1][1]}", f"id:{id(a_shallowcopy[1][1])}"))
print("{:<20}{:<20}{}".format("a_deepcopy[1][1]:", f"{a_deepcopy[1][1]}", f"id:{id(a_deepcopy[1][1])}"))