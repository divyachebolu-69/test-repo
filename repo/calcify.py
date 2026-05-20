#features of calcify
# can do +,=,*,/ operations
# accepts full expressions (example: 1+2*3-4)
# shows error for division by zero
# allows only numbers and operators
# runs until user types 'exit'

def calcify():

    print("===== welcome to calcify - simple calculator =====")
    print("supports: addition (+), subtraction (-), multiplication (*),  division (/)")
    print("type 'exit' to quit.\n")

    while True:
        expression = input('enter expression:')

        if expression.lower() == 'exist':
            print('existing calcify')
            break

        try:
            allowed = '0123456789+-*/.()'

            if all(char in allowed for char in expression):
               result = eval(expression)
               print(f'result:{result}')
               
            else:
               print('error: invalid chars')
        except ZeroDivisionError:
           print('Error: Division by Zero')
        except Exception as e:
             print ('error: invalid expression')
calcify()

