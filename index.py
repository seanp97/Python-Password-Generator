import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"  "k", "l", "m", "n",
"o", "p", "q",  "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabetLen = len(alphabet)

myNewPass = []
finishedPass = ""
passLen = input("How long do you want your password to be? \n")

for i in range(int(passLen)):
    randPass = random.randrange(alphabetLen)
    myNewPass = alphabet[randPass]
    finishedPass += str(myNewPass)

newPass = finishedPass
print("Your generated password is",newPass)