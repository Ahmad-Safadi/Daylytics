from colorama import Fore, Style, init
init(autoreset=True)

def progress_bar(percent, length=25):
    filled = int(length * percent / 100)
    return f"[{Fore.CYAN}{'█' * filled}{Style.RESET_ALL}{' ' * (length - filled)}]"

#====================================#
print(f"{Fore.LIGHTRED_EX}📉 Enter bad activities (name and hours). Type 'done' when finished:{Style.RESET_ALL}")

Day = 24
bad = {}

while Day > 0:
    name = input(f"{Fore.RED}Bad activity name: {Style.RESET_ALL}").strip()
    if name.lower() == 'done':
        break

    try:
        hours = float(input(f"{Fore.YELLOW}Hours for '{name}': {Style.RESET_ALL}"))

        if hours <= 0:
            print(f"{Fore.RED}Please enter a positive number.{Style.RESET_ALL}")
            continue
        if hours > Day:
            print(f"{Fore.RED}Not enough remaining hours. You only have {Day} hour(s) left.{Style.RESET_ALL}")
            continue

        bad[name] = hours
        Day -= hours
        print(f"{Fore.CYAN}Remaining hours: {Day}{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter a valid number.{Style.RESET_ALL}")
        continue

print(f"\n{Fore.LIGHTRED_EX}📋 Summary of bad activities:{Style.RESET_ALL}")
for activity, hrs in bad.items():
    print(f"{Fore.RED}- {activity}: {hrs} hour(s){Style.RESET_ALL}")
print(f"{Fore.RED}Total bad hours: {sum(bad.values())}h{Style.RESET_ALL}")
print(f"{Fore.GREEN}Remaining available hours: {Day}h{Style.RESET_ALL}")

#====================================#
print(f"\n{Fore.LIGHTGREEN_EX}📈 Enter good activities (name and hours). Type 'done' when finished:{Style.RESET_ALL}")

good = {}

while Day > 0:
    name = input(f"{Fore.GREEN}Good activity name: {Style.RESET_ALL}").strip()
    if name.lower() == 'done':
        break

    try:
        hours = float(input(f"{Fore.YELLOW}Hours for '{name}': {Style.RESET_ALL}"))

        if hours <= 0:
            print(f"{Fore.RED}Please enter a positive number.{Style.RESET_ALL}")
            continue
        if hours > Day:
            print(f"{Fore.RED}Not enough remaining hours. You only have {Day} hour(s) left.{Style.RESET_ALL}")
            continue

        good[name] = hours
        Day -= hours
        print(f"{Fore.CYAN}Remaining hours: {Day}{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter a valid number.{Style.RESET_ALL}")
        continue

print(f"\n{Fore.LIGHTGREEN_EX}📋 Summary of good activities:{Style.RESET_ALL}")
for activity, hrs in good.items():
    print(f"{Fore.GREEN}- {activity}: {hrs} hour(s){Style.RESET_ALL}")
print(f"{Fore.GREEN}Total good hours: {sum(good.values())}h{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Unallocated remaining hours: {Day}h{Style.RESET_ALL}")

#====================================#
print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
print(f"{Fore.LIGHTCYAN_EX}📊 DAILY ACTIVITY ANALYSIS 📊{Style.RESET_ALL}")
print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")

#====================================#
bad_total = sum(bad.values())
good_total = sum(good.values())

#====================================#
print(f"\n{Fore.LIGHTRED_EX}❌ Bad Activities:{Style.RESET_ALL}")
for name, h in sorted(bad.items(), key=lambda x: x[1], reverse=True):
    p = (h / bad_total) * 100 if bad_total else 0
    print(f"{Fore.RED}- {name.ljust(25)} {Fore.YELLOW}{p:.1f}% {progress_bar(p)} {Fore.WHITE}({h}h){Style.RESET_ALL}")
print(f"{Fore.RED}Total Bad: {bad_total}h{Style.RESET_ALL}")

print(f"\n{Fore.LIGHTGREEN_EX}✅ Good Activities:{Style.RESET_ALL}")
for name, h in sorted(good.items(), key=lambda x: x[1], reverse=True):
    p = (h / good_total) * 100 if good_total else 0
    print(f"{Fore.GREEN}- {name.ljust(25)} {Fore.YELLOW}{p:.1f}% {progress_bar(p)} {Fore.WHITE}({h}h){Style.RESET_ALL}")
print(f"{Fore.GREEN}Total Good: {good_total}h{Style.RESET_ALL}")

if bad_total > good_total:
    print(f"\n{Fore.LIGHTYELLOW_EX}⚠️  You spent more time on distractions than good activities.{Style.RESET_ALL}")
else:
    print(f"\n{Fore.LIGHTGREEN_EX}🎯 Well done! You maintained a healthy balance.{Style.RESET_ALL}")
#====================================#