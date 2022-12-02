num1 = 0
num2 = 1
vvodish = int(input("Введите номер последнего элемента числа Фибаначчи: "))
for i in range(vvodish):
    sum = num1 + num2
    num1 = num2
    num2 = sum
print("Ответ = ", num1)