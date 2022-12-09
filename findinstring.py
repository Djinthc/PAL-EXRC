def findInString(word,string):
    '''are the characters comprising the first string hidden inside the second string?
    input: 2 Strings    output: bool
    '''
    positions = [0]
    alfa = 0
    for ch in word:
        positions.append(string.find(ch,positions[alfa]))
        alfa += 1
        
        


    if any(positions) == -1:
        return False
    else:
        if sorted(positions) != positions:
            return False
        else:
            return True

if findInString('donor','Nabucodonosor') == True:
    print('Test 1 - OK')
else:
    print('Test 1 - FAILED')

if findInString('donut','Nabucodonosor') == False:
    print('Test 1 - OK')
else:
    print('Test 1 - FAILED')
