import random
import string
def generatepassword(length):
    l=string.ascii_lowercase
    u=string.ascii_uppercase
    d=string.digits
    p=string.punctuation
    password=[random.choice(l),random.choice(u),random.choice(p),random.choice(p)]
    password+=random.choices(l+u+d+p,k=length-4)
    random.shuffle(password)
    return ''.join(password)
l=int(input("Enter the length to generate password :"))
print("Generated password =",generatepassword(l))
