num = input('Enter card number: ')

if len(num) == 15:
    if num.startswith('34') or num.startswith('37'):
        print('AMEX')
elif len(num) == 16:
    if num.startswith('6011'):
        print('Discover')
elif len(num) == 16:
    if num.startswith('51') or num.startswith('52') or (
        num.startswith('53') or num.startswith('52')):
        print('Mastercard')
elif len(num) == 16 or len(num) == 13:
    if num.startswith('4'):
        print('VISA')      
else:
    print('Unknown')

