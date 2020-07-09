
# Importing 'string' module
import string

# Importing 'random' module
import random

#  main Function
if __name__ == "__main__":

    # Store 'string constants'
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    # input the Length of password user wanted
    length = int(input("Enter the Password length  :  "))

    # Creating List for password
    s = []

    # Adding all string constant
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    #random shuffling of the string
    random.shuffle(s)
    
    #Printing string of desire length
    print("".join(s[0:length]))
