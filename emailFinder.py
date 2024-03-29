import re, pyperclip 

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # main 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)
                        
emailRegex = re.compile(r'''(
    [a-zA-Z0-9.-_%+]+    # user name
    @                    # at
    [a-zA-Z0-9.-]+       # domain name    
    (\.[a-zA-Z]{2,4})    # dot and something  
    )''', re.VERBOSE)
    

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum = phoneNum + ' X' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Results copied to clipboard:')
    print('\n'.join(matches))
else: 
    print("No phone numbera or e-mail addresses found.")
