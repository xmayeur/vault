import getpass
import sys

import crypto_helpers as c

db = input('Enter the database pathname: ')
# c.create_table_id_tbl(db)
aes = c.AEScipher(db=db)
uid = input('Enter a IdentityId: ')

if uid == 'dump':
    print(aes.dump())
elif uid == 'load':
    pass
elif uid == 'create':
    c.create_table_id_tbl(db)
else:
    
    uname, pwd = aes.read(uid)
    
    if uname == '':
        uname = input('Enter a new User Name: ')
        pwd1 = getpass.getpass('Enter a new password: ')
        pwd2 = getpass.getpass('Repeat the new password: ')
        if pwd1 != pwd2:
            print('Password mismatch!')
            sys.exit(1)
        else:
            aes.save(uid, uname, pwd1)
            sys.exit(0)
    else:
        pwd1 = getpass.getpass('Enter current password: ')
        if pwd1 != pwd:
            print('Password mismatch!')
            sys.exit(1)
        else:
            pwd1 = getpass.getpass('Enter a new password: ')
            pwd2 = getpass.getpass('Repeat the new password: ')
            if pwd1 != pwd2:
                print('Password mismatch!')
                sys.exit(1)
            elif pwd1 == '' and pwd2 == '':
                aes.remove(uid, pwd)
                sys.exit(0)
            else:
                aes.save(uid, uname, pwd1)
                print('Identity saved!')
                sys.exit(0)
