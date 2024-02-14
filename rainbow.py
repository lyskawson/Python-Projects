import time, sys, bext




time.sleep(1)

indent = 0  
indentIncreasing = True 

try:
    while True:  
        print(' ' * indent, end='')
        bext.fg('red')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('purple')
        print('##')

        if indentIncreasing:
         
            indent = indent + 1
            if indent == 50:  
                indentIncreasing = False
        else:
            
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True

        time.sleep(0.02)  # Add a slight pause.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
