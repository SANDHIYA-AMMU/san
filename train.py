t={'t1':[['name','deptime','arr_time','tarvel_time',"0123456"],['c1','c2']],
       't2':[['name','deptime','arr_time','tarvel_time',"1245"],['c1','c2']],
       't3':[['name','deptime','arr_time','tarvel_time',"2345"],['c1','c2']],
       't4':[['name','deptime','arr_time','tarvel_time',"012345"],['c1','c2']],
       't5':[['name','deptime','arr_time','tarvel_time',"012345"],['c1','c2']]}
c={'t1c1':[0,10,2],'t1c2':[1,15,15],
       't1c1':[12,1,12],'t1c2':[1,5,15],
       't1c1':[0,12,33],'t1c2':[1,15,10],
       't1c1':[12,13,13],'t1c2':[15,15,15],
       't1c1':[13,13,13],'t1c2':[19,19,19]}


def trdetails(tno,cno):
    name=t[tno][0][0]
    dep=t[tno][0][1]
    arr=t[tno][0][2]
    ttime=t[tno][0][3]
    weekdays=getweek(t[tno][0][4])
    class_section=t[tno][1]
    print(tno,name,dep,arr,ttime,weekdays,class_section)
    print("Available seats in train " +tno+ ":" ,avail(tno,cno,day))


def pgrdet():
    return input("enter your berth preference lower/middle/upper"),input("Other Available berth Preference(yes/no)")

def train(Srcs,Desti):
    try:
        city={'pondicherry':'pndy','chennai':'chni','madurai':'mdura','villupuram':'vlpm'}
        train={'pndychni':['t1','t2'],'chnimdura':['t4','t5'],'vlpmmdura':['t3']}
        print("List of train from "+Srcs+" to "+Desti+":")
        return (train[city[Srcs]+city[Desti]])
    except:
        return ("No trains from "+Srcs+" to "+Desti)

def avail(tno,cno,day):
    return sum(c[tno+cno])==0 and "no seats" or sum(c[tno+cno])

def getweek(w):
        l=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        k=[]
        for i in range(len(w)):
            k.append(l[int(w[i])])
        return k
def pickberth(cno,b1,p):
    l=['low','middle','high']
    b1=l.index(b1)
    return c[cno][b1]>0 and l[b1] or p=='yes' and l[c[cno].index(max(c[cno]))] or 'no seats in '+l[b1]


from datetime import date
import calendar
my_date = date.today()
day = calendar.day_name[my_date.weekday()]
Srcs = input("Enter source")
Desti = input("Enter destination")
tr=train(Srcs,Desti)
print(tr)
tno=input('choose a train')
cno=input("Enter coach (c1 or c2): ")
trdetails(tno,cno)
berth,pref=pgrdet()
print(pickberth(tno+cno,berth,pref))
