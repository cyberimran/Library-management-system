import random
imran=0
arjun=0
anil=0
total_vote=0
print("WELLCOME TO VOTING SYSTEM CREATED BY IMRAN\n")
while (True):
    vote=input("NOTE: Type exit to know who won.\n\n1.IMRAN\n2.ARJUN\n3.ANIL\n\n")
    if vote=="exit":
        if imran>arjun and imran>anil:
            print(f"IMRAN = {imran} vote\nARJUN = {arjun} vote\nANIL = {anil} vote\nTOTAL = {total_vote} vote\n\nIMRAN IS WINNER")
        elif arjun>imran and arjun>anil:
            print(f"ARJUN = {arjun} vote\nIMRAN = {imran} vote\nANIL = {anil} vote\nTOTAL = {total_vote} vote\n\nARJUN IS WINNER")
        elif anil>imran and anil>arjun:
            print(f"ANIL = {anil} vote\nIMRAN = {imran} vote\nARJUN = {arjun} vote\nTOTAL = {total_vote} vote\n\nANIL IS WINNER")
        elif imran==arjun and imran==anil:
            print(f"IMRAN = {imran} vote\nARJUN = {arjun} vote\nANIL = {anil} vote\nTOTAL = {total_vote} vote\n\nVOTING IS DRAW TOSS AND WIN")
            v1="\nIMRAN PLEASE PICK 1 TO 3 ANY NUMBER: "
            v2="\nARJUN PLEASE PICK 1 TO 3 ANY NUMBER: "
            v3="\nANIL PLEASE PICK 1 TO 3 ANY NUMBER: "
            picker1=[v1,v2,v3]
            rand1=random.choice(picker1)
            picker1_input=input(rand1)
            ran1=random.randint(1,3)
            if rand1==v1:
                picker2=[v2,v3]
                rand2=random.choice(picker2)
                picker2_input=int(input(rand2))
                if picker1_input==ran1:
                    print("\n\nIMRAN IS WINNER")
                elif rand2==v2:
                    if picker2_input==ran1:
                        print("\n\nARJUN IS WINNER")
                    else:
                        print("\n\nANIL IS WINNER")
                elif rand2==v3:
                    if picker2_input==ran1:
                        print("\n\nANIL IS WINNER")
                    else:
                        print("\n\nARJUN IS WINNER")
            elif rand1==v2:
                 picker3=[v1,v3]
                 rand3=random.choice(picker3)
                 picker3_input=int(input(rand3))
                 if picker3_input==ran1:
                     print("\n\nARJUN IS WINNER")
                 elif rand3==v1:
                     if picker3_input==ran1:
                         print("\n\nIMRAN IS WINNER")
                     else:
                         print("\n\nANIL IS WINNER")
                 elif rand3==v3:
                     if picker3_input==ran1:
                         print("\n\nANIL IS WINNER")
                     else:
                         print("\n\nIMRAN IS WINNER")
            elif rand1==v3:
                picker4=[v1,v2]
                rand4=random.choice(picker4)
                picker4_input=int(input(rand4))
                if picker1_input==ran1:
                    print("\n\nANIL IS WINNER")
                elif rand4==v1:
                    if picker4_input==ran1:
                        print("\n\nIMRAN IS WINNER")
                    else:
                        print("\n\nARJUN IS WINNER")
                elif rand4==v2:
                    if picker4_input==ran1:
                        print("\n\nARJUN IS WINNER")
                    else:
                        print("\n\nIMRAN IS WINNER")

        elif imran==arjun:
            print(f"IMRAN = {imran} vote\nARJUN = {arjun} vote\nANIL = {anil} vote\nTOTAL = {total_vote} vote\n\nVOTING IS DRAW TOSS AND WIN")
            v1="IMRAN PLEASE CHOOSE ONE ANY NUMNER IN [1,2] : "
            v2="ARJUN PLEASE CHOOSE ONE ANY NUMNER IN [1,2] : "
            picker=[v1,v2]
            rand=random.choice(picker)
            picker_i=int(input(rand))
            ran=random.randint(1,2)
            if rand==v1:
                if picker_i==ran:
                    print("\n\nIMRAN IS WINNER")
                else:
                    print("\n\nARJUN IS WINNER")
            elif rand==v2:
                if picker_i==ran:
                    print("\n\nARJUN IS WINNER")
                else:
                    print("\n\nIMRAN IS WINNER")
        elif imran==anil:
            print(f"IMRAN = {imran} vote\nARJUN = {arjun} vote\nANIL = {anil} vote\nTOTAL = {total_vote} vote\n\nVOTING IS DRAW TOSS AND WIN")
            v1="IMRAN PLEASE CHOOSE ONE ANY NUMNER IN [1,2] : "
            v2="ANIL PLEASE CHOOSE ONE ANY NUMNER IN [1,2] : "
            picker=[v1,v2]
            rand=random.choice(picker)
            picker_i=int(input(rand))
            ran=random.randint(1,2)
            if rand==v1:
                if picker_i==ran:
                    print("\n\nIMRAN IS WINNER")
                else:
                    print("\n\nANIL IS WINNER")
            elif rand==v2:
                if picker_i==ran:
                    print("\n\nANIL IS WINNER")
                else:
                    print("\n\nIMRAN IS WINNER")
        elif arjun==anil:
            print(f"IMRAN = {imran} vote\nARJUN = {arjun} vote\nANIL = {anil} vote\nTOTAL = {total_vote} vote\n\nVOTING IS DRAW TOSS AND WIN")
            v1="ARJUN PLEASE CHOOSE ONE ANY NUMNER IN [1,2] : "
            v2="ANIL PLEASE CHOOSE ONE ANY NUMNER IN [1,2] : "
            picker=[v1,v2]
            rand=random.choice(picker)
            picker_i=int(input(rand))
            ran=random.randint(1,2)
            if rand==v1:
                if picker_i==ran:
                    print("\n\nARJUN IS WINNER")
                else:
                    print("\n\nANIL IS WINNER")
            elif rand==v2:
                if picker_i==ran:
                    print("\n\nANIL IS WINNER")
                else:
                    print("\n\nARJUN IS WINNER")
                
        
                               
        break
    else:
     
        if vote=="1":
            imran+=1
            total_vote+=1
        elif vote=="2":
            arjun+=1
            total_vote+=1
        elif vote=="3":
            anil+=1
            total_vote+=1   
        else:
            print("WRONG INPUT")