# ═║╔╗╚╝╠╣╩╬
#Colorama
from distutils.log import error
from xml.etree import ElementInclude
from colorama import *
#Others
import os, requests, random, string, base64, threading, socket, webbrowser, concurrent.futures
#Main Menu
def MainMenu():
    os.system('title PURO TOOLKIT 0.1 - Main Menu')
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
    print(F'{Fore.BLACK}║{Fore.WHITE} 4 | Misc Menu                                         {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 0 | Exit                                              {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    try:
        while True:
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
                break
            else:
                print(f'{Fore.RED}ERROR |  {Fore.WHITE}Please select a valid option')
    except ValueError:
        print(f'\n{Fore.RED}ERROR | {Fore.WHITE}')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Main Menu')
        MainMenu()
#Credits Menu
def CreditsMenu():
    os.system('title PURO TOOLKIT 0.1 - Credits Menu')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Credits Menu                                          {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Made By: Puro#9999                                    {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} Version: 0.1.0                                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}║                                                       ║')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} 1 | GitHub                                            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 2 | YouTube                                           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 0 | Main Menu                                         {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    try:
        CreditsChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
        if CreditsChoice == 1:
            webbrowser.open_new("https://github.com/RealPuro")
        elif CreditsChoice == 2:
            webbrowser.open_new("https://www.youtube.com/channel/UCBqqNNYO5ku5gNgGuf41DLw")
        elif CreditsChoice == 0:
            MainMenu()
        else:
            print(f'\n{Fore.RED}ERROR |  {Fore.WHITE}Incorrect option')
            input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Main Menu')
            CreditsMenu()
    except ValueError:
        print(f'\n{Fore.RED}ERROR |  {Fore.WHITE}Incorrect option')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Main Menu')
        CreditsMenu()
#Discord Menu
def DiscordMenu():
    os.system('title PURO TOOLKIT 0.1 - Discord Menu')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Menu                                          {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} 1 | Nitro Generator                                   {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 2 | Nitro Checker                                     {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 3 | Token Generator                                   {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 4 | Token to Account Info                             {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 5 | Email/Password to Token                           {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 6 | User ID to Half Token                             {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 7 | Webhook Spammer                                   {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 8 | Webhook Deleter                                   {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 9 | Next page                                         {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 0 | Main Menu                                         {Fore.BLACK}║')
    print(f'{Fore.BLACK}╚══════════════════════════════════════════════════════╝\n')#-------------------║
    try:
        DiscordMenuChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
        if DiscordMenuChoice == 1:
            DiscordNitroGenerator()
        elif DiscordMenuChoice == 2:
            DiscordNitroChecker()
        elif DiscordMenuChoice == 3:
            DiscordTokenGenerator()
        elif DiscordMenuChoice == 4:
            DiscordTokenInfo()
        elif DiscordMenuChoice == 5:
            DiscordTokenEmailPass()
        elif DiscordMenuChoice == 6:
            DiscordWebhookSpammer()
        elif DiscordMenuChoice == 7:
            DiscordWebhookDeleter()
        elif DiscordMenuChoice == 8:
            DiscordHalfToken()
        elif DiscordMenuChoice == 9:
            DiscordMenu2()
        elif DiscordMenuChoice == 0:
            MainMenu()
        else:
            print(f'\n{Fore.RED}ERROR | {Fore.WHITE}Incorrect option')
            input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordMenu()
    except ValueError:
        print(f'\n{Fore.RED}ERROR | {Fore.WHITE}Incorrect option')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
#Discord Menu2
def DiscordMenu2():
    os.system('title PURO TOOLKIT 0.1 - Discord Menu 2')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Menu 2                                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} 1 | Hypesquad House                                   {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 2 | Token Disabler                                    {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 8 | Previous page                                     {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.RED} 9 | Next page (WIP)                                   {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 0 | Main Menu                                         {Fore.BLACK}║')
    print(f'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    try:  
        DiscordMenu2Choice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))  
        if DiscordMenu2Choice == 1:
            DiscordDisableToken()
        elif DiscordMenu2Choice == 2:
            DiscordHypesquadHouse()
        elif DiscordMenu2Choice == 8:
            DiscordMenu()
        elif DiscordMenu2Choice == 9:
            DiscordMenu2()
        elif DiscordMenu2Choice == 0:
            MainMenu()
        else:
            print(f'\n{Fore.RED}ERROR | {Fore.WHITE}Incorrect option')
            input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordMenu()
    except ValueError:
        print(f'\n{Fore.RED}ERROR | {Fore.WHITE}Incorrect option')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
#Network Menu
def NetworkMenu():
    os.system('title PURO TOOLKIT 0.1 - Misc Menu')
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
    try:
        NetworkMenuChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))

        if NetworkMenuChoice == 1:
            LocalChatServer()
        elif NetworkMenuChoice == 2:
            LocalChatClient()
        elif NetworkMenuChoice == 3:
            PortScanner()
        elif NetworkMenuChoice == 0:
           MainMenu()
        else:
            print(f'\n{Fore.RED}ERROR |  {Fore.WHITE}Incorrect option')
            input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Main Menu')
            MainMenu()
    except ValueError:
        print(f'\n{Fore.RED}ERROR |  {Fore.WHITE}Incorrect option')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Main Menu')
        MainMenu()
#Misc Menu
def MiscMenu():
    os.system('title PURO TOOLKIT 0.1 - Misc Menu')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Misc Menu                                             {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} 1 | Receive SMS Online (Web)                          {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 0 | MainMenu                                          {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    try:
        MiscMenuChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
        if MiscMenuChoice == 1:
            webbrowser.open_new("https://www.freereceivesms.com/en/")
        elif MiscMenuChoice == 0:
           MainMenu()
        else:
            print(f'\n{Fore.RED}ERROR |  {Fore.WHITE}Incorrect option')
            input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Main Menu')
            MainMenu()
    except ValueError:
        print(f'\n{Fore.RED}ERROR |  {Fore.WHITE}Incorrect option')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Main Menu')
        MainMenu()
#Discord Menu > Nitro Generator
def DiscordNitroGenerator():
    os.system('title PURO TOOLKIT 0.1 - Discord Menu > Nitro Generator')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Menu > Nitro Generator                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    try:
        print(f'{Fore.YELLOW}WARN | {Fore.WHITE}Mostly of the codes will be invalid, so generating a working nitro is very hard.{Fore.WHITE}')
        DiscordNitroGeneratorAmount = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Amount: '))
        DiscordNitroGeneratorLength = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Length (Default: 16): '))
        DiscordNitroGeneratorFileName = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}File Name (Without .txt): ')
        print()
        DiscordNitroGeneratedAmount = 1
        DiscordNitroFile = open(f'{DiscordNitroGeneratorFileName}.txt', 'w')
        DiscordNitroFile.write(f'{DiscordNitroGeneratorAmount} Discord Nitro Codes with a length of {DiscordNitroGeneratorLength} characters | Generated with PuroToolKit')
        for i in range(DiscordNitroGeneratorAmount):
            code = 'https://discord.gift/' + ('').join(random.choices(string.ascii_letters + string.digits, k=DiscordNitroGeneratorLength))
            print(f'{Fore.BLACK}PURO TOOLKIT (Code: {DiscordNitroGeneratedAmount}) | {Fore.WHITE}{code}')
            DiscordNitroFile.write(f'\n{code}')
            DiscordNitroGeneratedAmount += 1
        DiscordNitroFile.close()
        print(f'\n{Fore.BLACK}INFO | {Fore.WHITE}Generated {DiscordNitroGeneratorAmount} codes with a length of {DiscordNitroGeneratorLength} characters')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
    except ValueError:
        print(f'\n{Fore.RED}ERROR | {Fore.WHITE}Invalid amount')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
#Discord Menu > Nitro Checker
def DiscordNitroChecker():
    os.system('title PURO TOOLKIT 0.1 - Discord Menu > Nitro Checker')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Menu > Nitro Checker                          {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    try:
        DiscordNitroCheckerAmount = 0
        DiscordNitroCheckerFileName = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}File Name (Without .txt): ')
        DiscordNitroCheckerValidSave = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Save Valid Codes? (y/n): ')
        DiscordNitroCheckerInvalidSave = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Save Invalid Codes? (y/n): ')
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
                DiscordNitroCheckerAmount = DiscordNitroCheckerAmount + 1
                if r.status_code == 200:
                    print(f'{Fore.GREEN}VALID (Code: {DiscordNitroCheckerAmount}) (Status: {r.status_code}) | {Fore.WHITE}{NitroCode}')
                    if DiscordNitroCheckerValidSave == "y":
                        DiscordValidFile = open(f'{DiscordNitroCheckerFileName}Valid.txt', 'a')
                        DiscordValidFile.write(f'\n{NitroCode}')
                else:
                    print(f'{Fore.RED}INVALID (Code: {DiscordNitroCheckerAmount}) ({r.status_code}) | {Fore.WHITE}{NitroCode}')
                    if DiscordNitroCheckerInvalidSave == "y":
                        DiscordInvalidFile = open(f'{DiscordNitroCheckerFileName}Invalid.txt', 'a')
                        DiscordInvalidFile.write(f'\n{NitroCode}')
        DiscordValidFile.close()
        DiscordInvalidFile.close()
        print(f'\n{Fore.BLACK}INFO | {Fore.WHITE}Checked {DiscordNitroCheckerAmount} codes')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
    except FileNotFoundError:
        print(f'\n{Fore.RED}ERROR | {Fore.WHITE}This file does not exist')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
    except ValueError as NitroCheckerValueError:
        print(f'\n{Fore.RED}ERROR | {Fore.WHITE}Invalid option, {NitroCheckerValueError}')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
    except Exception as NitroCheckerException:
        print(f'\n{Fore.RED}ERROR | {Fore.WHITE}Something went wrong, {NitroCheckerException}')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
#Discord Menu > Token Generator
def DiscordTokenGenerator():
    os.system('title PURO TOOLKIT 0.1 - Discord Menu > Token Generator')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Menu > Token Generator                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    try:
        print(f'{Fore.YELLOW}WARN | {Fore.WHITE}Mostly of the tokens will be invalid, so generating a working token is very hard.{Fore.WHITE}')
        DiscordTokenGeneratorAmount = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Amount: '))
        DiscordTokenGeneratorLength = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Length (Default: 70): '))
        DiscordTokenGeneratorFileName = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}File Name (Without .txt): ')
        print()
        value = 1
        DiscordTokenFile = open(f'{DiscordTokenGeneratorFileName}.txt', 'w')
        DiscordTokenFile.write(f'{DiscordTokenGeneratorAmount} Discord Tokens with a length of {DiscordTokenGeneratorLength} characters | Generated with PuroToolKit')
        while value <= DiscordTokenGeneratorAmount:
            code = ('').join(random.choices(string.ascii_letters + string.digits, k=DiscordTokenGeneratorLength))
            print(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}{code}')
            DiscordTokenFile.write(f'\n{code}')
            value += 1
        DiscordTokenFile.close()
        print(f'\n{Fore.BLACK}INFO | {Fore.WHITE}Generated {DiscordTokenGeneratorAmount} tokens with a length of {DiscordTokenGeneratorLength} characters')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
    except ValueError:
        print(f'\n{Fore.RED}ERROR | {Fore.WHITE}Invalid amount')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
#Discord Menu > Token Info
def DiscordTokenInfo():
    os.system('title PURO TOOLKIT 0.1 - Discord Menu > Token to Account Info')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Menu > Token to Account Info                  {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    TokenInfoToken = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Token: ')
    headers = {'Authorization': TokenInfoToken, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        verified = r.json()['verified']
        print(f'\n{Fore.BLACK}INFO | {Fore.WHITE}User: {userName}')
        print(f'{Fore.BLACK}INFO | {Fore.WHITE}ID: {userID}')
        print(f'{Fore.BLACK}INFO | {Fore.WHITE}Phone: {phone}')
        print(f'{Fore.BLACK}INFO | {Fore.WHITE}Email: {email}')
        print(f'{Fore.BLACK}INFO | {Fore.WHITE}MFA: {mfa}')
        print(f'{Fore.BLACK}INFO | {Fore.WHITE}Verified: {verified}')
        print(f'{Fore.BLACK}INFO | {Fore.WHITE}Token: {TokenInfoToken}')
        print(f'\n{Fore.BLACK}INFO | {Fore.WHITE}Info generated')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
    else:
        print(f'\n{Fore.RED}ERROR | {Fore.WHITE}Invalid Token')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
#Discord Menu > Token from Email/Password
def DiscordTokenEmailPass():
    os.system('title PURO TOOLKIT 0.1 - Discord Menu > Email/Password to Token')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Discord Menu > Email/Password to Token                {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    TokenFromEmail = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Email: ')
    TokenFromPassword = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Password: ')
    data={'email': TokenFromEmail, 'password': TokenFromPassword, 'undelete': 'false'}
    headers={'content-type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
    r = requests.post('https://discord.com/api/v8/auth/login', json=data, headers=headers)
    if r.status_code == 200:
        token = r.json()['token']
        print(f'\n{Fore.WHITE}TOKEN: {token}')
        print(f'\n{Fore.BLACK}INFO |  {Fore.WHITE}Token generated')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
        os.system('cls; clear')
    elif 'PASSWORD_DOES_NOT_MATCH' in r.text:
        print(f'\n{Fore.RED}ERROR |   {Fore.WHITE}Invalid password')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
    elif 'captcha-required' in r.text:
        print(f'\n{Fore.YELLOW}ERROR | {Fore.WHITE}Returned captcha')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
    else:
        print(f'\n{Fore.RED}ERROR |   {Fore.WHITE}Invalid email or password')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
#Discord Menu > HalfToken
def DiscordHalfToken():
    os.system('title PURO TOOLKIT 0.1 - Discord Menu > Half Token from user ID')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Discord Menu > User ID to Half Token                  {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    userid = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}UserID: ')
    string_b = f'{userid}'.encode('utf')
    bas64_bytes = base64.b64encode(string_b)
    HalfTokenGen = bas64_bytes.decode('utf-8')
    print(f'\n{Fore.WHITE}Half Token: {HalfTokenGen}')
    print(f'\n{Fore.BLACK}INFO |  {Fore.WHITE}Half token generated')
    input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
    DiscordMenu()
#Discord Menu > WebHook Spammer
def DiscordWebhookSpammer():
    os.system('title PURO TOOLKIT 0.1 - Discord Menu > Webhook Spammer')
    os.system('cls')
    
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Discord Menu > Webhook Spammer                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    try:
        WebhookSpammerWebhook = input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Webhook: ')
        WebhookSpammerMessage = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Message: ')
        WebhookSpammerAmount = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Amount: '))
        print()
        for i in range(WebhookSpammerAmount):
            _data = requests.post(WebhookSpammerWebhook, json={'content': WebhookSpammerMessage}, headers={'Content-Type': 'application/json'})
            if _data.status_code < 400:
                print(f'{Fore.GREEN}INFO | {Fore.WHITE}Message sent')
            else:
                print(f"{Fore.RED}ERROR | {Fore.WHITE}Message not sent")
        print(f'\n{Fore.BLACK}INFO |  {Fore.WHITE}Sent {WebhookSpammerAmount} messages')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
    except:
        print(f"\n{Fore.RED}ERROR |  {Fore.WHITE}Couldn't spam Webhook")
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
#Discord Menu > Webhook Deleter
def DiscordWebhookDeleter():
    os.system('title PURO TOOLKIT 0.1 - Discord Menu > Webhook Deleter')
    os.system('cls')  
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Discord Menu > Webhook Deleter                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    try:
        WebhookDeleterWebhook = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Webhook: ')
        requests.delete(WebhookDeleterWebhook.rstrip())
        print(f'\n{Fore.BLACK}INFO |  {Fore.WHITE}Webhook deleted')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
    except:
        print(f"\n{Fore.RED}ERROR |  {Fore.WHITE}Couldn't delete Webhook")
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
#Discord Menu > Change Hypesquad House
def DiscordHypesquadHouse():
    os.system('title PURO TOOLKIT 0.1 - Discord Menu > Hypesquad House')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Discord Menu > Hypesquad House                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} 1 | Bravery                                           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 2 | Brilliance                                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 3 | Balance                                           {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    try:
        ChangeHypesquadHouseHouse = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
        ChangeHypesquadHouseToken = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Token: ')
        headers = {'Authorization': ChangeHypesquadHouseToken, 'Content-Type': 'application/json'}  
        r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
        if r.status_code == 200:
            headers = {
                'Authorization': ChangeHypesquadHouseToken,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
            }
        if ChangeHypesquadHouseHouse == '1':
            payload = {'house_id': 1}
        elif ChangeHypesquadHouseHouse == '2':
            payload = {'house_id': 2}
        elif ChangeHypesquadHouseHouse == '3':
            payload = {'house_id': 3}
        r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
        if r.status_code == 204:
            print(f'\n{Fore.BLACK}INFO |  {Fore.WHITE}House changed')
            input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordMenu()
    except:
        print(f'\n{Fore.RED}ERROR |  {Fore.WHITE}Invalid token')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()
#Discord Menu 2 > Disable Token
def DiscordDisableToken():
    os.system('title PURO TOOLKIT 0.1 - Discord Menu > Token Disabler')
    os.system('cls')
    
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Discord Menu > Token Disabler                         {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    
    disabletokentoken = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Token: ')
    headers = {'Authorization': disabletokentoken, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        r = requests.patch('https://discordapp.com/api/v8/users/@me', headers={'Authorization': disabletokentoken}, json={'date_of_birth': '2015-7-16'})
        if r.status_code == 400:
            print(f'\n{Fore.BLACK}INFO |  {Fore.WHITE}Token disabled')
            input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu 2')
            DiscordMenu2()
        else:
            print(f'\n{Fore.RED}ERROR |  {Fore.WHITE}Invalid token')
            input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu 2')
            DiscordMenu2()
    else:
        print(f'\n{Fore.RED}ERROR |  {Fore.WHITE}Invalid token')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu 2')
        DiscordMenu2()
#Network Menu > LocalChatServer
def LocalChatServer():
    os.system('title PURO TOOLKIT 0.1 - Misc Local Chat Server')
    os.system('cls')
    
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Network Menu > Local Chat Server                      {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    # Server Data
    host = 'localhost'
    port = 55555
    # Starting Server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    # Lists For Clients and Their Nicknames
    clients = []
    nicknames = []
    # Sending Messages To All Connected Clients
    def broadcast(message):
        for client in clients:
            client.send(message)
    # Handling Messages From Clients
    def handle(client):
        while True:
            try:
                # Broadcasting Messages
                message = client.recv(1024)
                broadcast(message)
            except:
                # Removing And Closing Clients
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast('{} left!'.format(nickname).encode('utf-8'))
                nicknames.remove(nickname)
                break
    # Receiving / Listening Function
    def receive():
        while True:
            # Accept Connection
            client, address = server.accept()
            print(f'{Fore.BLUE}INFO | {Fore.WHITE}Client Connection with {address}')
            # Request And Store Nickname
            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            nicknames.append(nickname)
            clients.append(client)
            # Print And Broadcast Nickname
            print(f'{Fore.BLUE}INFO | {Fore.WHITE}Client Username: {nickname}')
            client.send(f'{Fore.BLUE}INFO | {Fore.WHITE}Connected to server!'.encode('utf-8'))
            broadcast(f'\n{Fore.BLUE}INFO | {Fore.WHITE}{nickname} joined!'.encode('utf-8'))
            # Start Handling Thread For Client
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
    receive()
#Network Menu > LocalChatClient
def LocalChatClient():
    os.system('title PURO TOOLKIT 0.1 - Network Menu > Local Chat Client')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Network Menu > Local Chat Client                      {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    # Choosing Nickname
    nickname = input(f"{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Username: ")
    # Connecting To Server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 55555))
    # Listening to Server and Sending Nickname
    def receive():
        while True:
            try:
                # Receive Message From Server
                # If 'NICK' Send Nickname
                message = client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    client.send(nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                # Close Connection When Error
                print(f"{Fore.RED}ERROR | {Fore.WHITE}An error ocurred")
                client.close()
                break
    # Sending Messages To Server
    def write():
        while True:
            message = '{}{}: {}'.format(f"{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}", nickname, input(''))
            client.send(message.encode('utf-8'))
    # Starting Threads For Listening And Writing
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    write_thread = threading.Thread(target=write)
    write_thread.start()
    write()
#Network Menu > PortScanner
def PortScanner():
    os.system('title PURO TOOLKIT 0.1 - Network Menu > Port Scanner')
    os.system('cls')
    
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Network Menu > Port Scanner                           {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝')#--------------------║

    try:
        PortScannerIP = input(f"\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Target IP: ")
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
        PortScannerClosed = input(f"{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Show Closed/Filtered ports? (y/n): ")
        PortScannerMaxWorkers = int(input(f"{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Max Workers (Default: 100): "))
        PortScannerClosedPorts = 0
        PortScannerOpenPorts = 0
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
                    if PortScannerClosed == "y":
                        print(f"{Fore.RED}CLOSED/FILTERED | {Fore.WHITE}{PortScannerPort}")
        with concurrent.futures.ThreadPoolExecutor(max_workers=PortScannerMaxWorkers) as executor:
            for PortScannerPort in range(PortScannerMinPort, PortScannerMaxPort + 1):
                executor.submit(PortScannerScan, PortScannerIP, PortScannerPort)
        print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Scanned {PortScannerTotalPorts} ports')
        print(f'{Fore.BLUE}INFO | {Fore.WHITE}{PortScannerOpenPorts} Open Ports: {PortScannerOpenPortsList}')
        print(f'{Fore.BLUE}INFO | {Fore.WHITE}{PortScannerClosedPorts} Closed/Filtered Ports')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Misc Menu')
        MiscMenu()
    except ValueError:
        print(f'\n{Fore.RED}ERROR | {Fore.WHITE}Invalid amount')
        input(f'\n{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
        DiscordMenu()

MainMenu()