import requests, datetime, json, random, warnings, os, threading, time
from colorama import *
from requests.sessions import Session

init()

def warn(*args, **kwargs):
    pass

warnings.warn = warn

class Library:
    Name = "9e1 Spam Call"

    class Json:
        def Read(FileName, Key):
            File = open(FileName, "r")
            Data = json.loads(File.read())

            return Data[Key]

    def Print(message, mode = None, title = None):
        Hour = int(datetime.datetime.now().strftime("%H")) - 12
        Minute = int(datetime.datetime.now().strftime("%M"))

        if len(str(Minute)) < 2:
            Minute = f"0{Minute}"

        if not mode == None:
            if str.lower(mode) == "warning":
                Theme = Fore.YELLOW
                Title = "WARNING"
            elif str.lower(mode) == "normal":
                Theme = Fore.LIGHTBLUE_EX
                Title = Library.Name
            elif str.lower(mode) == "error":
                Theme = Fore.LIGHTRED_EX
                Title = "ERROR"
        else:
            Theme = Fore.LIGHTBLUE_EX
            Title = Library.Name
            
        if not title == None:
            Title = title
            
        Time = f"{Hour}:{Minute}".replace("-", "")
        
        Callback = print(f"  {Fore.WHITE}{Time}{Fore.RESET} | {Theme}{Title}{Fore.RESET} | {Fore.LIGHTWHITE_EX}{message}{Fore.RESET}")
        
        return Callback

    def Input(message, mode = None, title = None):
        Hour = int(datetime.datetime.now().strftime("%H")) - 12
        Minute = int(datetime.datetime.now().strftime("%M"))

        if len(str(Minute)) < 2:
            Minute = f"0{Minute}"

        if not mode == None:
            if str.lower(mode) == "warning":
                Theme = Fore.YELLOW
                Title = "WARNING"
            elif str.lower(mode) == "normal":
                Theme = Fore.LIGHTBLUE_EX
                Title = Library.Name
            elif str.lower(mode) == "error":
                Theme = Fore.LIGHTRED_EX
                Title = "ERROR"
        else:
            Theme = Fore.LIGHTBLUE_EX
            Title = Library.Name
            
        if not title == None:
            Title = title
            
        Time = f"{Hour}:{Minute}".replace("-", "")
        
        Callback = input(f"  {Fore.WHITE}{Time}{Fore.RESET} | {Theme}{Title}{Fore.RESET} | {Fore.LIGHTWHITE_EX}{message}{Fore.RESET}: ")
        
        return Callback

    def vaildToken(Token):
        User = requests.get("https://discordapp.com/api/v9/users/@me", headers = {
            "authorization": Token
        })
        print(User.status_code)

        if User.status_code == 200 or User.status_code == 204:
            return [True, User]
        else:
            return [False, None]

Token = Library.Json.Read("./Data.json", "discordToken")

if Library.vaildToken(Token)[0] == True:
    User = Library.vaildToken(Token)[1]

    Name = User.json()["username"]
    Dis = User.json()["discriminator"]
    Username = f"{Name}#{Dis}"
    Session = requests.Session()
    Called = 0

    os.system("cls")
    os.system("title "+ f"{Library.Name} * Client: ({Username})")

    def Spam(Token, ChannelID, Target):
        global Called

        RequestCall = Session.post(f"https://discord.com/api/v9/channels/{ChannelID}/call/ring",
            json = {
                "recipients": [Target]
            }, 
            
            headers = {
                "authorization":  Token,
                "user-agent": Library.Name
            }
        )

        if RequestCall.status_code == 204:
            Called = Called + 1

            os.system("title "+ f"{Library.Name} * Client: ({Username}) * {Called}")

            time.sleep(0.1)

            RequestCall = Session.post(f"https://discord.com/api/v9/channels/{ChannelID}/call/stop-ringing",
                json = {
                    "recipients": [Target]
                }, 
                
                headers = {
                    "authorization":  Token,
                    "user-agent": Library.Name
                }
            )

            if RequestCall.status_code == 204:
                Called = Called + 1

                os.system("title "+ f"{Library.Name} * Client: ({Username}) * {Called}")

                
            
    def __Start():
        global ChannelID
        global ID
            
        while True:
            Spam(Token, ChannelID, ID)

    Library.Print("Loaded Modules | Created by  9e1 (Rainn)", "normal")

    ChannelID = Library.Input("Channel ID (Servers do not function)")
    ID = int(Library.Input("Target ID"))
    Threads = int(Library.Input("Threads (Max 5 : Min 1)"))

    if Threads > 5 or Threads < 1:
        Threads = 5

    Library.Print(f"Module Activity : True", "normal")

    for _threaded in range(Threads):
        threading.Thread(target = __Start).start()
else:
    Library.Print("Failed to Login : Invaild Token (Go to ./Data.json)")

    input("Press Enter to close.. >")
