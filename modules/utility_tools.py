"""
Utility Tools Module
"""

import hashlib
import qrcode
from PIL import Image
from colorama import Fore, Style
from cryptography.fernet import Fernet
import base64
import re

class UtilityTools:
    """Utility Tools"""
    
    @staticmethod
    def hash_generator(file_path):
        """Generate file hashes"""
        print(f"\n{Fore.CYAN}[*] File Hash Generator{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}[*] File: {file_path}{Style.RESET_ALL}\n")
        
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            
            # Calculate hashes
            md5 = hashlib.md5(data).hexdigest()
            sha1 = hashlib.sha1(data).hexdigest()
            sha256 = hashlib.sha256(data).hexdigest()
            sha512 = hashlib.sha512(data).hexdigest()
            
            print(f"{Fore.GREEN}[+] Hash Values:{Style.RESET_ALL}\n")
            print(f"  MD5:    {md5}")
            print(f"  SHA1:   {sha1}")
            print(f"  SHA256: {sha256}")
            print(f"  SHA512: {sha512}\n")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
    
    @staticmethod
    def qr_generator():
        """Generate QR code"""
        print(f"\n{Fore.CYAN}[*] QR Code Generator{Style.RESET_ALL}\n")
        
        data = input(f"{Fore.CYAN}[>] Enter data for QR code: {Style.RESET_ALL}").strip()
        output = input(f"{Fore.CYAN}[>] Output filename (default: qrcode.png): {Style.RESET_ALL}").strip() or "qrcode.png"
        
        try:
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(output)
            
            print(f"\n{Fore.GREEN}[+] QR code saved to: {output}{Style.RESET_ALL}\n")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
    
    @staticmethod
    def encryption_tool():
        """Encrypt/Decrypt text"""
        print(f"\n{Fore.CYAN}[*] Encryption/Decryption Tool{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}1. Encrypt")
        print(f"2. Decrypt{Style.RESET_ALL}\n")
        
        choice = input(f"{Fore.CYAN}[>] Choose option: {Style.RESET_ALL}").strip()
        
        try:
            if choice == '1':
                # Encrypt
                text = input(f"{Fore.CYAN}[>] Enter text to encrypt: {Style.RESET_ALL}").strip()
                
                # Generate key
                key = Fernet.generate_key()
                f = Fernet(key)
                
                # Encrypt
                encrypted = f.encrypt(text.encode())
                
                print(f"\n{Fore.GREEN}[+] Encryption Key (SAVE THIS!):{Style.RESET_ALL}")
                print(f"  {key.decode()}\n")
                print(f"{Fore.GREEN}[+] Encrypted Text:{Style.RESET_ALL}")
                print(f"  {encrypted.decode()}\n")
                
            elif choice == '2':
                # Decrypt
                key = input(f"{Fore.CYAN}[>] Enter encryption key: {Style.RESET_ALL}").strip()
                encrypted_text = input(f"{Fore.CYAN}[>] Enter encrypted text: {Style.RESET_ALL}").strip()
                
                f = Fernet(key.encode())
                decrypted = f.decrypt(encrypted_text.encode())
                
                print(f"\n{Fore.GREEN}[+] Decrypted Text:{Style.RESET_ALL}")
                print(f"  {decrypted.decode()}\n")
            else:
                print(f"{Fore.RED}[!] Invalid choice!{Style.RESET_ALL}")
                
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
    
    @staticmethod
    def password_checker():
        """Check password strength"""
        print(f"\n{Fore.CYAN}[*] Password Strength Checker{Style.RESET_ALL}\n")
        
        password = input(f"{Fore.CYAN}[>] Enter password to check: {Style.RESET_ALL}").strip()
        
        # Criteria
        length = len(password) >= 8
        uppercase = bool(re.search(r'[A-Z]', password))
        lowercase = bool(re.search(r'[a-z]', password))
        numbers = bool(re.search(r'\d', password))
        special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        
        score = sum([length, uppercase, lowercase, numbers, special])
        
        print(f"\n{Fore.YELLOW}[*] Password Analysis:{Style.RESET_ALL}\n")
        print(f"  Length (≥8): {Fore.GREEN + '✓' if length else Fore.RED + '✗'}{Style.RESET_ALL}")
        print(f"  Uppercase: {Fore.GREEN + '✓' if uppercase else Fore.RED + '✗'}{Style.RESET_ALL}")
        print(f"  Lowercase: {Fore.GREEN + '✓' if lowercase else Fore.RED + '✗'}{Style.RESET_ALL}")
        print(f"  Numbers: {Fore.GREEN + '✓' if numbers else Fore.RED + '✗'}{Style.RESET_ALL}")
        print(f"  Special chars: {Fore.GREEN + '✓' if special else Fore.RED + '✗'}{Style.RESET_ALL}")
        
        # Strength
        if score <= 2:
            strength = f"{Fore.RED}WEAK"
        elif score <= 3:
            strength = f"{Fore.YELLOW}MEDIUM"
        elif score <= 4:
            strength = f"{Fore.GREEN}STRONG"
        else:
            strength = f"{Fore.GREEN}VERY STRONG"
        
        print(f"\n{Fore.CYAN}[*] Strength: {strength}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*] Score: {score}/5{Style.RESET_ALL}\n")
        
        # Recommendations
        if score < 5:
            print(f"{Fore.YELLOW}[*] Recommendations:{Style.RESET_ALL}")
            if not length:
                print(f"  - Use at least 8 characters")
            if not uppercase:
                print(f"  - Add uppercase letters")
            if not lowercase:
                print(f"  - Add lowercase letters")
            if not numbers:
                print(f"  - Add numbers")
            if not special:
                print(f"  - Add special characters")
            print()
    
    @staticmethod
    def handle_choice(choice):
        """Handle menu choice"""
        if choice == '0':
            return
        elif choice == '1':
            file_path = input(f"{Fore.CYAN}[>] Enter file path: {Style.RESET_ALL}").strip()
            UtilityTools.hash_generator(file_path)
        elif choice == '2':
            UtilityTools.qr_generator()
        elif choice == '3':
            UtilityTools.encryption_tool()
        elif choice == '4':
            UtilityTools.password_checker()
        else:
            print(f"{Fore.RED}[!] Invalid choice!{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
