'''This program finds to pallindrome in a string by taking each character as a
center of pallindrome. From center it probes in both direction this pallindrome
exists.
A pallindrome might exists in space between two characters e.g, "bb"
'''
def palindrome(string):
    if not string:
        return None
    max_range = ()
    max_length = 0
    for i in range(len(string)):
        current_range = find_pallindrome(i, string)
        new_length = current_range[1] - current_range[0] + 1
        if max_length < new_length :
            max_length = new_length
            max_range = current_range
    return string[max_range[0]:max_range[1] + 1]
        
def find_pallindrome(i, string):
    len_str = len(string)
    len_first = 0
    len_second = 0
    low = i
    high = i
    while (low > -1 and high < len_str and string[low] == string[high]):
        low -= 1
        high += 1
    if low == i and high == i:
        len_first = (low, high)
    else:
        len_first = (low + 1, high - 1)
    low = i
    high = i + 1
    while(low > -1 and high < len_str and string[low] == string[high]):
        low -= 1
        high += 1
    if low == i and high == i + 1:
        len_second = (low, high - 1)
    else:
        len_second = (low + 1, high - 1)
    if len_first[1] - len_first[0] > len_second[1] - len_second[0]:
        return len_first
    else:
        return len_second

print palindrome("")
print palindrome("a")
print palindrome("ab")
print palindrome("bb")
print palindrome("abcba")
print palindrome("efabcba")
