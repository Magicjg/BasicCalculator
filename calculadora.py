#Calculator v1 

import os


    
print('1)Addition')
print('2)Subtraction')
print('3)Multiply')
print('4)Split')
print('5) exit')
print('')
    

dec = str(input('Choose an option: '))

os.system("clear")

if dec=='1':
        num1 = float(input('Insert your first number: '))
        num2 = float(input('Insert your second number: '))
        res = num1 + num2
        print('Result:  '+ str(res))
elif dec=='2':
        num1 = float(input('Insert your first number: '))
        num2 = float(input('Insert your second number: '))
        res = num1 - num2
        print('Result:  ' + str(res))
elif dec=='3':
        num1 = float(input('I5nsert your first number: '))
        num2 = float(input('insert your second number: '))
        res = num1 * num2
        print('Result:  ' + str(res))
elif dec=='4':
        num1 = float(input('insert your first number:'))
        num2 = float(input('insert your second number: '))
        if num1 == 0:
                print('You can`t divide zero')
                quit()
        if num2 == 0:
                print('you can`t divide by zero')
                quit()
                

        res = num1 / num2 
        print('Result: '+ str(res))
elif dec=='5':
        print('BYE')
        
else:
       print('BYE') 

