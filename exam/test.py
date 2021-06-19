# def two(arg1):
#     if arg1 % 3 == 0 and arg1 % 5 ==0:
#         return "fizzbuzz"
#     elif arg1 % 3 == 0:
#         return "fizz"
#     elif arg1 % 5 == 0:
#         return "buzz"
#     else:
#         return "null"

# testing = two(10)

# print(testing)

# # def three(input):
# #     input = input.lower()
# #     count = 0 
# #     word_length = len(input)
# #     for letter in range(word_length):
# #         if input[letter] == "a":
# #             count += 1
# #         elif input[letter] == "e":
# #             count += 1 
# #         elif input[letter] == "i":
# #             count += 1 
# #         elif input[letter] == "o":
# #             count += 1 
# #         elif input[letter] == "u":
# #             count += 1 
# #     return count

# def four(input):
#     for letter in range(len(input)):
#         if input[letter] == "e" and input[letter+1] == "i":
#             if input[letter-1] == "c":
#                 return True
#             else:
#                 return False
#         elif input[letter] == "i" and input[letter+1] == "e":
#             if input[letter-1] == "c":
#                 return False
#             else:
#                 return True

# testing = four("glacier")
# testing2 = four("believe")

# print(testing)
# print(testing2)

# def five(input):
#     import math 
#     return math.factorial(input)

# test = five(8)
# print(test)

def five(input):
    total = 1
    for num in range(1, input+1):
        total *= num
    return total 

test = five(8)
print(test)