
for l, c, r in board:
   print(l, c, r)
 
# 1 2 3
# 4 4 4
# 7 8 9

choices = {
    'top-left': [0,0],
    'top-center': [0,1],
    'top-right': [0,2],
    'center-left': [1,0],
    'center': [1,1],
}

for key in choices.keys():
   print(key)
 
# top-left
# top-center
# top-right
# center-left
# center

for value in choices.values():
   print(value)
 
# [0, 0]
# [0, 1]
# [0, 2]
# [1, 0]
# [1, 1]

for key, value in choices.items():
   print(key, value)
 
# top-left [0, 0]
# top-center [0, 1]
# top-right [0, 2]
# center-left [1, 0]
# center [1, 1]

choices.get()

for key, value in choices.items():
   print(key)
   print(value)
 
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
