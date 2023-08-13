print("----------------------welcome to the Quiz Game!!!!!!----------------------")
rules="""RULES!!!
1.Questions will be asked on the basis of your domain\n2.There are 5 questions in a domain\n3.Each question carries 10 points\n4.There is no negative points"""
print(rules)
print("*******************************************************************")
msg="""The domains are:   
* python\n* c\n* java"""
print(msg)
print("********************************************************************")
ch="yes"
while ch=="yes":
    domain=input("plz select the domain you want to take test:")
    if domain=="python":
        print("welcome to python programming quiz")
        print("********************************************************************")
        q1="""1.who developed python programming language? \n1)wick van Rossum\n2)Rasmus Lerdorf\n3)Guido van Rossum\n4)niene stom"""
        print(q1)
        ans=input("the answer is:")
        print("*************************************")
        if ans == "Guido van Rossum":
            p1=10
            print("you got a 10 points")
        else:
            p1=0
            print("oops!!!Try gain")
        print("*************************************")
        q2="""2.Is python case sensitive?\n1)yes\n2)No\n3)Machine dependent\n4)none of the mentioned"""
        print(q2)
        ans = input("the answer is:")
        print("*************************************")
        if ans == "yes":
            p2=10
            print("you got a 10 points")
        else:
            p2=0
            print("oops!!!Try gain")
        print("*************************************")
        q3 = """3.which of the following is the correct extension of python?\n1).python\n2).pi\n3).py\n4).p"""
        print(q3)
        ans = input("the answer is:")
        print("*************************************")
        if ans == ".py":
            p3=10
            print("you got a 10 points")
        else:
            p3=0
            print("oops!!!Try gain")
        print("*************************************")
        q4 = """4.what will be the value of the following expression(4+2%5)?\n1)7\n2)2\n3)4\n4)1"""
        print(q4)
        ans = input("the answer is:")
        print("*************************************")
        if ans == "4":
            p4=10
            print("you got a 10 points")
        else:
            p4=0
            print("oops!!!Try gain")
        print("*************************************")
        q5 = """5.which keyword is used for function in python language?\n1)Function\n2)def\n3)Fun\n4)Define"""
        print(q5)
        ans = input("the answer is:")
        print("*************************************")
        if ans == "def":
            p5=10
            print("you got a 10 points")
        else:
            p5=0
            print("oops!!!Try gain")
        print("*************************************")
        total=p1+p2+p3+p4+p5
    elif domain=="c":
        print("welcome to c programming quiz ")
        print("********************************************************************")
        c1 = """1.who developed c programming language?\n1)Steve jobs\n2)James Gosling \n3)Dennis Ritche\n4)Rasmus Lerdorf"""
        print(c1)
        ans = input("the answer is:")
        print("*************************************")
        if ans == "Dennis Ritche":
            c1=10
            print("you got a 10 points")
        else:
            c1=0
            print("oops!!!Try gain")
        print("*************************************")
        c2 = """2.All keywords in C are in? \n1)lowercase letter\n2)Uppercase letter\n3)Camelcase letter\n4)none of the mentioned"""
        print(c2)
        ans = input("the answer is:")
        print("*************************************")
        if ans == "lowercase letter":
            c2=10
            print("you got a 10 points")
        else:
            c2=0
            print("oops!!!Try gain")
        print("*************************************")
        c3 = """3.which is valid c expression?\n1)int my_num=100,0000;\n2)int my_num=1000000;\n3)int my num=1000;\n4)int $my_num=100000;"""
        print(c3)
        ans = input("the answer is:")
        print("*************************************")
        if ans == "int my_num=1000000;":
            c3=10
            print("you got a 10 points")
        else:
            c3=0
            print("oops!!!Try gain")
        print("*************************************")
        c4 = """4.what is an example of iteration in c?\n1)for\n2)while \n3)do-while\n4)all the mentioned above"""
        print(c4)
        ans = input("the answer is:")
        print("*************************************")
        if ans == "all the mentioned above":
            c4=10
            print("you got a 10 points")
        else:
            c4=0
            print("oops!!!Try gain")
        print("*************************************")
        c5 = """5.The c-preprocessor are specified with ________symbol?\n1)#\n2)$\n3)""\n4)&"""
        print(c5)
        ans = input("the answer is:")
        print("*************************************")
        if ans == "#":
            c5=10
            print("you got a 10 points")
        else:
            c5=0
            print("oops!!!Try gain")
        print("*************************************")
        total = c1 + c2 + c3 + c4 + c5
    elif domain=="java":
        print("welcome to java programming quiz")
        print("********************************************************************")
        j1 = """1.who developed java programming language? \n1)Steve jobs\n2)James Gosling \n3)Dennis Ritche\n4)Rasmus Lerdorf"""
        print(j1)
        ans = input("the answer is:")
        print("*************************************")
        if ans == "James Gosling ":
            j1=10
            print("you got a 10 points")
        else:
            j1=0
            print("oops!!!Try gain")
        print("*************************************")
        j2 = """2.Number of primitive datatypes in java are? \n1)6\n2)7 \n3)8\n4)9"""
        print(j2)
        ans = input("the answer is:")
        print("*************************************")
        if ans == "8":
            j2=10
            print("you got a 10 points")
        else:
            j2=0
            print("oops!!!Try gain")
        print("*************************************")
        j3 = """2.What is the size of float and double in java? \n1)32 and 64\n2)32 and 32\n3)64 and 64\n4)64 and 32"""
        print(j3)
        ans = input("the answer is:")
        print("*************************************")
        if ans == "32 and 64":
            j3=10
            print("you got a 10 points")
        else:
            j3=0
            print("oops!!!Try gain")
        print("*************************************")
        j4 = """4.Arrays in java are?\n1)Object references\n2)Objects\n3)Primitive datatype\n4)none"""
        print(j4)
        ans = input("the answer is:")
        print("*************************************")
        if ans == "objects":
            j4=10
            print("you got a 10 points")
        else:
            j4=0
            print("oops!!!Try gain")
        print("*************************************")
        j5 = """5.compareTo() returns? \n1)True\n2)False\n3)An int value\n4)none"""
        print(j5)
        ans = input("the answer is:")
        print("*************************************")
        if ans == "An int value":
            j5=10
            print("you got a 10 points")
        else:
            j5=0
            print("oops!!!Try gain")
        print("*************************************")
        total =j1 + j2 + j3 + j4 + j5
    else:
        print("plz enter the correct domain")
    if total >= 40:
        print("""congratulations!!!!!!
                    you have scored:""", total, "points")
    elif total >= 20:
        print("""Try to get good marks...
                    you have scored:""", total, "points")
    else:
        print("""oops!!!
                better luck next time""")
    print("********************************************************************")
    ch=input("do you want to play again??(yes/no):")



