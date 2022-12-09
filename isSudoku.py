def isSudoku(matrix):
    '''reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.'''
    numbers = '123456789'
    
    for row in matrix:
        positions = []
        row = str(row)
        for number in str(row):
            positions.append(numbers.find(number))
        
        if sum(positions) != 36:
            return False
        elif(len(set(positions)) != len(positions)):
            return False

        for row in range(len(matrix)):
            vpositions = []
            for column in range(len(matrix)):
                matrix = str(matrix)
                number = matrix[column+1][row]
                vpositions.append(numbers.find(number))

            if sum(vpositions) != 36:
                return False
            elif(len(set(vpositions)) != len(vpositions)):
                return False
            else:
                return True


if isSudoku([295743861,431865927,876192543,387459216,612387495,549216738,763524189,928671354,154938672]) == True:
    print('Test1 - OK!')
else:
    print('Test1 - FAILED!')

if isSudoku([395743862,431865927,876192543,387459216,612387495,549216738,763524189,928671354,254938671]) == False:
    print('Test2 - OK!')
else:
    print('Test2 - FAILED!')






      

