################################################
#
#   Scraper made by LizardX2 
#
#   contact for issues or improvements;
#
#   Telegram: @LizardX2 link: t.me/LizardX2
#
#################################################
import os
from colorama import *
from googlesearch import *

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

valid_syntax = ["inurl", "site", "or"]
valid_domain = ['aero', 'asia', 'biz', 'cat', 'com', 'coop', 'info', 'int', 'jobs', 'mobi', 'museum', 'name', 'net', 'org', 'pro', 'tel', 'travel', 'xxx', 'edu', 'gov', 'mil', 'ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bm', 'bn', 'bo', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cs', 'cu', 'cv', 'cx', 'cy', 'cz', 'dd', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'ss', 'st', 'su', 'sv', 'sy', 'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'ye', 'yt', 'yu', 'za', 'zm', 'zw']

clear()
print(f"{Fore.LIGHTYELLOW_EX}LIZARD SCRAPER v0.1 | {Fore.LIGHTBLACK_EX}by @LizardX2{Fore.RESET}\n")
searchSite = input(str(f"{Fore.YELLOW}Choose a Domain > {Fore.RESET}"))
searchTerm = input(str(f"{Fore.YELLOW}Choose a term to scrape (case sensitive) > {Fore.RESET}"))
syntax = input(str(f"{Fore.YELLOW}Choose the syntax (inurl, site, or) > {Fore.RESET}"))

def Error():
    print(f"{Fore.RED}\nERROR! Syntax not valid{Fore.RESET}")
    exit()

def Check():
    if searchSite.count(".") >= 2:
        static = "IP"
    else:
        static = "Site"
        domain_parts = searchSite.split(".")
        if syntax in valid_syntax and domain_parts[-1] in valid_domain:
            pass
        else:
            Error()
    return static

def Scraper():
    date = input(f"{Fore.YELLOW}Set date parameters? (format xx/xx/xxxx) Y/N > {Fore.RESET}")
    if date.lower() == "y":
        fromDate = input(f"\n{Fore.CYAN}First date parameter (FROM) > {Fore.RESET}")
        toDate = input(f"{Fore.CYAN}Second date parameter (TO) > {Fore.RESET}")
    elif date.lower() == "n":
        pass
    clear()
    print(f"{Fore.LIGHTBLUE_EX}Settings>>> {Check()}: {Fore.LIGHTBLACK_EX}{searchSite}{Fore.RESET}{Fore.LIGHTBLUE_EX} | Term: {Fore.LIGHTBLACK_EX}{searchTerm}{Fore.RESET}{Fore.LIGHTBLUE_EX} |Syntax: {Fore.LIGHTBLACK_EX}{syntax}{Fore.RESET}")
    print(f"{Fore.LIGHTBLUE_EX}\nSCRAPING...\n{Fore.RESET}")
    scraping = f"{syntax.lower()}:{searchSite} {searchTerm}"

    if date.lower() == "y":
        for _ in search(scraping, tld="com", num=99999999, stop=200, pause=0, tbs=f"cdr:1,cd_min:{fromDate},cd_max:{toDate}"):
            print(f"{Fore.GREEN}[+] {_}{Fore.RESET}")
            if _ not in open("logs.txt", "r").read():
                logs = open("logs.txt", "a")
                logs.write(_ + "\n")
                logs.close()
    elif date.lower() == "n":
        for _ in search(scraping, tld="com", num=99999999, stop=200, pause=0):
            print(f"{Fore.GREEN}[+] {_}{Fore.RESET}")
            if _ not in open("logs.txt", "r").read():
                logs = open("logs.txt", "a")
                logs.write(_ + "\n")
                logs.close()
    else:
        Error()
    
    quit = input(f"\n{Fore.LIGHTYELLOW_EX}[!]{Fore.RESET} {Fore.RED}PRESS ENTER TO EXIT{Fore.RESET}")
Check()
Scraper()