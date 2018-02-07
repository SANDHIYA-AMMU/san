import json
from datetime import date
from tabulate import tabulate
file = open("bid.txt", "r")
bid=file.read()
file.close()
bid=int(bid)
bid+=1

#dictionary for city code
ccode={'pondicherry':'pdy','chennai':'chn','madurai':'mdu'}
l=['low','middle','upper']

#BY USING CITY_CODE(ccode) LIST THE TRAIN USING DICT
srcdest={'pdychn':['pc1','pc2'],'chnmdu':['cm1','cm2']}

#TRAIN DICT
#IT CONTAINS--> TRAIN_NO->LIST_OF [ train_name, Departure_time, Arrival_time,
#               Weekdays("0123456")], LIST[CLASSES]
t={'pc1':[['Cheran','10:00','13:00','3 hours'],['a','b']],
   'cm1':[['pandiyan Exp','12:00','20:00','8 hours'],['a','b']],
    'cm2':[['Pallavan Exp','00:00','08:00','8 hours'],['a','b']],
    'pc2':[['MGR Exp','13:00','16:00','3 hours'],['a','b']]}

#CLASS DICT CONTAINS CLASS --->LIST OF SEATS [LOWER BERTH,MIDDLE BERTH, UPPER BERTH]
c={'pc1a':[[10,10,10,],[50]],'pc1b':[[15,15,15],[30]],
    'pc2a':[[10,10,10,],[50]],'pc2b':[[15,15,15],[30]],
    'cm1a':[[10,10,10,],[100]],'cm1b':[[15,15,15],[100]],
    'cm2a':[[10,10,10,],[100]],'cm2b':[[15,15,15],[100]],
    }
datedict = json.load(open("datedict.txt"))
#FUNCTION FOR GETTING DETAILS FROM DICT AND STORE AND RETURN TO OBJECT
def trainl(tno): #train_no(tno) as arguement
    #get dict train_det,class_det from file
    name=t[tno][0][0]
    dep=t[tno][0][1]
    arr=t[tno][0][2]
    ttime=t[tno][0][3]
    class_section=t[tno][1]
    return  tno , name , dep , arr , ttime , class_section  # return as list
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
        datedict[(dat)]=v
    return sum(datedict[dat][tn+cno][0])==0 and "no seats" or sum(datedict[dat][tn+cno][0])


def pickberth(cno,b1,p):
    b1=l.index(b1)
    return datedict[str(dat)][cno][0][b1]>0 and l[b1] or p=='y' and l[datedict[str(dat)][0].index(max(datedict[str(dat)][cno][0]))] or 'no seats in '+l[b1]
def getpasdet(i):
    name=input("Enter Name:")
    age=input("Enter Age:")
    berth=input("Enter Berth(low/middle/upper)")
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
    getseat=generateseatno(p,datedict[str(dat)][tn+cno][0])
    b.append([str(pbid),p[0][1],cno,getseat,])
    print("No. of Seats:",seat,"And Seats are: ",getseat)
    print("Price:",datedict[str(dat)][tn+cno][1][0]*seat)
    return b

def main():
    fro=input("Enter From:")
    to=input("Enter to:")
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
    if rang<=15 and rang>=0 :
        return fro,to,dat
    else:
        print("Enter the Date correct date:")
        return main()

def selectTrain(fro,to):
    gettraindetails(fro,to)
    tn=input("Enter train no")
    cno=input("Select Class:")
    seat_count=checkdet(tn,cno,str(dat))
    print("\n\nAvailabilty:\nTrain_no:\t",tn," \nclass",cno,":\nSeat Count:\t",seat_count) #claculate the day by using math.....
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
        bye=input("Enter any key to see Booking Details:")
        return p,seat
def displayDetail(p,seat):
    print('='*80)
    print("Booking Details".center(80))
    print("\n\n")
    print(tabulate(bookDetail(p,seat),headers=['Booking_Id','From','To','Date','Train_No','Class']))
    print("\n")
    print("Passenger Details".center(80))
    print("\n\n")
    print(tabulate(passDetail(p),headers=['S_NO','Passenger_Name', 'Age','Berth','seat_No']))
    file = open("bid.txt","w")
    file.write(str(bid))
    file.close()
    json.dump(datedict, open("datedict.txt",'w'))

fro,to,dat=main()
tn,cno,seat_count=selectTrain(fro,to)
p,seat=getpassengerdet(seat_count,tn,cno)
displayDetail(p,seat)
