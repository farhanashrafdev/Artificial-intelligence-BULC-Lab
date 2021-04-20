MatricMarks= input("Enter your marks in Matric: ")
FSCMarks= input("Enter your marks in FSC: ")
Major=input("Have you studied Physics as major in college")
CSback=input("Have Any CS Background?")


def main():
     counter = 0

     if int(MatricMarks) > 50:
        counter = counter+1
     if int(FSCMarks) >50:
         counter = counter+1
     if Major== 'y' or int(Major) == 1:
         counter = counter+1
     if CSback== 'y' or int(CSback)==1:
        counter = counter+1
     if counter==4:
       print("You will get admission")
     else:
        print("You will not get admission")
main()