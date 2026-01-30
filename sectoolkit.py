#!/usr/bin/env python3
"""
SecToolkit - Complete Security Toolkit
Educational Purpose Only
"""

import sys
import argparse
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Import modules
from modules.android_security import AndroidSecurity
from modules.dev_tools import DevTools
from modules.pentest_tools import PentestTools
from modules.utility_tools import UtilityTools
from modules.bugbounty_tools import BugBountyTools

BANNER = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   {Fore.GREEN}███████╗███████╗ ██████╗████████╗ ██████╗  ██████╗ ██╗  {Fore.CYAN}║
║   {Fore.GREEN}██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║  {Fore.CYAN}║
║   {Fore.GREEN}███████╗█████╗  ██║        ██║   ██║   ██║██║   ██║██║  {Fore.CYAN}║
║   {Fore.GREEN}╚════██║██╔══╝  ██║        ██║   ██║   ██║██║   ██║██║  {Fore.CYAN}║
║   {Fore.GREEN}███████║███████╗╚██████╗   ██║   ╚██████╔╝╚██████╔╝███████╗{Fore.CYAN}║
║   {Fore.GREEN}╚══════╝╚══════╝ ╚═════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝{Fore.CYAN}║
║                                                           ║
║              {Fore.YELLOW}Complete Security Toolkit v1.0{Fore.CYAN}                ║
║              {Fore.RED}Educational Purpose Only{Fore.CYAN}                      ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""

def print_menu():
    """Display main menu"""
    print(BANNER)
    print(f"\n{Fore.YELLOW}[*] Select Category:{Style.RESET_ALL}\n")
    print(f"{Fore.GREEN}1.{Style.RESET_ALL} Android Security Tools")
    print(f"{Fore.GREEN}2.{Style.RESET_ALL} Development Tools")
    print(f"{Fore.GREEN}3.{Style.RESET_ALL} Penetration Testing Tools")
    print(f"{Fore.GREEN}4.{Style.RESET_ALL} Utility Tools")
    print(f"{Fore.GREEN}5.{Style.RESET_ALL} Bug Bounty Helpers")
    print(f"{Fore.RED}0.{Style.RESET_ALL} Exit\n")

def android_menu():
    """Android Security Tools menu"""
    print(f"\n{Fore.CYAN}=== Android Security Tools ==={Style.RESET_ALL}\n")
    print(f"{Fore.GREEN}1.{Style.RESET_ALL} APK Analyzer")
    print(f"{Fore.GREEN}2.{Style.RESET_ALL} ProGuard Config Generator")
    print(f"{Fore.GREEN}3.{Style.RESET_ALL} Security Checker")
    print(f"{Fore.GREEN}4.{Style.RESET_ALL} Certificate Validator")
    print(f"{Fore.YELLOW}0.{Style.RESET_ALL} Back to Main Menu\n")

def dev_menu():
    """Development Tools menu"""
    print(f"\n{Fore.CYAN}=== Development Tools ==={Style.RESET_ALL}\n")
    print(f"{Fore.GREEN}1.{Style.RESET_ALL} Build Automation")
    print(f"{Fore.GREEN}2.{Style.RESET_ALL} Version Manager")
    print(f"{Fore.GREEN}3.{Style.RESET_ALL} Dependency Checker")
    print(f"{Fore.GREEN}4.{Style.RESET_ALL} Code Quality Analyzer")
    print(f"{Fore.YELLOW}0.{Style.RESET_ALL} Back to Main Menu\n")

def pentest_menu():
    """Penetration Testing Tools menu"""
    print(f"\n{Fore.CYAN}=== Penetration Testing Tools ==={Style.RESET_ALL}\n")
    print(f"{Fore.GREEN}1.{Style.RESET_ALL} Network Scanner")
    print(f"{Fore.GREEN}2.{Style.RESET_ALL} Port Scanner")
    print(f"{Fore.GREEN}3.{Style.RESET_ALL} SSL/TLS Checker")
    print(f"{Fore.GREEN}4.{Style.RESET_ALL} Header Analyzer")
    print(f"{Fore.YELLOW}0.{Style.RESET_ALL} Back to Main Menu\n")

def utility_menu():
    """Utility Tools menu"""
    print(f"\n{Fore.CYAN}=== Utility Tools ==={Style.RESET_ALL}\n")
    print(f"{Fore.GREEN}1.{Style.RESET_ALL} File Hash Generator")
    print(f"{Fore.GREEN}2.{Style.RESET_ALL} QR Code Generator/Scanner")
    print(f"{Fore.GREEN}3.{Style.RESET_ALL} Encryption/Decryption Tool")
    print(f"{Fore.GREEN}4.{Style.RESET_ALL} Password Strength Checker")
    print(f"{Fore.YELLOW}0.{Style.RESET_ALL} Back to Main Menu\n")

def bugbounty_menu():
    """Bug Bounty Tools menu"""
    print(f"\n{Fore.CYAN}=== Bug Bounty Helpers ==={Style.RESET_ALL}\n")
    print(f"{Fore.GREEN}1.{Style.RESET_ALL} Subdomain Finder")
    print(f"{Fore.GREEN}2.{Style.RESET_ALL} WHOIS Lookup")
    print(f"{Fore.GREEN}3.{Style.RESET_ALL} URL Parameter Analyzer")
    print(f"{Fore.GREEN}4.{Style.RESET_ALL} API Testing Tool")
    print(f"{Fore.YELLOW}0.{Style.RESET_ALL} Back to Main Menu\n")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='SecToolkit - Complete Security Toolkit')
    parser.add_argument('--tool', help='Direct tool access')
    parser.add_argument('--target', help='Target for scanning/testing')
    parser.add_argument('--file', help='File to analyze')
    args = parser.parse_args()

    # Direct tool access
    if args.tool:
        print(f"{Fore.YELLOW}[*] Running tool: {args.tool}{Style.RESET_ALL}")
        # Tool execution logic here
        return

    # Interactive mode
    while True:
        print_menu()
        try:
            choice = input(f"{Fore.CYAN}[>] Enter choice: {Style.RESET_ALL}").strip()
            
            if choice == '0':
                print(f"\n{Fore.GREEN}[+] Thanks for using SecToolkit! Stay ethical! 🛡️{Style.RESET_ALL}\n")
                sys.exit(0)
            elif choice == '1':
                android_menu()
                android_choice = input(f"{Fore.CYAN}[>] Enter choice: {Style.RESET_ALL}").strip()
                AndroidSecurity.handle_choice(android_choice)
            elif choice == '2':
                dev_menu()
                dev_choice = input(f"{Fore.CYAN}[>] Enter choice: {Style.RESET_ALL}").strip()
                DevTools.handle_choice(dev_choice)
            elif choice == '3':
                pentest_menu()
                pentest_choice = input(f"{Fore.CYAN}[>] Enter choice: {Style.RESET_ALL}").strip()
                PentestTools.handle_choice(pentest_choice)
            elif choice == '4':
                utility_menu()
                utility_choice = input(f"{Fore.CYAN}[>] Enter choice: {Style.RESET_ALL}").strip()
                UtilityTools.handle_choice(utility_choice)
            elif choice == '5':
                bugbounty_menu()
                bugbounty_choice = input(f"{Fore.CYAN}[>] Enter choice: {Style.RESET_ALL}").strip()
                BugBountyTools.handle_choice(bugbounty_choice)
            else:
                print(f"{Fore.RED}[!] Invalid choice!{Style.RESET_ALL}")
        except KeyboardInterrupt:
            print(f"\n\n{Fore.YELLOW}[!] Interrupted by user{Style.RESET_ALL}")
            sys.exit(0)
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
