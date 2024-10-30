# # while loop = execute some code WHILE some condition remains true

# #iteration -> loops

#example 1

# name = input('Enter your name:')

# while name == '':
#     print('You did not enter your name')
#     #infinite looping 

# # else:
# #     print(f'Hello{name}')

#example 2

# age = int(input('Enter your age:'))
# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age"))

#     print(f"You are {age}years old")

#example 3

# food = input("enter a food you like(q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")
# #     print("Bye")

# #example 4

# num = int(input("Enter a # between 1- 10: "))

# while num < 1 or num >10
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))

# print("fYour number is {num}")
#________________________________________________________________________________________________
#for loops = execute a block of code a fixed number of times.
#  You can iterate a range, string, sequence, etc.

#example 1

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

#example 2

# for x in reversed(range(1, 11, 3)):
#     print(x)

# print("HAPPY NEW YEAR")

#example 3

# for x in range(1,21):
#     if x == 13:
#         continue #coninue -> skips 

#     else:
#         print(x)

# for x in range(1,21):
#     if x == 13:
#             break #break -> stops the program at at a certain point
#     else:
#         print(x)
#______________________________________________________________________________________________

# #challenge 

# list_of_names = ['John','Paul', 'George', 'Ringo']
#if the name is 'George', print 'George was found!'
#otherwise, print 'George was not found!' and print out the other names using a loop

# for name in list_of_names:
#     if name == 'George':
#         print('George was found!')
#     else:
#         print('George was not found')

# list_of_names2 = ['Thanos', 'Ironman', 'Thor', 'Hulk']
# #loop through the list_of_names2 and 
# # if the name is 'Ironman', skip over it and print out the other names'

# for name in list_of_names2:
#     if name == 'Ironman':
# #         continue
# #     print(name)

# list_of_names3 = ['Esteban', 'Lilly', 'Manny', 'Daniel']
# for name in list_of_names3:
#     if name == 'Esteban':
#         name = 'Daniel'
#     print(name)