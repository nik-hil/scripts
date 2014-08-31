'''This program finds to pallindrome in a string by taking each character as a
center of pallindrome. From center it probes in both direction this pallindrome
exists.
A pallindrome might exists in space between two characters e.g, "bb"
'''

def pallindrome(string):
    print ">>>>>>>> string: " + string
    for i in range(len(string)):
        max_range = find_pallindrome(i, string)
        print "max_range: "+ str(max_range)
        if max_range[1] == max_range[0]:
            print "pallindrome: " + string[max_range[0]]   
        else:
            print "pallindrome: " + string[max_range[0]:max_range[1]+1]

def find_pallindrome(i, string):
    j = 0
    low = i-j
    high = i+j
    flag1 = False # if while loop has not started. pallindrome is that char
    flag2 = False
    try :
        while string[low] == string[high]:
            flag1 = True
            j += 1
            low = i-j
            high = i+j
            if low < 0: # -ve index points towards end.
                break
            
    except Exception, e:
        print "first: ", str(e)
    finally:
        j -=1
        if flag1:
            pal_len1 = i+j -(i-j) + 1
            pal_range1 = (i-j, i+j)
        else:
            pal_len1 = 0
            pal_range1 = (i,i)

    try :
        j = 0
        low = i-j
        high = i+j +1
        while string[low] == string[high]:
            flag2 = True
            j += 1
            low = i-j
            high = i+j +1
            if low < 0:
                break
    except Exception, e:
        print "Second: ", str(e)
        
    finally:
        j -=1
        if flag2:
            pal_len2 = i+1+j -(i-j) + 1
            pal_range2 = (i-j, i+1+j)
        else:
            pal_len2 = 0
            pal_range2 = (i,i)


    if pal_len1 > pal_len2:
        return pal_range1
    else:
        return pal_range2


pallindrome("a")
pallindrome("ab")
pallindrome("bb")
pallindrome("abcba")
pallindrome("efabcba")
