import utils.Mangalist as Mangalist
import utils.dt as dt

error_count = 0
def returnManga():
    global error_count

    name = input("Enter name of Borrower: ")
    a = "Borrow-" + name + ".txt"
    try:
        with open(a, "r") as f:
            lines = f.readlines()
            lines = [a.strip("$") for a in lines]

        with open(a, "r") as f:
            data = f.read()
            print(data)
    except:
        error_count += 1
        if error_count == 3:
            print("Error occured atleast 3 times, the program will now end")
            return

        print("The Borrower name is incorrect")
        returnManga()

    b = "Return-" + name + ".txt"
    with open(b, "w+") as f:
        f.write("                Manga Management System \n")
        f.write("                   Returned By: " + name + "\n")
        f.write("    Date: " + dt.getDate() + "    Time:" + dt.getTime() + "\n\n")
        f.write("S.N.\t\tBookname\t\tCost\n")

    total = 0.0
    for i in range(3):
        if Mangalist.manganame[i] in data:
            with open(b, "a") as f:
                f.write(str(i + 1) + "\t\t" + Mangalist.manganame[i] + "\t\t$" + Mangalist.cost[i] + "\n")
                Mangalist.quantity[i] = int(Mangalist.quantity[i]) + 1
            total += float(Mangalist.cost[i])

    print("\t\t\t\t\t\t\t" + "$" + str(total))
    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    stat = input()
    if (stat.upper() == "Y"):
        print("By how many days was the book returned late?")
        day = int(input())
        fine = 2 * day
        with open(b, "a") as f:
            f.write("\t\t\t\t\tFine: $" + str(fine) + "\n")
        total = total + fine

    print("Final Total: " + "$" + str(total))
    with open(b, "a") as f:
        f.write("\t\t\t\t\tTotal: $" + str(total))

    with open("Stock.txt", "w+") as f:
        for i in range(3):
            f.write(
                Mangalist.manganame[i] + "," + Mangalist.authorname[i] + "," + str(Mangalist.quantity[i]) + "," + "$" +
                Mangalist.cost[i] + "\n")