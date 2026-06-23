def firstpalindrome(words) :
    for word in words :
        if word == word[::-1] :
            return word
    return ""
#test case
print(firstpalindrome(["abc","car","ada","racecar","cool"]))
print(firstpalindrome(["notapalindrome","racecar"]))