import requests,os,threading,optparse,random,time
paser=optparse.OptionParser()
paser.add_option('-p','--path',dest='path',help="add path of txt")
(o,a)=paser.parse_args()
count=0
path=o.path.replace("\\","/")
dir=path.split("/")
dir=dir[-1].replace(".txt","")
###########################################################################################
#Emty list
list_main=[]
p_l=[]
clean_data=[]
not_done=[]
###########################################################################################
try:
    os.mkdir(dir)
except:
    pass
#########################################
#Reading the proxy txt:
p=open("work_proxy.txt","r")
for l in p.readlines():
    p_l.append(l)
###########################################
#Dividing proxy into 4 sections
proxy1=random.choice(p_l)
proxy2=random.choice(p_l)
proxy3=random.choice(p_l)
proxy4=random.choice(p_l)
##############################################
#Reading the path of the txt provide above
f=open(path,"r")
list_main=f.readlines()
################################################
#Checking if the dat is already done 
def check():
    global list_ , list_main
    list_=os.listdir()
    if len(list_)==len(list_main):
        print("[+] All the data has been done")
        exit()
    else:
       for i in list_main:
            on=i.split("/")
            if on[-1].strip() not in list_:
                clean_data.append(i)
       if len(clean_data)!=len(list_main):
            print("[+] Not done:",len(clean_data))
            list_main=clean_data
    list_main=clean_data
check()
##################################################################
#Dividing list into 4 part 
my_list=list_main
part1 = my_list[:len(my_list)//4]
part2 = my_list[len(my_list)//4:len(my_list)//2]
part3 = my_list[len(my_list)//2:3*len(my_list)//4]
part4 = my_list[3*len(my_list)//4:]\
##################################################
#Function to divied to download that list 
def first():
    global count
    for i in part1:
        name=str(i).split("/")
        name=str(name[-1].strip())
        re=requests.get(i.strip(),proxies={"http:":proxy1}).content
        g=open(name,"wb")
        g.write(re)
        g.close()
        count+=1

def second():
    global count
    for s in part2:
        n=str(s).split("/")
        n=str(n[-1].strip())
        r=requests.get(s.strip(),proxies={"http:":proxy2}).content
        u=open(n,"wb")
        u.write(r)
        u.close()
        count+=1
def thrid():
    global count
    for thr in part3:
        t=str(thr).split("/")
        t=str(t[-1].strip())
        tr=requests.get(thr.strip(),proxies={"http:":proxy3}).content
        th=open(t,"wb")
        th.write(tr)
        th.close()
        count+=1
def fourth():
    global count
    for fo in part4:
        f=str(fo).split("/")
        f=str(f[-1].strip())
        rf=requests.get(fo.strip(),proxies={"http:":proxy4}).content
        fou=open(f,"wb")
        fou.write(rf)
        fou.close()
        count+=1
####################################################
#thread function
def start_thread():
    firs=threading.Thread(target=first)
    s=threading.Thread(target=second)
    thri=threading.Thread(target=thrid)
    fourt=threading.Thread(target=fourth)
    firs.daemon=True
    s.daemon=True
    thri.daemon=True
    fourt.daemon=True
    firs.start()
    s.start()
    thri.start()
    fourt.start()
#######################################################
#Printing function
def print_():
    global count
    print(f"""[+] Saving to:{os.getcwd()}\n[+] Using proxy 1 name:{proxy1.strip()}\n[+] Using proxy 2 name:{proxy2.strip()}\n[+] Using proxy 3 name:{proxy3.strip()}\n[+] Using proxy 4 name:{proxy4.strip()}\n[+] Total file to be done:{len(list_main)}""")
    while count<len(list_main):
        print(f"[+] Total file done are:{count}",end="\r",flush=True)
        time.sleep(1)
    print("\n")
start_thread()
print_()
