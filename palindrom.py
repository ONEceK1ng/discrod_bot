# palidromus = 121
#
# # i = 121
# #
# # o = 1234 % 10
# #
# # s = 1234 % 100
# # t = 1234 % 1000
# # x = 1234 % 10000
# number = 12345
#
# number_1 = number
# result = []
# while number_1 > 0:
#     result.append(number_1 % 10)
#     number_1 //= 10
# x = result
# print(x)
#
# res = int(''.join(map(str, x)))
# print(type(res))
# print(res)
#
# number_2 = number
# print(type(number_2))
# print(number_2)
#
# if number_2 == res or number_1 == res:
#     print("yes")
# else:
#     print("No")

# print(y)



# for i in range(len(str(number))//2):
#     if str(number)[i] != str(number)[-1-i]:
#         print('No Palindrome')
#         quit()
#
# print('Palindrome')

# for i in range(len(str(number))//2):
#     print(i)
#     print("Yse")
#
# result = []
# while number > 0:
#     result.append(number % 10)
#     number //= 10
# x = result




# a = i % 10
# b = (i // 10) % 10
# c = (i // 10) // 10


# x = (i%10000)
# print(x)

# while i >= 0:
#     result.append(i % 10)
#     print(i)

# while i > 0:
#     result.append(i % 10)
#     result.append((i // 10) % 10)
#     result.append((i // 10) // 10)
#     # i //= 10
#     print(i)
#
# # x = result_1
# t = sum(result)
# print(t)
#
#
#
# if x == t:
#     print("Yes")
# else:
#     print("No")

# a = i % 10
# b = (i // 10) % 10
# c = (i // 10) // 10
# if ( a == c and a == b and b == c) or (a == c):
#     print("Yes")
# else:
#     print("No")


number = int(input())

reversed_number = 0
tmp_original = number

while tmp_original > 0:
    reversed_number = (reversed_number * 10) + tmp_original % 10
    tmp_original = tmp_original // 10

if number == reversed_number:
    print("Palindrom")
else:
    print("No Palindrom")