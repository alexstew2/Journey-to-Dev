# board = [[[],[],[]],[[],[],[]],[[],[],[]]]
# for l, c, r in board:
#    print(l, c, r)
 
# 1 2 3
# 4 4 4
# 7 8 9

# choices = {
#     'top-left': [0,0],
#     'top-center': [0,1],
#     'top-right': [0,2],
#     'center-left': [1,0],
#     'center': [1,1],
# }

# for key in choices.keys():
#    print(key)
 
# top-left
# top-center
# top-right
# center-left
# center

# for value in choices.values():
#    print(value)
 
# [0, 0]
# [0, 1]
# [0, 2]
# [1, 0]
# [1, 1]

# for key, value in choices.items():
#    print(key, value)
 
# top-left [0, 0]
# top-center [0, 1]
# top-right [0, 2]
# center-left [1, 0]
# center [1, 1]

# choices.get()

# for key, value in choices.items():
#    print(key)
#    print(value)
 
# top-left
# [0, 0]
# top-center
# [0, 1]
# top-right
# [0, 2]
# center-left
# [1, 0]
# center
# [1, 1]

# def switcher(player):
#    player = (player + 1) % 2
#    print(player)


# switcher(switcher(1))


# for

# def min(arr):
#    min_num = arr[0]
#    for number in arr:
#       if number < min_num:
#          min_num = number

#    return min_num

# def evens(numbers):
#    even_list = []
#    for num in numbers:
#       if num % 2 == 0:
#          even_list.append(num)
#    return even_list



# print(min([2,3,-5,2,6,8,9,-10,2,67]))

# lists

names = ["Jack", "Penny", "Austin", "Alex", "Matt"]

# for i in range(len(names)):
#    names[i] = names[i].lower()
# print(names)

# range(len(list)) 

# for i in range(4):
#    print(i)

# # print first item
# print(names[0])
# # length
# print(len(names))
# # last item
# print(names[len(names) - 1])

# # print all but the first two
# print(names[2:])

# # print only the first two
# print(names[:2])

# # slice syntax list[start:stop:step]


def list_to_dict(names):
   name_dict = {}
   for index, value in enumerate(names):
      name_dict[index] = value
   return name_dict

print(list_to_dict(names))