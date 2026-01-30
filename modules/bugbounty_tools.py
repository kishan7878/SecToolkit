"""
Bug Bounty Helper Tools Module
"""

import requests
import whois
import dns.resolver
from colorama import Fore, Style
from urllib.parse import urlparse, parse_qs
import json

class BugBountyTools:
    """Bug Bounty Helper Tools"""
    
    @staticmethod
    def subdomain_finder(domain):
        """Find subdomains"""
        print(f"\n{Fore.CYAN}[*] Subdomain Finder{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}[*] Target: {domain}{Style.RESET_ALL}\n")
        
        # Common subdomains to check
        common_subdomains = [
            'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk',
            'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'm', 'imap', 'test',
            'ns', 'blog', 'pop3', 'dev', 'www2', 'admin', 'forum', 'news', 'vpn',
            'ns3', 'mail2', 'new', 'mysql', 'old', 'lists', 'support', 'mobile', 'mx',
            'static', 'docs', 'beta', 'shop', 'sql', 'secure', 'demo', 'cp', 'calendar',
            'wiki', 'web', 'media', 'email', 'images', 'img', 'www1', 'intranet',
            'portal', 'video', 'sip', 'dns2', 'api', 'cdn', 'stats', 'dns1', 'ns4',
            'www3', 'dns', 'search', 'staging', 'server', 'mx1', 'chat', 'wap', 'my',
            'svn', 'mail1', 'sites', 'proxy', 'ads', 'host', 'crm', 'cms', 'backup',
            'mx2', 'lyncdiscover', 'info', 'apps', 'download', 'remote', 'db', 'forums',
            'store', 'relay', 'files', 'newsletter', 'app', 'live', 'owa', 'en', 'start',
            'sms', 'office', 'exchange', 'ipv4'
        ]
        
        found_subdomains = []
        
        print(f"{Fore.YELLOW}[*] Checking {len(common_subdomains)} common subdomains...{Style.RESET_ALL}\n")
        
        for subdomain in common_subdomains:
            full_domain = f"{subdomain}.{domain}"
            try:
                # Try DNS resolution
                answers = dns.resolver.resolve(full_domain, 'A')
                for rdata in answers:
                    found_subdomains.append((full_domain, str(rdata)))
                    print(f"{Fore.GREEN}[+] Found: {full_domain} -> {rdata}{Style.RESET_ALL}")
            except:
                pass
        
        print(f"\n{Fore.GREEN}[+] Found {len(found_subdomains)} subdomains{Style.RESET_ALL}\n")
        
        # Additional methods suggestion
        print(f"{Fore.YELLOW}[*] For comprehensive subdomain enumeration, use:{Style.RESET_ALL}")
        print(f"  - Sublist3r")
        print(f"  - Amass")
        print(f"  - Subfinder")
        print(f"  - crt.sh (Certificate Transparency)")
        print()
    
    @staticmethod
    def whois_lookup(domain):
        """WHOIS domain lookup"""
        print(f"\n{Fore.CYAN}[*] WHOIS Lookup{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}[*] Domain: {domain}{Style.RESET_ALL}\n")
        
        try:
            w = whois.whois(domain)
            
            print(f"{Fore.GREEN}[+] WHOIS Information:{Style.RESET_ALL}\n")
            
            if w.domain_name:
                print(f"  Domain Name: {w.domain_name}")
            if w.registrar:
                print(f"  Registrar: {w.registrar}")
            if w.creation_date:
                print(f"  Created: {w.creation_date}")
            if w.expiration_date:
                print(f"  Expires: {w.expiration_date}")
            if w.updated_date:
                print(f"  Updated: {w.updated_date}")
            if w.status:
                print(f"  Status: {w.status}")
            if w.name_servers:
                print(f"  Name Servers: {', '.join(w.name_servers) if isinstance(w.name_servers, list) else w.name_servers}")
            
            print()
            
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
    
    @staticmethod
    def url_analyzer(url):
        """Analyze URL parameters"""
        print(f"\n{Fore.CYAN}[*] URL Parameter Analyzer{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}[*] URL: {url}{Style.RESET_ALL}\n")
        
        try:
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            
            print(f"{Fore.GREEN}[+] URL Components:{Style.RESET_ALL}\n")
            print(f"  Scheme: {parsed.scheme}")
            print(f"  Domain: {parsed.netloc}")
            print(f"  Path: {parsed.path}")
            print(f"  Query: {parsed.query}")
            print(f"  Fragment: {parsed.fragment}")
            
            if params:
                print(f"\n{Fore.GREEN}[+] Parameters:{Style.RESET_ALL}\n")
                for key, value in params.items():
                    print(f"  {key} = {value}")
                
                # Security checks
                print(f"\n{Fore.YELLOW}[*] Security Analysis:{Style.RESET_ALL}\n")
                
                # Check for common vulnerable parameters
                vuln_params = ['id', 'page', 'file', 'url', 'redirect', 'path', 'query', 'search']
                for param in params.keys():
                    if param.lower() in vuln_params:
                        print(f"{Fore.YELLOW}  ! Parameter '{param}' might be vulnerable to:{Style.RESET_ALL}")
                        if param.lower() in ['id', 'page']:
                            print(f"    - SQL Injection")
                        if param.lower() in ['file', 'path']:
                            print(f"    - Path Traversal / LFI")
                        if param.lower() in ['url', 'redirect']:
                            print(f"    - Open Redirect")
                        if param.lower() in ['query', 'search']:
                            print(f"    - XSS")
                
                print(f"\n{Fore.YELLOW}[*] Test payloads:{Style.RESET_ALL}")
                print(f"  SQL Injection: ' OR '1'='1")
                print(f"  XSS: <script>alert('XSS')</script>")
                print(f"  Path Traversal: ../../etc/passwd")
                print()
            else:
                print(f"\n{Fore.YELLOW}[*] No parameters found{Style.RESET_ALL}\n")
                
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
    
    @staticmethod
    def api_tester():
        """Test API endpoints"""
        print(f"\n{Fore.CYAN}[*] API Testing Tool{Style.RESET_ALL}\n")
        
        url = input(f"{Fore.CYAN}[>] Enter API endpoint: {Style.RESET_ALL}").strip()
        method = input(f"{Fore.CYAN}[>] Method (GET/POST/PUT/DELETE): {Style.RESET_ALL}").strip().upper() or "GET"
        
        headers = {}
        add_headers = input(f"{Fore.CYAN}[>] Add custom headers? (y/n): {Style.RESET_ALL}").strip().lower()
        if add_headers == 'y':
            while True:
                key = input(f"{Fore.CYAN}[>] Header name (or press Enter to finish): {Style.RESET_ALL}").strip()
                if not key:
                    break
                value = input(f"{Fore.CYAN}[>] Header value: {Style.RESET_ALL}").strip()
                headers[key] = value
        
        data = None
        if method in ['POST', 'PUT']:
            data_input = input(f"{Fore.CYAN}[>] Request body (JSON): {Style.RESET_ALL}").strip()
            if data_input:
                try:
                    data = json.loads(data_input)
                except:
                    print(f"{Fore.RED}[!] Invalid JSON, sending as text{Style.RESET_ALL}")
                    data = data_input
        
        try:
            print(f"\n{Fore.YELLOW}[*] Sending request...{Style.RESET_ALL}\n")
            
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=10)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data, timeout=10)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, json=data, timeout=10)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers, timeout=10)
            else:
                print(f"{Fore.RED}[!] Invalid method{Style.RESET_ALL}")
                return
            
            print(f"{Fore.GREEN}[+] Response:{Style.RESET_ALL}\n")
            print(f"  Status Code: {response.status_code}")
            print(f"  Reason: {response.reason}")
            
            print(f"\n{Fore.GREEN}[+] Response Headers:{Style.RESET_ALL}\n")
            for key, value in response.headers.items():
                print(f"  {key}: {value}")
            
            print(f"\n{Fore.GREEN}[+] Response Body:{Style.RESET_ALL}\n")
            try:
                # Try to format as JSON
                json_response = response.json()
                print(json.dumps(json_response, indent=2))
            except:
                # Print as text
                print(response.text[:1000])  # Limit output
                if len(response.text) > 1000:
                    print(f"\n... (truncated, total length: {len(response.text)} chars)")
            
            print()
            
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
    
    @staticmethod
    def handle_choice(choice):
        """Handle menu choice"""
        if choice == '0':
            return
        elif choice == '1':
            domain = input(f"{Fore.CYAN}[>] Enter domain: {Style.RESET_ALL}").strip()
            BugBountyTools.subdomain_finder(domain)
        elif choice == '2':
            domain = input(f"{Fore.CYAN}[>] Enter domain: {Style.RESET_ALL}").strip()
            BugBountyTools.whois_lookup(domain)
        elif choice == '3':
            url = input(f"{Fore.CYAN}[>] Enter URL: {Style.RESET_ALL}").strip()
            BugBountyTools.url_analyzer(url)
        elif choice == '4':
            BugBountyTools.api_tester()
        else:
            print(f"{Fore.RED}[!] Invalid choice!{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
