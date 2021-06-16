User={}
Passs={}
FACULTY=["1","FACULTY2","FACULTY3","FACULTY4"]
PASSWORD=["1","2222","3333","4444"]
Branch=["MECHANICAL","COMPUTER SCIENCE","CIVIL","CLOUD"]
sub={0:[["THERMODYNAMICS","MATHS","PG","EEE"],["E-COMMERCE","MARKETING","LAW","NATURAL RESOURCES"]],1:[["C++","PHP","MATHS","JAVA"],["E-COMMERCE","NANO SCIENCE","CYBER LAW","FRENCH"]],2:[["AUTO CAD","CHEMISTRY","PHYSICS","ENGLISH"],["SOFT COMPUTING","NANO SCIENCE","FRENCH","WEB DESIGNING"]],3:[["C++","PHP","HACKING","JAVA"],["E-COMMERCE","NANO SCIENCE","CYBER SECURITY","FRENCH"]]}
def register(userid,passwd,name=None,mobile=None,branch=None,subject=None,marks=None):
    temp=[]
    temp.append(name)
    temp.append(mobile)
    temp.append(branch)
    temp.append(subject)
    Passs[userid]=passwd
    temp.append(marks)
    User[userid]=temp
    
def login(userid,passwd):
    
    if Passs[userid]==passwd:
        update(userid)
        return True,User
        
    else:
        return False,0
def update(user):
    print("{:<5}Name{:<20}".format("",User[user][0]))
    print("{:<5}Branch{:<20}".format("",User[user][2]))
    a="{:<25}{:<10}{:<10}{:<10}{:<10}{:<10}"
    print(a.format("","CIE-I","MSE","CIE-II","ESE","TOTAL"))
    for i in User[user][3]:
        m1,m2,m3,m4=User[user][4][i]
        sum=0
        
        for j in User[user][4][i]:
            if j!='':
                sum=sum+j
        if sum==0:
            sum=''
        
        print(a.format(i,m1,m2,m3,m4,sum))
 
    
    
    
    


