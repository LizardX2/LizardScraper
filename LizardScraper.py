################################################
#
#   Scraper made by LizardX2 
#
#   contact for issues or improvements;
#
#   Telegram: @LizardX2 link: t.me/LizardX2
#
#################################################

import os,validators
from colorama import *
from googlesearch import *

def clear():
    if os.name == 'nt': os.system("cls")
    else: os.system("clear")

clear()
print(f"{Fore.LIGHTYELLOW_EX}LIZARD SCRAPER v0.1 | {Fore.LIGHTBLACK_EX}by @LizardX2{Fore.RESET}\n")

searchSite = input(f"{Fore.YELLOW}Choose a Domain > {Fore.RESET}").lower()
searchTerm = input(f"{Fore.YELLOW}Choose a term to scrape (case sensitive) > {Fore.RESET}")
syntax = input(f"{Fore.YELLOW}Choose the syntax (inurl, site, or) > {Fore.RESET}").lower()
date = input(f"{Fore.YELLOW}Set date parameters? (format xx/xx/xxxx) Y/N > {Fore.RESET}")
if date.lower() == "y":
    fromDate = input(f"\n{Fore.CYAN}First date parameter (FROM) > {Fore.RESET}")
    toDate = input(f"{Fore.CYAN}Second date parameter (TO) > {Fore.RESET}")
    tbs_setting =f"cdr:1,cd_min:{fromDate},cd_max:{toDate}"
else:
    tbs_setting = "0"

def Scraper():

    if syntax not in ["inurl", "site", "or"] or validators.domain(searchSite) != True:
        input(f"{Fore.RED}\nERROR! Syntax not valid{Fore.RESET}")
        exit()
    
    clear()
    print(f"{Fore.LIGHTBLUE_EX}Settings: {Fore.LIGHTBLACK_EX}{searchSite}{Fore.RESET}{Fore.LIGHTBLUE_EX} | Term: {Fore.LIGHTBLACK_EX}{searchTerm}{Fore.RESET}{Fore.LIGHTBLUE_EX} | Syntax: {Fore.LIGHTBLACK_EX}{syntax}{Fore.RESET}")
    print(f"{Fore.LIGHTBLUE_EX}\nSCRAPING...\n{Fore.RESET}")

    scraping = f"{syntax}:{searchSite} {searchTerm}"

    for result in search(scraping, tbs=tbs_setting):
        print(f"{Fore.GREEN}[+] {result}{Fore.RESET}")
        if result not in open("logs.txt", "r").read():
            logs = open("logs.txt", "a")
            logs.write(result + "\n")
            logs.close()
    
    input(f"\n{Fore.LIGHTYELLOW_EX}[!]{Fore.RESET} {Fore.RED}PRESS ENTER TO EXIT{Fore.RESET}")

Scraper()