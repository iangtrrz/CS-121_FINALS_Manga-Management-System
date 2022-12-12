import utils.dt as dt
import utils.Mangalist as Mangalist

class Borrow:

    def borrowManga():
        success=False
        while(True):
            firstName=input("Enter the First Name of the Borrower: ")
            if firstName.isalpha():
                break
            print("Please input alphabet from A-Z")
        while(True):
            lastName=input("Enter the Last Name of the Borrower: ")
            if lastName.isalpha():
                break
            print("Please input alphabet from A-Z")
            
        t="Borrow-"+firstName+".txt"
        with open(t,"w+") as f:
            f.write("               Manga Management System  \n")
            f.write("                   Borrowed By: "+ firstName+" "+lastName+"\n")
            f.write("    Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
            f.write("S.N. \t\t Manganame \t      Authorname \n" )
    
        while success==False:
            print("Please select a option below:")
            for i in range(len(Mangalist.manganame)):
                print("Enter", i, "to borrow manga", Mangalist.manganame[i])
    
            try:   
                a=int(input())
                try:
                    if(int(Mangalist.quantity[a])>0):
                        print("Manga is available")
                        with open(t,"a") as f:
                            f.write("1. \t\t"+ Mangalist.manganame[a]+"\t\t  "+Mangalist.authorname[a]+"\n")

                        Mangalist.quantity[a]=int(Mangalist.quantity[a])-1
                        with open("Stock.txt","w+") as f:
                            for i in range(13):
                                f.write(Mangalist.manganame[i]+","+Mangalist.authorname[i]+","+str(Mangalist.quantity[i])+","+"$"+Mangalist.cost[i]+"\n")


                        #multiple book borrowing code
                        loop=True
                        count=1
                        while loop==True:
                            choice=str(input("Do you want to borrow more mangas? However you cannot borrow same manga twice. Press Y for yes and N for no."))
                            if(choice.upper()=="Y"):
                                count=count+1
                                print("Please select an option below:")
                                for i in range(len(Mangalist.manganame)):
                                    print("Enter", i, "to borrow book", Mangalist.manganame[i])
                                a=int(input())
                                if(int(Mangalist.quantity[a])>0):
                                    print("Book is available")
                                    with open(t,"a") as f:
                                        f.write(str(count) +". \t\t"+ Mangalist.manganame[a]+"\t\t  "+Mangalist.authorname[a]+"\n")

                                    Mangalist.quantity[a]=int(Mangalist.quantity[a])-1
                                    with open("Stock.txt","w+") as f:
                                        for i in range(13):
                                            f.write(Mangalist.manganame[i]+","+Mangalist.authorname[i]+","+str(Mangalist.quantity[i])+","+"$"+Mangalist.cost[i]+"\n")
                                        success=False
                                else:
                                    loop=False
                                    break
                            elif (choice.upper()=="N"):
                                print ("Thank you for borrowing manga from us. ")
                                print("")
                                loop=False
                                success=True
                            else:
                                print("Please choose as instructed")
                        
                    else:
                        print("Manga is not available")
                        Borrow()
                        success=False
                except IndexError:
                    print("")
                    print("Please choose Manga acording to their number.")
            except ValueError:
                print("")
                print("Please choose as suggested.")
