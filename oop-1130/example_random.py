import random
import math

def strinnng():
    import random
    str_num = ""
    for i in range(4):
        num = random.randrange(97,123)  # 随机小写字母ASCII值
        str_s = chr(num)
        str_num = str_num+str_s
    for i in range(8):
        num = random.randrange(0,10)
        str_num = str_num + str(num)
    return str_num  # 省略此行会默认retur NONE

num = input("Please input a 3-digit number:")
if num.isdigit() and 100 <= int(num) <= 999:
    bet = random.randrange(100,1000)
    bai = bet // 100
    shi = bet % 100 // 10
    ge = bet % 10
    print(str(bet) + " <---> " + num)
    if int(num) > bet:
        print("You are GREATER!")
        print("The lucky number is {0}-{1}-{2}".format(bai, shi, ge))

    elif int(num) < bet:
        print("Sorry you lose :( ")
        for i in range(10):  # 重复执行十次
            str_line = strinnng()
            #print(str_line)
            with open("random_str.txt","a") as fd:
                fd.write(str_line + '\n')
    elif int(num) == bet:
        print("THIS IS AMAZING")
        print("OMG JACKPOT!!!")

else:
    print("Number ONLY")


