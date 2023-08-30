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
    digit=[0,1,2,3,4,5,6,7,8,9]
    uppercase=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    special=['!','@','#','$','%','^','&','*','(',')'',','"','/','?','{','}','[',']','|','=','+','.','<','>']
    if complexity=="weak":
        i = 0
        s = ""
        while i < length:
            c = random.choice(lowercase +  uppercase)
            s += str(c)
            i += 1
        print("The generated password is:", s, end="")
    elif complexity=="medium":
        i = 0
        s = ""
        while i < length:
            c = random.choice(lowercase + uppercase+digit)
            s += str(c)
            i += 1
        print("The generated password is:", s, end="")
    else:
        i = 0
        s = ""
        while i < length:
            c = random.choice(lowercase + uppercase+digit+special)
            s += str(c)
            i += 1
        print("The generated password is:", s, end="")
    print('\n')
    ch=input("do you want to regenerate the password again(yes/no):")











