# 4 задание Ильина
print("Исходный список:", numbers)
even=[]
for i in range(len(numbers)):
    if numbers[i]%2==0:
      even.append(numbers[i])
odd=[]
for i in range(len(numbers)-1,-1,-1):
    if numbers[i]%2==1:
      odd.append(numbers[i])
print("\nЧётные:", even)
print("Нечётные:",odd)
