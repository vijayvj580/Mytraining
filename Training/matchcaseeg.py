print('Hi')

ch=int(input('enter a num:'))
match (ch):
    case 1:
        print('one')
    case 2:
        print('Two')


ch=int(input('enter a num:'))
match (ch):
    case 1:
        print('one')
    case 2:
        print('Two')
    case _:
        print('none')


ch=(input('enter a num:'))
match (ch):
    case '1':
        print('one')
    case '2':
        print('Two')
    case _:
        print('none')

ch=float(input('enter a num:'))
print(ch)
match (ch):
    case 1:
        print('one')
    case 2:
        print('Two')
    case _:
        print('none')


ch=float(input('enter a num:'))
print(ch)
match (ch):
    case 1.1:
        print('one')
    case 2.2:
        print('Two')
    case _:
        print('none')


ch=input('enter a num: ')
print(ch)
match (ch):
    case 2:
        print('One')
    case 2.0:
        print('Two')
    case _:
        print('none')