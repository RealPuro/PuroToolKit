from colorama import *
from pypresence import Presence
from itertools import cycle
import os, requests, random, string, base64, threading, socket, webbrowser, concurrent.futures, sys, time, discord
Version = "1.0.0"
os.system(f'title Puro Toolkit {Version} - Rich Presence')
os.system('cls')
DiscordRichPresence = input(f'{Style.BRIGHT}{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Enable Discord Rich Presence? (Y/N): ')
if DiscordRichPresence == "y" or DiscordRichPresence == "Y":
    try:
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
    except ValueError as ValueErrorOutput:
        print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Menu')
    except KeyboardInterrupt:
        print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
        input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Menu')
    except Exception as ExceptionOutput:
        print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
        input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Menu')
def Menu():
    os.system(f'title Puro Toolkit {Version} - Menu')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Menu                                                  {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} 1 | Credits                                           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 2 | Discord Tools                                     {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 3 | Network Tools                                     {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 4 | Miscellaneous Tools                               {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 0 | Exit                                              {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            MenuChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
            if MenuChoice == 1:
                Credits()
            elif MenuChoice == 2:
                DiscordTools()
            elif MenuChoice == 3:
                NetworkTools()
            elif MenuChoice == 4:
                MiscellaneousTools()
            elif MenuChoice == 0:
                sys.exit()
            else:
                print(f'{Fore.RED}ERROR | {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Menu')
            Menu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def Credits():
    os.system(f'title Puro Toolkit {Version} - Credits')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Credits                                               {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Made By: Puro#9999                                    {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} Version: {Version}                                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} 1 | GitHub                                            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 2 | YouTube                                           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 0 | Menu                                              {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            CreditsMenuChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
            if CreditsMenuChoice == 1:
                webbrowser.open_new("https://github.com/RealPuro")
            elif CreditsMenuChoice == 2:
                webbrowser.open_new("https://www.youtube.com/channel/UCBqqNNYO5ku5gNgGuf41DLw")
            elif CreditsMenuChoice == 0:
                Menu()
            else:
                print(f'{Fore.RED}ERROR |  {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Credits Menu')
            Credits()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordTools():
    os.system(f'title Puro Toolkit {Version} - Discord Tools')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Tools                                         {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} 1 | Generator/Checker Tools                           {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 2 | Info Gathering Tools                              {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 3 | Account Tools                                     {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 4 | Webhook Tools                                     {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 5 | Account Nuking Tools (WIP)                        {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 6 | Server Nuking Tools (WIP)                         {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 0 | Menu                                              {Fore.BLACK}║')
    print(f'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordMenuChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
            if DiscordMenuChoice == 1:
                DiscordGeneratorCheckerTools()
            elif DiscordMenuChoice == 2:
                DiscordInfoGatheringTools()
            elif DiscordMenuChoice == 3:
                DiscordAccountTools()
            elif DiscordMenuChoice == 4:
                DiscordWebhookTools()
            elif DiscordMenuChoice == 0:
                Menu()
            else:
                print(f'{Fore.RED}ERROR | {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Menu')
            Menu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordGeneratorCheckerTools():
    os.system(f'title Puro Toolkit {Version} - Discord Tools - Generator/Checker Tools')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Tools - Generator/Checker Tools               {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} 1 | Nitro Generator                                   {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 2 | Nitro Checker                                     {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 3 | Token Generator                                   {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 4 | Token Checker (WIP)                               {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 5 | More (WIP)                                        {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 0 | Discord Menu                                      {Fore.BLACK}║')
    print(f'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordGeneratorCheckerToolsChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
            if DiscordGeneratorCheckerToolsChoice == 1:
                DiscordNitroGenerator()
            elif DiscordGeneratorCheckerToolsChoice == 2:
                DiscordNitroChecker()
            elif DiscordGeneratorCheckerToolsChoice == 3:
                DiscordTokenGenerator()
            elif DiscordGeneratorCheckerToolsChoice == 0:
                DiscordTools()
            else:
                print(f'{Fore.RED}ERROR | {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordInfoGatheringTools():
    os.system(f'title Puro Toolkit {Version} - Discord Tools - Info Gathering Tools')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Tools - Info Gathering Tools                  {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} 1 | Email/Password to Token                           {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 2 | User ID to Half Token                             {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 3 | Token to Account Info                             {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 4 | More (WIP)                                        {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 0 | Discord Menu                                      {Fore.BLACK}║')
    print(f'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordInfoGatheringToolsChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
            if DiscordInfoGatheringToolsChoice == 1:
                DiscordEmailPasswordToToken()
            elif DiscordInfoGatheringToolsChoice == 2:
                DiscordUserIdToHalfToken()
            elif DiscordInfoGatheringToolsChoice == 3:
                DiscordTokenToAccountInfo()
            elif DiscordInfoGatheringToolsChoice == 0:
                DiscordTools()
            else:
                print(f'{Fore.RED}ERROR | {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordAccountTools():
    os.system(f'title Puro Toolkit {Version} - Discord Tools - Account Tools')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Tools - Account Tools                          {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} 1 | Token Unverifier                                  {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 2 | Token Disabler                                    {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 3 | Token Troller                                     {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 4 | Hypesquad House Changer                           {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 5 | More (WIP)                                        {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 0 | Discord Menu                                      {Fore.BLACK}║')
    print(f'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordAccountToolsChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
            if DiscordAccountToolsChoice == 1:
                DiscordTokenUnverifier()
            elif DiscordAccountToolsChoice == 2:
                DiscordTokenDisabler()
            elif DiscordAccountToolsChoice == 3:
                DiscordTokenTroller()
            elif DiscordAccountToolsChoice == 4:
                DiscordHypesquadHouseChanger()
            elif DiscordAccountToolsChoice == 0:
                DiscordTools()
            else:
                print(f'{Fore.RED}ERROR | {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordWebhookTools():
    os.system(f'title Puro Toolkit {Version} - Discord Tools - Webhook Tools')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Discord Tools - Webhook Tools                         {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} 1 | Webhook Sender                                    {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 2 | Webhook Editer (WIP)                              {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 3 | Webhook Deleter                                   {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 4 | More (WIP)                                        {Fore.BLACK}║')
    print(f'{Fore.BLACK}║{Fore.WHITE} 0 | Discord Menu                                      {Fore.BLACK}║')
    print(f'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordWebhookToolsChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
            if DiscordWebhookToolsChoice == 1:
                DiscordWebhookSender()
            elif DiscordWebhookToolsChoice == 3:
                DiscordWebhookDeleter()
            elif DiscordWebhookToolsChoice == 0:
                DiscordTools()
            else:
                print(f'{Fore.RED}ERROR | {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordNitroGenerator():
    os.system(f'title Puro Toolkit {Version} - Generator/Checker Tools - Nitro Generator')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Generator/Checker Tools - Nitro Generator             {Fore.BLACK}║')
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
            DiscordGeneratorCheckerTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordNitroChecker():
    os.system(f'title Puro Toolkit {Version} - Generator/Checker Tools - Nitro Checker')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Generator/Checker Tools - Nitro Checker               {Fore.BLACK}║')
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
            DiscordGeneratorCheckerTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordTokenGenerator():
    os.system(f'title Puro Toolkit {Version} - Generator/Checker Tools - Token Generator')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Generator/Checker Tools - Token Generator             {Fore.BLACK}║')
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
            DiscordGeneratorCheckerTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordEmailPasswordToToken():
    os.system(f'title Puro Toolkit {Version} - Info Gathering Tools - Email/Password to Token')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Info Gathering Tools - Email/Password to Token        {Fore.BLACK}║')
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
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordInfoGatheringTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordUserIdToHalfToken():
    os.system(f'title Puro Toolkit {Version} - Info Gathering Tools - Half Token from user ID')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Info Gathering Tools - User ID to Half Token          {Fore.BLACK}║')
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
            DiscordInfoGatheringTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordTokenToAccountInfo():
    os.system(f'title Puro Toolkit {Version} - Info Gathering Tools - Token to Account Info')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Info Gathering Tools - Token to Account Info          {Fore.BLACK}║')
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
            DiscordInfoGatheringTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordTokenUnverifier():
    os.system(f'title Puro Toolkit {Version} - Account Tools - Token Unverifier')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Account Tools - Token Unverifier                      {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordTokenUnverifierToken = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Token: ')
            headers = {'Authorization': DiscordTokenUnverifierToken, 'Content-Type': 'application/json'} 
            r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
            if r.status_code == 200:
                r = requests.post('https://discordapp.com/api/v8/users/@me/relationships', headers={'Authorization': DiscordTokenUnverifierToken, 'User-Agent': 'discordbot'}, json={'username': 'LMAO', 'discriminator': 6572})
                if r.status_code == 204:
                    print(f'{Fore.BLUE}INFO |  {Fore.WHITE}Token unverified')
                else:
                    print(f'{Fore.RED}ERROR |  {Fore.WHITE}Token not unverified')
            else:
                print(f'{Fore.RED}ERROR |  {Fore.WHITE}Invalid token')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu 2')
            DiscordAccountTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordTokenDisabler():
    os.system(f'title Puro Toolkit {Version} - Account Tools - Token Disabler')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Account Tools - Token Disabler                        {Fore.BLACK}║')
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
                    print(f'{Fore.RED}ERROR |  {Fore.WHITE}Token not disabled')
            else:
                print(f'{Fore.RED}ERROR |  {Fore.WHITE}Invalid token')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu 2')
            DiscordAccountTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordTokenTroller():
    os.system(f'title Puro Toolkit {Version} - Account Tools - Token Troller')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Account Tools - Token Troller                         {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordTokenTrollerToken = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Token: ')
            DiscordTokenTrollerAmount = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Amount: '))
            DiscordTokenTrollerModes = cycle(["light", "dark"])
            headers = {'Authorization': DiscordTokenTrollerToken, 'Content-Type': 'application/json'}  
            for i in range(DiscordTokenTrollerAmount):
                time.sleep(0.15)
                setting = {'theme': next(DiscordTokenTrollerModes)}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
            print(f'{Fore.BLUE}INFO |  {Fore.WHITE}Token Trolled')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu 2')
            DiscordAccountTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordHypesquadHouseChanger():
    os.system(f'title Puro Toolkit {Version} - Account Tools - Hypesquad House Changer')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Account Tools - Hypesquad House Changer              {Fore.BLACK}║')
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
            DiscordAccountTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordWebhookSender():
    os.system(f'title Puro Toolkit {Version} - Webhook Tools - Webhook Sender')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Webhook Tools - Webhook Sender                        {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            DiscordWebhookSenderWebhook = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Webhook: ')
            DiscordWebhookSenderMessage = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Message: ')
            DiscordWebhookSenderAmount = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Amount: '))
            for i in range(DiscordWebhookSenderAmount):
                requests.post(DiscordWebhookSenderWebhook, json={'content': DiscordWebhookSenderMessage}, headers={'Content-Type': 'application/json'})
            print(f'{Fore.BLUE}INFO | {Fore.WHITE}Sent {DiscordWebhookSenderAmount} messages')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Discord Menu')
            DiscordWebhookTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def DiscordWebhookDeleter():
    os.system(f'title Puro Toolkit {Version} - Webhook Tools - Webhook Deleter')
    os.system('cls')  
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Webhook Tools - Webhook Deleter                       {Fore.BLACK}║')
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
            DiscordWebhookTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def NetworkTools():
    os.system(f'title Puro Toolkit {Version} - Network Tools')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Network Tools                                         {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} 1 | Local Chat Server                                 {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 2 | Local Chat Client                                 {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 3 | Port Scanner                                      {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 0 | Menu                                              {Fore.BLACK}║')
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
                Menu()
            else:
                print(f'{Fore.RED}ERROR | {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Menu')
            Menu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def NetworkLocalChatServer():
    os.system(f'title Puro Toolkit {Version} - Network Tools - Local Chat Server')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Network Tools - Local Chat Server                     {Fore.BLACK}║')
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
            NetworkTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Network Menu - LocalChatClient
def NetworkLocalChatClient():
    os.system(f'title Puro Toolkit {Version} - Network Tools - Local Chat Client')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} Network Tools - Local Chat Client                     {Fore.BLACK}║')
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
            NetworkTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
#Network Menu - PortScanner
def NetworkPortScanner():
    os.system(f'title Puro Toolkit {Version} - Network Tools - Port Scanner')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Network Tools - Port Scanner                          {Fore.BLACK}║')
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
                        if PortScannerClosed == "y" or PortScannerClosed == "Y":
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
            NetworkTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def MiscellaneousTools():
    os.system(f'title Puro Toolkit {Version} - Miscellaneous Tools')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Miscellaneous Tools                                   {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(F'{Fore.BLACK}║{Fore.WHITE} 1 | Password Generator                                {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE} 0 | Menu                                              {Fore.BLACK}║')
    print(F'{Fore.BLACK}╚═══════════════════════════════════════════════════════╝\n')#------------------║
    while True:
        try:
            MiscMenuChoice = int(input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Option: '))
            if MiscMenuChoice == 1:
                MiscellaneousPasswordGenerator()
            elif MiscMenuChoice == 0:
                Menu()
            else:
                print(f'{Fore.RED}ERROR |  {Fore.WHITE}Please select a valid option')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Misc Menu')
            Menu()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
def MiscellaneousPasswordGenerator():
    os.system(f'title Puro Toolkit {Version} - Miscellaneous Tools - Password Generator')
    os.system('cls')
    print(F'{Style.BRIGHT}{Fore.BLACK}╔═══════════════════════════════════════════════════════╗')#------║
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╔═╗╦ ╦╦═╗╔═╗  ╔╦╗╔═╗╔═╗╦  ╦╔═╦╔╦╗           {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╠═╝║ ║╠╦╝║ ║   ║ ║ ║║ ║║  ╠╩╗║ ║            {Fore.BLACK}║')
    print(F'{Fore.BLACK}║{Fore.WHITE}           ╩  ╚═╝╩╚═╚═╝   ╩ ╚═╝╚═╝╩═╝╩ ╩╩ ╩            {Fore.BLACK}║')
    print(F'{Fore.BLACK}╠═══════════════════════════════════════════════════════╣')#--------------------║
    print(f'{Fore.BLACK}║{Fore.WHITE} Miscellaneous Tools - Password Generator              {Fore.BLACK}║')
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
            if MiscellaneousPasswordGeneratorDigits == "y" or MiscellaneousPasswordGeneratorSave == "Y":
                MiscellaneousPasswordGeneratorCharacters += string.digits
            if MiscellaneousPasswordGeneratorLowercaseLetters == "y" or MiscellaneousPasswordGeneratorSave == "Y":
                MiscellaneousPasswordGeneratorCharacters += string.ascii_lowercase
            if MiscellaneousPasswordGeneratorUppercaseLetters == "y" or MiscellaneousPasswordGeneratorSave == "Y":
                MiscellaneousPasswordGeneratorCharacters += string.ascii_uppercase
            if MiscellaneousPasswordGeneratorSpecialCharacters == "y" or MiscellaneousPasswordGeneratorSave == "Y":
                MiscellaneousPasswordGeneratorCharacters += string.punctuation
            if MiscellaneousPasswordGeneratorSave == "y" or MiscellaneousPasswordGeneratorSave == "Y":
                MiscellaneousPasswordGeneratorFileName = input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}File Name (Without .txt): ')
                MiscellaneousPasswordGeneratorFile = open(f'{MiscellaneousPasswordGeneratorFileName}.txt', 'w')
                MiscellaneousPasswordGeneratorFile.write(f'{MiscellaneousPasswordGeneratorAmount} passwords with a length of {MiscellaneousPasswordGeneratorLength} characters | Generated with PuroToolKit')
            for i in range(MiscellaneousPasswordGeneratorAmount):
                password = ('').join(random.choices(MiscellaneousPasswordGeneratorCharacters, k=MiscellaneousPasswordGeneratorLength))
                print(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}{password}')
                if MiscellaneousPasswordGeneratorSave == "y" or MiscellaneousPasswordGeneratorSave == "Y":
                    MiscellaneousPasswordGeneratorFile.write(f'\n{password}')
            if MiscellaneousPasswordGeneratorSave == "y" or MiscellaneousPasswordGeneratorSave == "Y":
                MiscellaneousPasswordGeneratorFile.close()
            print(f'{Fore.BLUE}INFO | {Fore.WHITE}Generated {MiscellaneousPasswordGeneratorAmount} codes with a length of {MiscellaneousPasswordGeneratorLength} characters')
        except ValueError as ValueErrorOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Please enter a valid input ({ValueErrorOutput})')
        except KeyboardInterrupt:
            print(f'\n{Fore.BLUE}INFO | {Fore.WHITE}Keyboard Interrupt issued')
            input(f'{Fore.BLACK}PURO TOOLKIT | {Fore.WHITE}Press Enter to return to Misc Menu')
            MiscellaneousTools()
        except Exception as ExceptionOutput:
            print(f'{Fore.RED}ERROR | {Fore.WHITE}Something went wrong ({ExceptionOutput})')
Menu()