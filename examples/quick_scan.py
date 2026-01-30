#!/usr/bin/env python3
"""
Quick Security Scan Example
Demonstrates how to use SecToolkit modules programmatically
"""

import sys
sys.path.append('..')

from modules.pentest_tools import PentestTools
from modules.utility_tools import UtilityTools
from colorama import init, Fore, Style

init(autoreset=True)

def quick_web_scan(url):
    """Perform a quick security scan on a website"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"  Quick Security Scan")
    print(f"  Target: {url}")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    
    # 1. Check SSL/TLS
    print(f"{Fore.YELLOW}[1/3] Checking SSL/TLS Certificate...{Style.RESET_ALL}")
    domain = url.replace('https://', '').replace('http://', '').split('/')[0]
    PentestTools.ssl_checker(domain)
    
    # 2. Analyze HTTP Headers
    print(f"\n{Fore.YELLOW}[2/3] Analyzing Security Headers...{Style.RESET_ALL}")
    if not url.startswith('http'):
        url = 'https://' + url
    PentestTools.header_analyzer(url)
    
    # 3. Port Scan (common ports only)
    print(f"\n{Fore.YELLOW}[3/3] Scanning Common Ports...{Style.RESET_ALL}")
    common_ports = [80, 443, 8080, 8443]
    for port in common_ports:
        PentestTools.port_scanner(domain, port, port)
    
    print(f"\n{Fore.GREEN}{'='*60}")
    print(f"  Scan Complete!")
    print(f"{'='*60}{Style.RESET_ALL}\n")

def main():
    """Main function"""
    print(f"{Fore.CYAN}SecToolkit - Quick Scan Example{Style.RESET_ALL}\n")
    
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input(f"{Fore.CYAN}[>] Enter target URL or domain: {Style.RESET_ALL}").strip()
    
    if not target:
        print(f"{Fore.RED}[!] No target specified!{Style.RESET_ALL}")
        sys.exit(1)
    
    print(f"{Fore.RED}[!] WARNING: Only scan systems you own or have permission to test!{Style.RESET_ALL}")
    confirm = input(f"{Fore.YELLOW}[?] Continue? (y/n): {Style.RESET_ALL}").strip().lower()
    
    if confirm != 'y':
        print(f"{Fore.YELLOW}[*] Scan cancelled{Style.RESET_ALL}")
        sys.exit(0)
    
    try:
        quick_web_scan(target)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Scan interrupted by user{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
