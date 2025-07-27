#main focus area is List, Tupple, Set, Dictionary

# List :  ordered, mutable, Heterogeneous data structure

my_list = [10, "hello", 3.14, True]
#print(my_list)

#---------Creating List
empty = []
nums = [1, 2, 3, 0, 10]
mixed = [1, "hello", 4.5, [10, 20]]
from_list = list("abc")  # ['a', 'b', 'c']
print(from_list)
print(type(from_list))

#---------- Acessing List's Element
print(nums[0])
#---------- Modifying List's Element
nums[1]=69
print(nums[1])

# ----- Adding / Removing Items on list
nums.append(60)

nums.remove (60)
nums.pop()          # Removes and returns last item 
nums.pop(1)         # Removes and returns item at index 1
del nums[0]         # Deletes item at index 0
nums.clear()        # Empties the list

#------ Concatenation
concat= from_list + mixed 
print(concat)

# repetition 