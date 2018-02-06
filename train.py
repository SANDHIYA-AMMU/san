from datetime import date
from tabulate import tabulate
bid=10
#dictionary for city code
ccode={'pondicherry':'pdy','chennai':'chn','madurai':'mdu'}
l=['l','m','h']
#BY USING CITY_CODE(ccode) LIST THE TRAIN USING DICT
srcdest={'pdychn':['pc1','pc2'],'chnmdu':['cm1','cm2']}

#TRAIN DICT
#IT CONTAINS--> TRAIN_NO->LIST_OF [ train_name, Departure_time, Arrival_time,
#               Weekdays("0123456")], LIST[CLASSES]
t={'pc1':[['name','deptime','arr_time','tarvel_time'],['c1','c2']],
    'cm1':[['name','deptime','arr_time','tarvel_time'],['c1','c2']],
    'cm2':[['name','deptime','arr_time','tarvel_time'],['c1','c2']],
    'pc2':[['name','deptime','arr_time','tarvel_time'],['c1','c2']]}

#CLASS DICT CONTAINS CLASS --->LIST OF SEATS [LOWER BERTH,MIDDLE BERTH, UPPER BERTH]
c={'pc1c1':[[10,10,10,],[50]],'pc1c2':[[15,15,15],[30]]}
datedict={}

#FUNCTION FOR GETTING DETAILS FROM DICT AND STORE AND RETURN TO OBJECT
def trainl(tno): #train_no(tno) as arguement
    #get dict train_det,class_det from file
    name=t[tno][0][0]
    dep=t[tno][0][1]
    arr=t[tno][0][2]
    ttime=t[tno][0][3]
    class_section=t[tno][1]
    return  tno , name , dep , arr , ttime , class_section

    # RETURN TRAIN DETAILS...

#FUNCTION FOR LISTING TRAINS...
def gettraindetails(src,dest):#arg as src dest
    #get dict ccode,srcdest from file
    train_list=srcdest[ccode[src]+ccode[dest]]
    #GETTING TRAIN LIST
    t=[]
    for i in range(len(train_list)):
        t.append(trainl( train_list[i]))
    print (tabulate(t, headers=['Train_NO','Train_Name', 'Departure','Arrival','Train_Time','Classes']))

#FUNCTION FOR CHECKING SEAT AVAILABITY FOR COMPARTMENT....
def checkdet(tn,cno,dat):
    while dat not in datedict:
        v={}
        v[tn+cno]=c[tn+cno]
        datedict[dat]=v
    return sum(datedict[dat][tn+cno][0])==0 and "no seats" or sum(datedict[dat][tn+cno][0])



def pickberth(cno,b1,p):
    b1=l.index(b1)
    return datedict[dat][cno][0][b1]>0 and l[b1] or p=='y' and l[c[cno][0].index(max(datedict[dat][cno][0]))] or 'no seats in '+l[b1]
def getpasdet(i):
    name=input("Enter Name:")
    age=input("Enter Age:")
    berth=input("Enter Berth(l/m/u)")
    opt=input("Enter Optional Berth(y/n)")
    return i,name,age,berth,opt

def get_ticket_total():
    return [10,10,10]

def generateseatno(p,li):
    t=[]
    for i in range(len(p)):
        s=l.index(p[i][5])
        t.append("seat_no"+str(((get_ticket_total()[s]-li[s])*3)+(s+1)))
        li[s]=li[s]-1
    return t

def passDetail(p):
    #print(tabulate(bookDetail(),headers=['S_NO','Passenger_Name', 'Age','Berth','seat_No']))
    #print(tabulate (p, headers=['S_NO','Passenger_Name', 'Age','Berth','Optional Berth','Berth Status']))
    bd =[ ]
    for i in range(len(p)):
        sno=p[i][0]
        passen=p[i][1]
        age=p[i][2]
        berth=p[i][3]
        seatno=getseat[i]
        bd.append ( [ sno , passen , age , berth , seatno ] )
    return bd
def bookDetail(p,seat):
    b=[]
    global bid
    global getseat
    print("Booking ID: b"+str(bid))
    pbid="b"+str(bid)
    bid+=1
    getseat=generateseatno(p,datedict[dat][tn+cno][0])
    b.append([str(pbid),p[0][1],cno,getseat,])
    print("No. of Seats:",seat,"And Seats are: ",getseat)
    print("Price:",datedict[dat][tn+cno][1][0]*seat)
    return b

def main():
    #fro=input("Enter From:")
    fro="pondicherry"
    #to=input("Enter to:")
    to="chennai"
    dat= list(map(int,input("Enter date within 15 days yyyy/mm/dd").split('/')))
    #dat=list(map(int,"1990/9/9".split('/')))
    dat=date(dat[0],dat[1],dat[2])
    print("\n\nFROM:",fro)
    print("TO",to)
    print("Date:",dat)
    print("\n\n")
    print(str(dat - date.today()),"hi")
    if dat==date.today():
        rang=0
    else:
        rang=int(str(dat - date.today()).split(" ")[0])
    #By using this range return the main
    if rang<=15 and rang>=0 :
        print("ok in range")
        return fro,to,dat
    else:
        print("Enter the Date correct date:")
        return main()
    #get the details
def selectTrain(fro,to):
    gettraindetails(fro,to)
    tn=input("Enter tno")
    cno=input("Enter 'c1/c2':")
    #tn="pc1"
    #cno="c1"
    seat_count=checkdet(tn,cno,dat)
    print("\n\nAvailabilty:\nTrain_no:\t",tn," and class",cno,":\t",seat_count) #claculate the day by using math.....
    return tn,cno,seat_count


def getpassengerdet(seat_count,tn,cno):
    seat=int(input("Enter Total no_of Seats:"))
    p=[]
    g=0
    if seat<=seat_count:
        for i in range(int(seat)):
            p.append( list(getpasdet(i+1)))
            berth=pickberth(tn+cno,p[i][3],p[i][4])
            p[i].append(berth)
            if "no seats" in p[i][5]:
                g=1
        print(tabulate (p, headers=['S_NO','Passenger_Name', 'Age','Berth','Optional Berth','Berth Status']))
    if g==1:
        getuser=input("Press Y to exit or N to Re-Enter the passenger Details")
        if getuser=='y' or getuser=='Y':
            getpassengerdet(seat_count,tn,cno)
    else:
        bye=input("Enter any to see Booking Details:")
        return p,seat

def displayDetail(p,seat):
    print("Booking Details\n")
    print(tabulate(bookDetail(p,seat),headers=['Booking_Id','From','To','Date','Train_No','Class']))
    print("\n")
    print("Passenger Details\n")
    print(tabulate(passDetail(p),headers=['S_NO','Passenger_Name', 'Age','Berth','seat_No']))
    print(datedict)


fro,to,dat=main()
tn,cno,seat_count=selectTrain(fro,to)
p,seat=getpassengerdet(seat_count,tn,cno)
displayDetail(p,seat)


