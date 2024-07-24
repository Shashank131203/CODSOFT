import string
import random

if __name__ == "__main__":
    s1= string.ascii_lowercase
    s2= string.ascii_uppercase
    s3= string.digits
    s4= string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))



    print("Welcome to Password Generator")
    plen = int(input("Enter password length\n"))
    plen_letters = int(input("How many letters you want in passowrd?\n"))
    plen_symbols = int(input("How many symbols you want in password?\n"))
    plen_numbers = int(input("How many numbers you want in password?\n"))

    pssd = ""

    if plen != (plen_letters+plen_numbers+plen_symbols):
            print("The total number of characters doesn't match the required password length.Try again\n")
    else:
        for i in range(0,plen_letters):
            char = random.choice(s)
            pssd = pssd+char

        for i in range(0,plen_numbers):
            char = random.choice(s3)
            pssd = pssd+char
        
        for i in range(0,plen_symbols):
            char = random.choice(s4)
            pssd = pssd+char

        pssd = list(pssd) 
        random.shuffle(pssd)
        print(pssd)
        password = ""
        for i in pssd:
            password += i
        
        print(password)
             