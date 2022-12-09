def isAnagram(text,text2):
    text, text2 = text.upper().replace(' ',''), text2.upper().replace(' ','')
    sum1 = 0
    sum2 = 0
    
    for ch in text:
        sum1 += ord(ch)
    for ch in text2:
        sum2 += ord(ch)

    if sum1 == sum2:
        print('Yes it is')
        return True
    else:
        print('Nope')
        return False

if isAnagram('Listen','Silent') == True:
    print('Test OK!')
else:
    print('Test FAiled!')

if isAnagram('modern','norman') != True:
    print('Test OK!')
else:
    print('Test FAiled!')