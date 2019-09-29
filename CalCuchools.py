# Programmed By DL-TTy
# via Python 3.4.4

def main():
      welcome()
      
def welcome():
      q = input("""Hello, I`m CalCuchools.
A Calculator For Formuls And Hard Activitys.
>>>>>My Programmer Is A.M. Ispare<<<<<
I`m Always Have Update That`s Can Help You.
Press ENTER Key For Start Our Work.""")
      work_find()
      
def work_find():
      print("""Good. Now, Please Insert Number Of Your Work:
Diameters: 1
Addition: 2
Subtraction: 3
Multiplication: 4
Division: 5(Coming Soon ...)
power: 6(Coming Soon ...)
Average: 7
""")
      activity = input("Witch One ??  _")
      if (int(activity) == int("1")):
            dia_frml()
      elif (int(activity) == int("2")):
            add_frml()
      elif (int(activity) == int("3")):
            sub_frml()
      elif (int(activity) == int("4")):
            mul_frml()
      elif (int(activity) == int("5")):
            div_frml()
      elif (int(activity) == int("6")):
            power_select_mode()
      elif (int(activity) == int("7")):
            avg_frml()
      else:
            errorMessage_1 = input("You Inserted A Invalid Number. Do You Want To Try Again?[y/n]")
            if (errorMessage_1 == "y"):
                  work_find()
            elif (errorMessage_1 == "Y"):
                  work_find()
            else:
                  exit()

def dia_frml():
      four = '4'
      three = '3'
      two = '2'#Number`s Name
      sides_str = input('Now, Insert Sides And Get Diameters: ')#Get Sides From User
      opr_1_dia = int(sides_str)
      opr_2_dia = int(sides_str) - int(three)
      opr_3_dia = int(opr_1_dia) * opr_2_dia
      opr_4_dia = int(two)
      awn_dia = opr_3_dia // opr_4_dia#Activitys
      diameters = awn_dia#Awnser
      if (int(sides_str) < int(four)):#Verifying Input
            errorMessage = input("""Erorr: Your Shape Has Not Any diameters.
If You Want To Try Other Numbers, Write RESET  And Press ENTER Key.
Or Press Enter For Exit.""")
            if (errorMessage == 'RESET'):#Reseting
                  dia_frml()
            if (errorMessage == 'Reset'):#Reseting
                  dia_frml()
            if (errorMessage == 'reset'):#Reseting
                  dia_frml()      
            else:
                  exit()
      else:#OutPut
            print("You Inserted ",int(sides_str),""", That Is A Valid Number For Claculate The Diameters.
We Calculated That The Number Of Diameters In A """,int(sides_str),"""
Sided Shape Is """,diameters,"Diameters.")#printing OutPut
            end_workMessage = input("You Want To Do It Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()

def add_frml():
      opr_1_add = int(input("Ok, Insert Your First Number"))
      opr_2_add = int(input("Ok, Insert Your Secend Number"))
      message = input("Do You Want Use Third Number?[y/n]")
      if (message == 'y'):
            opr_3_add = int(input("Ok, Insert Your Secend Number"))
            opr_4_add = opr_1_add + opr_2_add
            awn_add = opr_4_add + opr_3_add
            addition = awn_add
            print("Ok, We Add ",opr_1_add," To ",opr_2_add," And ",opr_3_add,""" And Get A Number.
That`s Is Your Awnser. """,addition)
            end_workMessage = input("You Want To Do It Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()
      else:
            awn_add = opr_1_add + opr_2_add
            addition = awn_add
            print("Ok, We Add ",opr_1_add," To ",opr_2_add,""" And Get A Number.
That`s Is Your Awnser. """,addition)
            end_workMessage = input("You Want To Do It Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()

def avg_frml():
      opr_1_avg = int(input("Now, Insert Your 1th Number. "))
      opr_2_avg = int(input("Now, Insert Your 2nd Number. "))
      message_1 = input("Do You Want Use An Other Number?[y/n]")
      if (message_1 == "y"):
            opr_3_avg = int(input("Now, Insert Your 3rd Number. "))
            message_2 = input("Do You Want Use An Other Number?[y/n]")
            if (message_2 == 'y'):
                  opr_4_avg = int(input("Now, Insert Your 4th Number. "))
                  message_3 = input("Do You Want Use An Other Number?[y/n]")
                  if (message_3 == 'y'):
                        opr_5_avg = int(input("Now, Insert Your 5th Number. "))
                        opr_4_1_avg = opr_1_avg + opr_2_avg
                        opr_4_2_avg = opr_4_1_avg + opr_3_avg
                        opr_4_3_avg = opr_4_2_avg + opr_4_avg
                        opr_4_4_avg = opr_4_3_avg + opr_5_avg 
                        awn_avg = opr_4_4_avg / 5
                        average = awn_avg
                        print("We Calculate Average Of ",opr_1_avg," And " ,opr_2_avg," , ",opr_3_avg," , ",opr_4_avg," , ",opr_5_avg ,""" Then From That Get A Number,
""",average)
                        end_workMessage = input("You Want To Do It Again?[y/n]")#Try Again Message
                        if (end_workMessage == "y"):#Select Try Again
                              work_find()
                        elif (end_workMessage == "n"):#Select Exit
                              input("Good Luck! _")
                              exit()
                        else:#Exit
                              input("Good Luck! _")
                              exit()
                  else:
                        opr_3_1_avg = opr_1_avg + opr_2_avg
                        opr_3_2_avg = opr_3_1_avg + opr_3_avg
                        opr_3_3_avg = opr_3_2_avg + opr_4_avg
                        awn_avg = opr_3_3_avg / 4
                        average = awn_avg
                        print("We Calculate Average Of ",opr_1_avg," And " ,opr_2_avg," , ",opr_3_avg," , ",opr_4_avg,""" Then From That Get A Number,
""",average)
                        end_workMessage = input("You Want To Do It Again?[y/n]")#Try Again Message
                        if (end_workMessage == "y"):#Select Try Again
                              work_find()
                        elif (end_workMessage == "n"):#Select Exit
                              input("Good Luck! _")
                              exit()
                        else:#Exit
                              input("Good Luck! _")
                              exit()
            else:
                  opr_2_1_avg = opr_1_avg + opr_2_avg
                  opr_2_2_avg = opr_2_1_avg + opr_3_avg
                  awn_avg = opr_2_2_avg / 3
                  average = awn_avg
                  print("We Calculate Average Of ",opr_1_avg," And " ,opr_2_avg," , ",opr_3_avg,""" Then From That Get A Number,
""",average)
            end_workMessage = input("You Want To Do It Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()
      else:
            opr_1_1_avg = opr_1_avg + opr_2_avg
            opr_1_2_avg = opr_1_1_avg / 2
            awn_avg = opr_1_2_avg
            average = awn_avg
            print("We Calculate Average Of ",opr_1_avg," And " ,opr_2_avg, """ Then From That Get A Number,
""",average)
            end_workMessage = input("You Want To Do It Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()
def sub_frml():
      opr_1_sub = int(input("Ok. Now, Insert First Number. _"))
      opr_2_sub = int(input("Now, Insert Secend Number. _"))
      message_sub = input("Do You Want To Ao Add A Third Number? _[y/n]")
      if (message_sub == 'y'):
            opr_3_sub = int(input("""OK, Insert Third Number.
(First - Secend - Third = Awnser) _"""))
            message_sub_2 = input("Do You Want To Ao Add A Third Number? _[y/n]")
            if (message_sub == 'y'):
                   opr_4_sub = int(input("""OK, Insert Fourth Number.
(First - Secend - Third - Fourth= Awnser) _"""))
                   opr_5_1_sub = opr_1_sub - opr_2_sub
                   opr_5_2_sub = opr_5_1_sub - opr_3_sub
                   awn_sub = opr_5_2_sub - opr_4_sub
                   subtraction = awn_sub
                   print("""Ummm, This Work So Eazy! I Do It.
""",subtraction," Is Your Awnser.")
                   end_workMessage = input("You Want To Do It Again?[y/n]")#Try Again Message
                   if (end_workMessage == "y"):#Select Try Again
                         work_find()
                   elif (end_workMessage == "n"):#Select Exit
                         input("Good Luck! _")
                         exit()
                   else:#Exit
                         input("Good Luck! _")
                         exit()
            else:
                   opr_5_1_sub = opr_1_sub - opr_2_sub
                   awn_sub = opr_5_1_sub - opr_3_sub
                   Subtraction = awn_sub
                   print("""Ummm, This Work So Eazy! I Do It.
""",subtraction," Is Your Awnser.")
                   end_workMessage = input("You Want To Do It Again?[y/n]")#Try Again Message
                   if (end_workMessage == "y"):#Select Try Again
                         work_find()
                   elif (end_workMessage == "n"):#Select Exit
                         input("Good Luck! _")
                         exit()
                   else:#Exit
                         input("Good Luck! _")
                         exit()
      else:
            opr_5_1_sub = opr_1_sub - opr_2_sub
            Subtraction = awn_sub
            print("""Ummm, This Work So Eazy! I Do It.
""",subtraction," Is Your Awnser.")
            end_workMessage = input("You Want To Do It Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()
def mul_frml():
      opr_1_mul = int(input("Right. Now, Insert 1th Numbet"))
      opr_2_mul = int(input("Right. Now, Insert 2nd Numbet"))
      message_mul = input("Do You Want Use An Other Number?[y/n]")
      if (message_mul == 'y'):
            opr_3_mul = int(input("Right. Now, Insert 3rd Numbet"))
            message_mul = input("Do You Want Use An Other Number?[y/n]")
            if (message_mul == 'y'):
                  opr_4_mul = int(input("Right. Now, Insert 4th Numbet"))
                  message_mul = input("Do You Want Use An Other Number?[y/n]")
                  if (message_mul == 'y'):
                        opr_5_mul = int(input("Right. Now, Insert 5th Numbet"))
                        opr_1_1_mul = opr_1_mul * opr_2_mul
                        opr_1_2_mul = opr_1_1_mul * opr_3_mul
                        opr_1_3_mul = opr_1_2_mul * opr_4_mul
                        awn_mul = opr_1_3_mul * opr_5_mul
                        multiplication = awn_mul
                        print("""We Do It :)
Your Awnser Is """,multiplication)
                        end_workMessage = input("You Want To Do It Again?[y/n]")#Try Again Message
                        if (end_workMessage == "y"):#Select Try Again
                              work_find()
                        elif (end_workMessage == "n"):#Select Exit
                              input("Good Luck! _")
                              exit()
                        else:#Exit
                              input("Good Luck! _")
                              exit()
                  else:
                        opr_5_mul = int(input("Right. Now, Insert 5th Numbet"))
                        opr_1_1_mul = opr_1_mul * opr_2_mul
                        opr_1_2_mul = opr_1_1_mul * opr_3_mul
                        awn_mul = opr_1_2_mul * opr_4_mul
                        multiplication = awn_mul
                        print("""We Do It :)
Your Awnser Is """,multiplication)
                        end_workMessage = input("You Want To Do It Again?[y/n]")#Try Again Message
                        if (end_workMessage == "y"):#Select Try Again
                              work_find()
                        elif (end_workMessage == "n"):#Select Exit
                              input("Good Luck! _")
                              exit()
                        else:#Exit
                              input("Good Luck! _")
                              exit()
            else:
                  opr_1_1_mul = opr_1_mul * opr_2_mul
                  awn_mul = opr_1_1_mul * opr_3_mul
                  multiplication = awn_mul
                  print("""We Do It :)
Your Awnser Is """,multiplication)
                  end_workMessage = input("You Want To Do It Again?[y/n]")#Try Again Message
                  if (end_workMessage == "y"):#Select Try Again
                        work_find()
                  elif (end_workMessage == "n"):#Select Exit
                        input("Good Luck! _")
                        exit()
                  else:#Exit
                        input("Good Luck! _")
                        exit()
      else:
            awn_mul = opr_1_mul * opr_2_mul
            multiplication = awn_mul
            print("""We Do It :)
Your Awnser Is """,multiplication)
            end_workMessage = input("You Want To Do It Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()





                  
main()



#Programmed By DL-TTy
