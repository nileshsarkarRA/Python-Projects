# Python Code to check for the criteria of pallindrom ie reversible text by Nilesh

def isPalindrome(str):

    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

# main function
s = input("Enter a text to run the test: ")
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")
