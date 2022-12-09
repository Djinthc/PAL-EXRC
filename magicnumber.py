def digitOfLife(number):
    '''input:number =  date of life YYYYMMDD as number
        output: single number as a sum of all the numbers in date'''

    number = str(number)
    while len(number)>1:
        number2 = 0
        for ch in number:
            number2 += int(ch)
        number = str(number2)
    return int(number)


if digitOfLife(19991229) == 6:
    print ('test - OK')
else:
    print ('test - FAILED')

if digitOfLife(20000101) == 4:
    print ('test - OK')
else:
    print ('test - FAILED')