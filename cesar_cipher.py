def cesar(text, number):
        result = ''
        for ch in text:
            o = ord(ch)
            if ch == ' ':
                result += ch

            elif ch.isnumeric() == True:
                result += ch
            
            elif o >= 65 and o <= 90:
                x = number
                while x > 0:
                    o +=1
                    x -=1
                    if o == 91:
                        o = 65
                result += chr(o)
            
            elif o >= 97 and o <= 122:
                x = number
                while x > 0:
                    o +=1
                    x -=1
                    if o == 123:
                        o = 97
                result += chr(o)
            else:
                continue
        return result


print(cesar('The die is cast', 25))

