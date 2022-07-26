table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_cards = ["J_D", "3_D"]

# ниже ваша реализация

# heart = ["1_H", "2_H", "3_H", "4_H", "5_H", "6_H", "7_H","8_H", "9_H", "10_H", "J_H", "Q_H", "K_H", "A_H"]
# diamond = ["1_D", "2_D", "3_D", "4_D", "5_D", "6_D", "7_D","8_D", "9_D", "10_D", "J_D", "Q_D", "K_D", "A_D"]
# club = ["1_C", "2_C", "3_C", "4_C", "5_C", "6_C", "7_C","8_C", "9_C", "10_C", "J_C", "Q_C", "K_C", "A_C"]
# spides = ["1_S", "2_S", "3_S", "4_S", "5_S", "6_S", "7_S","8_S", "9_S", "10_S", "J_S", "Q_S", "K_S", "A_S"]
# flush = 


list1 = ["A_S", "2_S", "3_D", "3_S", "J_C"]
list2 = ["K_S", "8_S"]
# list1.sort()
# list2.sort()
c = []
cur_sum = []
for x in list1:
    for y in list2:
        if x[2] == y[2]:
            cur_sum.append(x)
            cur_sum.append(y)
        else:
            print("dont S")

c = set(cur_sum)

# if c == c.index[0:4]:
#     print("Flush")
# else:
#     print("No flush")

print(type(c))
print(c)
