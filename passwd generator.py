import random
ch="yes"
while ch!="no":
    length=int(input("Enter the length of your Password:"))
    complexity=input("plz enter the complexity of the password you want(weak,medium,strong):")
    msg="""
    1.weak
    2.medium
    3.strong"""
    lowercase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    digit=["0","1","2","3","4","5","6","7","8","9"]
    uppercase=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    special=['!','@','#','$','%','^','&','*','(',')'',','"','/','?','{','}','[',']','|','=','+','.','<','>']
    if complexity=="weak":
            i = 0
            s = ""
            u=""
            while i <= length:
                c = random.choice(lowercase) +  random.choice(uppercase)
                s += str(c)
                i += 1
                d = random.choice(s)
                u += d
            print("The generated password is:",u, end="")


    elif complexity=="medium":
            i = 0
            s = ""
            u=""
            while i < length:
                c = random.choice(lowercase) + random.choice(uppercase) + random.choice(digit)
                s += str(c)
                i += 1
                d=random.choice(s)
                u+=d
            print("The generated password is:", u, end="")
    else:
        i = 0
        s = ""
        u=""
        while i < length:
            c = random.choice(lowercase) +  random.choice(uppercase) +random.choice(digit) + random.choice(special)
            s += str(c)
            i += 1
            d = random.choice(s)
            u += d
        print("The generated password is:", u, end="")
    print('\n')
    ch=input("do you want to regenerate the password again(yes/no):")










