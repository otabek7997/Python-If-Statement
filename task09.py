num1 = input('A=')
num2 = input('B=')
num3 = input('C=')

if num1 == num2 or num2 == num3 or num1 == num3:
    print("Teng tomonli uchburchak")
if num1 == num2 or num1 == num3 or num2 >= num3 :
    print("Teng yonli uchburchak")
else:
    print("Turli tomonli uchburchak")   