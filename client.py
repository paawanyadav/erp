from server import *
import random as r
import requests

def confirmation(w,mobile):
    url= "https://www.fast2sms.com/dev/bulk"
    num=mobile
    payload = "sender_id=FSTSMS&message=-\nWelcome To ERP System.\nYour Four Digit OTP is:"+str(w)+".\nThank You. \nFrom:- ERP HEAD OFFFICE &language=english&route=p&numbers="+mobile
    headers = {
        'authorization': "0ZJHquCUBgVU82nNE5Htfey68xUdK2SIEF3FmaqHpFrZzBHo1BlH0UcMI1Ta",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    

print("\n\n")
print("{:<8}=======================================================".format(""))
print("{:<8}||{:<8}*******    *******      *******   {:<8}||".format("","",""))
print("{:<8}||{:<8}*              *          *    *          * {:<8}||".format("","",""))
print("{:<8}||{:<8}****         *******      *******  {:<8}||".format("","",""))
print("{:<8}||{:<8}*              *  *            *             {:<8}||".format("","",""))
print("{:<8}||{:<8}*******    *   *           *       PAWAN{:<2}||".format("","",""))
print("{:<8}=======================================================".format(""))
while 1:
    check=input("\n\n\n1-REGISTER\n2-LOGIN\n3- TEACHER LOGIN\n\n")
   
    if check=='1':
        user_name=input("ENTER YOUR USER ID   ")
        pass_word=input("ENTER YOUR PASSWORD   ")
        confirm=input("RE-ENTER YOUR PASSWORD   ")
        if pass_word==confirm:
            name=input("ENTER YOUR NAME   ")
            mobile=input("ENTER YOUR 10 DIGIT MOBILE NO.   ")
            w=r.randint(1111,9999)
            confirmation(w,mobile)
            ver=int(input("ENTER YOUR FOUR DIGIT VERIFICATION CODE"))
            if(ver==w):
                print("YOUR NUMBER IS VERIFY SUCCESSFULLY.")
                flag=True
            else:
                print("YOUR OTP IS NOT VALID!!!!!!!!!!!!!!!!")
                flag=False



            if(flag==True):
                        print("CHOOSE YOUR BRANCH\n")
                        for i in Branch:
                            print(i)
                        opt=int(input("CHOOSE 0,1,2 OR 3"))
                        bb=Branch[opt]
                        try:
                            print("YOUR SUBJECT ARE")
                            for i in sub[opt][0]:
                                print(i)
                            subb=sub[opt][0]
                            print("\n\nCHOOSE YOUR OPEN ELECTIVE")
                            for i in sub[opt][1]:
                                print(i)
                            opt1=int(input("CHOOSE YOUR OPEN ELECTIVE\n0,1,2 OR 3"))
                            oe=sub[opt][1][opt1]
                            subb.append(oe)
                            d={}
                            for i in subb:
                                    d[i]=[""]*4
                        except:
                            print("-----ENTER VALID-----")
                            
                        register(user_name,pass_word,name,mobile,bb,subb,d)
                    
    elif check=='2':
        user_name=input("ENTER YOUR USER ID   ")
        pass_word=input("ENTER YOUR PASSWORD   ")
        a,b=login(user_name,pass_word)
        if a==True:
            opt=int(input("PRESS 1 FOR SEE DETAILS 0 FOR EXIT\n\n"))
            if opt==1:
                print("YOUR DETAILS ARE GIVEN BELOW\n\n")
                print("NAME IS {}".format(b[user_name][0]))
                print("MOBILE NO IS {}".format(b[user_name][1]))
                print("BRANCH IS {}".format(b[user_name][2]))
                print("YOUR SUBJECT ARE:-")
                for i in b[user_name][3][:-1]:
                    print(i)
                print("OPEN ELECTIVE-",b[user_name][3][-1])
               

                
            
        else:
            print("----------TRY AGAIN(INCORRECT PASSWORD)----------")
            exit()

    elif check=='3':
        fac_user=input("ENTER YOUR USERNAME   ")
        fac_pass=input("ENTER YOUR PASSWORD   ")
        a=FACULTY.index(fac_user)
        
        if PASSWORD[a]==fac_pass:
            print("LOGIN SUCCESSFULLY   ")
                       
            while 1:
                
                opt=int(input("1-FOR ENTER MARKS\n2-FOR EXIT"))
                if opt==1:
                    search=input("ENTER USER NAME OF STUDENT YOU WANT TO SEARCH")
                    f={"CIE-I":0,"MSE":1,"CIE-II":2,"ESE":3}
                    try:

                        s=input("ENTER NAME OF SUBJECT:-   ")
                        e=input("ENTER NAME OF EXAM:-    ")
                        m=int(input("ENTER MARKS:-   "))
                        User[search][4][s][f[e]]=m
                        update(search)
                    except:
                        pass
                else:
                    break
        else:
            print("INVALID USERNAME OR PASSWORD")
    else:
        print("----------PLEASE ENTER VALID OPTION ---------- ")


