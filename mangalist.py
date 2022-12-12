class Manga_list:
    def mangalist():
        global manganame
        global authorname
        global quantity
        global cost
        manganame=[]
        authorname=[]
        quantity=[]
        cost=[]
        with open("stock.txt","r") as f:
            
            lines=f.readlines()
            lines=[x.strip('\n') for x in lines]
            for i in range(len(lines)):
                ind=0
                for a in lines[i].split(','):
                    if(ind==0):
                        manganame.append(a)
                    elif(ind==1):
                        authorname.append(a)
                    elif(ind==2):
                        quantity.append(a)
                    elif(ind==3):
                        cost.append(a.strip("$"))
                    ind+=1