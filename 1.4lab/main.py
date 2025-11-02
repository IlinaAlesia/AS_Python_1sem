# 4 вариант Ильина
print("Исходный список:", numbers)
even=[]
for i in range(len(numbers)):
    if numbers[i]%2==0:
      even.append(numbers[i])
        even.sort()
odd=[]
for i in range(len(numbers)-1,-1,-1):
    if numbers[i]%2==1:
      odd.append(numbers[i])
        odd.sort(reverse=True)
print("\nЧётные:", even)
print("Нечётные:",odd)
print(even+odd)
