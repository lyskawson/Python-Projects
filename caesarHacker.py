print('Caesar Cipher Hacker')
 

print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')
 

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
for key in range(len(SYMBOLS)):  
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
   
            num = SYMBOLS.find(symbol)  #number of index 
            num = num - key
            
            
            if num < 0:
                num = num + len(SYMBOLS)
            
            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol
    print('Key #{}: {}'.format(key,translated))