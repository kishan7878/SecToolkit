#!/usr/bin/env python3
"""
APK Analysis Example
Demonstrates comprehensive APK security analysis
"""

import sys
sys.path.append('..')

from modules.android_security import AndroidSecurity
from colorama import init, Fore, Style

init(autoreset=True)

def comprehensive_apk_analysis(apk_path):
    """Perform comprehensive APK analysis"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"  Comprehensive APK Security Analysis")
    print(f"  File: {apk_path}")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    
    # 1. Basic Analysis
    print(f"{Fore.YELLOW}[1/3] Analyzing APK Structure...{Style.RESET_ALL}")
    AndroidSecurity.apk_analyzer(apk_path)
    
    # 2. Security Check
    print(f"\n{Fore.YELLOW}[2/3] Running Security Checks...{Style.RESET_ALL}")
    AndroidSecurity.security_checker(apk_path)
    
    # 3. Certificate Validation
    print(f"\n{Fore.YELLOW}[3/3] Validating Certificate...{Style.RESET_ALL}")
    AndroidSecurity.certificate_validator(apk_path)
    
    print(f"\n{Fore.GREEN}{'='*60}")
    print(f"  Analysis Complete!")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    
    # Recommendations
    print(f"{Fore.CYAN}[*] Recommendations:{Style.RESET_ALL}\n")
    print(f"  1. Use ProGuard/R8 for code obfuscation")
    print(f"  2. Enable certificate pinning for network security")
    print(f"  3. Implement root detection")
    print(f"  4. Use SafetyNet Attestation API")
    print(f"  5. Encrypt sensitive data")
    print(f"  6. Implement tamper detection")
    print(f"  7. Use HTTPS for all network communication")
    print(f"  8. Validate all user inputs")
    print(f"\n{Fore.YELLOW}[*] For detailed analysis, use:{Style.RESET_ALL}")
    print(f"  - MobSF (Mobile Security Framework)")
    print(f"  - Jadx (DEX to Java decompiler)")
    print(f"  - APKTool (APK reverse engineering)")
    print()

def main():
    """Main function"""
    print(f"{Fore.CYAN}SecToolkit - APK Analysis Example{Style.RESET_ALL}\n")
    
    if len(sys.argv) > 1:
        apk_path = sys.argv[1]
    else:
        apk_path = input(f"{Fore.CYAN}[>] Enter APK file path: {Style.RESET_ALL}").strip()
    
    if not apk_path:
        print(f"{Fore.RED}[!] No APK file specified!{Style.RESET_ALL}")
        sys.exit(1)
    
    try:
        comprehensive_apk_analysis(apk_path)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Analysis interrupted by user{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
