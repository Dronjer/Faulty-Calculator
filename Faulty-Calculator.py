print('Calculator')
print('Enter the 1st digit')
num1 = int(input())
print('Enter the 2nd digit')
num2 = int(input())
print('Select the operator you want perform')
print('Add, Subtract, Multiply, Divison')
action = input()
if action == 'Add':
    if num1 == 56 and num2 == 9:
        print(77)
    elif num1 == 9 and num2 == 56:
        print(77)
    else:
        print(num1 + num2)
elif action == 'Subtract':
    if num1>num2:
        print(num1-num2)
    else:
        print(num2-num1)
elif action == 'Multiply':
    if num2 == 45 and num1 == 3:
        print(555)
    elif num2 == 3 and num1 == 45:
        print(555)
    else:
        print(num1*num2)
else:
    if num1 == 56 and num2 == 6:
        print(4)
    elif num2<num1:
        print(num1/num2)
    else:
        print(num2/num1)

