#! /usr/bin/env python3
#Multiclipboard

# Usage: 
# ./mcb.pyw save <keyword> - Saves clipboard to keyword.
# ./mcb.pyw <keyword> - Load keyword to clipboard.
# ./mcb.pyw list - Load all keywords to clipboard.
# ./mcb_ext.pyw delete <keyword>- Deletes saved keyword and contents
# ./mcb_ext.pyw delete_all - Deletes all keywords from clipboard


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(sys.argv[2] + ' has been loaded succesfully')

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
    print(sys.argv[2] + ' deleted')


elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print('List of all keyword copied to clipboard.')
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(sys.argv[1] + ' copied to clipboard')
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
        print('All keywords and associated contents have been deleted.')



mcbShelf.close()


