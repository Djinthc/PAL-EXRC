def isPalindrome(text):
    text = text.upper()
    text = text.replace(' ','')
    rev = text[::-1]
    
    if text == rev:
        print('This is a Palindrome')
        return True
    else:
        print('This is NOT a Palindrome')
        return False

if isPalindrome('xaax') == True:
    print('OK')
else:
    print('Wrong')

if isPalindrome('xabax') == True:
    print('OK')
else:
    print('Wrong')

if isPalindrome('Ten animals I slam in a net') == True:
    print('OK')
else:
    print('Wrong')

if isPalindrome('More animals I slam in a net') == False:
    print('OK')
else:
    print('Wrong')
