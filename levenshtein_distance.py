
'''Levenshtian distance using dynamic programming
'''

def get_levenshtian_distance(string1, string2):
    if not string1:
        return len(string2)
    if not string2:
        return len(string1)
        
    len_string1 = len(string1)
    len_string2 = len(string2)
    matrix = []
    for i in range(len_string1 + 1):
        temp = [0] * (len_string2 + 1)
        matrix.append(temp)
    
    for i in range(len_string1 + 1):
        matrix[i][0] = i
    for j in range(len_string2 + 1):
        matrix[0][j] = j
    for i in range(1, len_string1 + 1):
        for j in range(1, len_string2 + 1):
            if string1[i - 1] == string2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] 
            else:
                matrix[i][j] = min([matrix[i - 1][j - 1] + 1,
                                    matrix[i ][j - 1] + 1,
                                    matrix[i - 1][j] + 1 ])
    
    # for row in matrix:
    #    print row
    # return matrix[len_string1][len_string2]

print get_levenshtian_distance("sunday", "saturday")
