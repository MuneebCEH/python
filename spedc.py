from time import *
import random as r


def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] !=usertest[i]:
               error = error + 1
        except :
            error = error + 1
    return  error
        
def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/ time_R
    return round(speed) 
if __name__== '__main__' :
    while True:
        ck = input(" ready to test : yes / no : ")
        if ck == "yes" :
            test=["if you have gained enough knowledge about the Python programming language and want to get selected in any company at a good salary, this video is for you.",
            "my name is muneeb ur rehman","welcome to sharp tech"]
            test1 = r.choice(test)
            print("            *****typing speed*****")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput=input(" Enter : ")
            time_2 = time()

            print('Speed : ',speed_time(time_1,time_2,testinput),"w/sec")
            print("Error : ",mistake(test1,testinput))
            
        elif ck == 'no':
            print(" Thank You ")
            break

        else:
            print(" wrong input ")