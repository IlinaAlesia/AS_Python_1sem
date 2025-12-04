# 4 вариант Ильина
str1 = "первая"
str2 = "вторая"
new_str1 = str2[0] + str1[1] + str1[2:]  # "П" + "е" + "рвая"
new_str2 = str1[0] + str2[1] + str2[2:]  # "в" + "т" + "орая"
result = new_str1 + " " + new_str2
print(result)
