# SecToolkit Usage Guide

Complete guide for using all tools in SecToolkit.

## Installation

```bash
git clone https://github.com/kishan7878/SecToolkit.git
cd SecToolkit
pip install -r requirements.txt
python sectoolkit.py
```

---

## 1. Android Security Tools

### APK Analyzer
Analyzes APK files for structure, security, and metadata.

```bash
# Interactive
python sectoolkit.py
# Select: 1 -> 1 -> Enter APK path

# Direct
python sectoolkit.py --tool apk-analyzer --file app.apk
```

**What it checks:**
- File hash (SHA256)
- APK contents (DEX, libraries, resources)
- Signing status
- ProGuard configuration
- Native architectures

### ProGuard Config Generator
Generates comprehensive ProGuard rules for code obfuscation.

```bash
# Interactive
python sectoolkit.py
# Select: 1 -> 2
```

**Output:** `proguard-rules.pro` file ready to use

### Security Checker
Scans APK for common security issues.

```bash
python sectoolkit.py
# Select: 1 -> 3 -> Enter APK path
```

**Checks for:**
- Unsigned APKs
- Hardcoded secrets
- Potential vulnerabilities

### Certificate Validator
Validates APK signing certificates.

```bash
python sectoolkit.py
# Select: 1 -> 4 -> Enter APK path
```

---

## 2. Development Tools

### Build Automation
Generates automated build scripts for Android projects.

```bash
python sectoolkit.py
# Select: 2 -> 1
```

**Creates:** Bash script with clean, build, and verification steps

### Version Manager
Manages semantic versioning for your projects.

```bash
python sectoolkit.py
# Select: 2 -> 2
```

**Features:**
- Major/Minor/Patch versioning
- Build number tracking
- Version history
- Release notes

### Dependency Checker
Analyzes project dependencies.

```bash
python sectoolkit.py
# Select: 2 -> 3 -> Enter build.gradle path
```

### Code Quality Analyzer
Analyzes project structure and code metrics.

```bash
python sectoolkit.py
# Select: 2 -> 4 -> Enter project directory
```

---

## 3. Penetration Testing Tools

⚠️ **WARNING:** Use only on systems you own or have explicit permission to test!

### Network Scanner
Scans network for active hosts.

```bash
python sectoolkit.py
# Select: 3 -> 1 -> Enter network (e.g., 192.168.1.0/24)
```

### Port Scanner
Discovers open ports on target systems.

```bash
python sectoolkit.py
# Select: 3 -> 2
# Enter: target IP/domain, start port, end port
```

**Example:**
```
Target: 192.168.1.1
Start port: 1
End port: 1024
```

### SSL/TLS Checker
Validates SSL certificates and checks security.

```bash
python sectoolkit.py
# Select: 3 -> 3 -> Enter domain
```

**Checks:**
- Certificate details
- Expiration dates
- TLS version
- Security recommendations

### Header Analyzer
Analyzes HTTP security headers.

```bash
python sectoolkit.py
# Select: 3 -> 4 -> Enter URL
```

**Checks for:**
- HSTS
- CSP
- X-Frame-Options
- X-Content-Type-Options
- And more...

---

## 4. Utility Tools

### File Hash Generator
Generates multiple hash types for files.

```bash
python sectoolkit.py
# Select: 4 -> 1 -> Enter file path
```

**Generates:**
- MD5
- SHA1
- SHA256
- SHA512

### QR Code Generator
Creates QR codes from text/URLs.

```bash
python sectoolkit.py
# Select: 4 -> 2
# Enter: data and output filename
```

### Encryption/Decryption Tool
Encrypts and decrypts text using AES.

```bash
python sectoolkit.py
# Select: 4 -> 3
# Choose: Encrypt (1) or Decrypt (2)
```

**Important:** Save the encryption key! You'll need it to decrypt.

### Password Strength Checker
Analyzes password security.

```bash
python sectoolkit.py
# Select: 4 -> 4 -> Enter password
```

**Checks:**
- Length
- Character variety
- Strength score
- Recommendations

---

## 5. Bug Bounty Helpers

### Subdomain Finder
Discovers subdomains for a target domain.

```bash
python sectoolkit.py
# Select: 5 -> 1 -> Enter domain
```

**Note:** For comprehensive results, use specialized tools like Sublist3r or Amass.

### WHOIS Lookup
Retrieves domain registration information.

```bash
python sectoolkit.py
# Select: 5 -> 2 -> Enter domain
```

**Shows:**
- Registrar
- Creation/expiration dates
- Name servers
- Status

### URL Parameter Analyzer
Analyzes URLs for potential vulnerabilities.

```bash
python sectoolkit.py
# Select: 5 -> 3 -> Enter URL
```

**Identifies:**
- URL components
- Parameters
- Potential injection points
- Suggested test payloads

### API Testing Tool
Tests API endpoints with custom requests.

```bash
python sectoolkit.py
# Select: 5 -> 4
# Configure: method, headers, body
```

**Supports:**
- GET, POST, PUT, DELETE
- Custom headers
- JSON payloads
- Response analysis

---

## Tips & Best Practices

### General
- Always get permission before testing systems
- Use in controlled environments
- Keep tools updated
- Report vulnerabilities responsibly

### Android Security
- Test on your own apps first
- Combine with professional tools (MobSF, Jadx)
- Keep ProGuard rules updated
- Sign all production APKs

### Penetration Testing
- Document all findings
- Use VPN when appropriate
- Respect rate limits
- Follow responsible disclosure

### Bug Bounty
- Read program rules carefully
- Start with reconnaissance
- Document everything
- Be patient and thorough

---

## Troubleshooting

### Common Issues

**Import errors:**
```bash
pip install -r requirements.txt --upgrade
```

**Permission denied:**
```bash
chmod +x sectoolkit.py
```

**Network timeouts:**
- Check firewall settings
- Verify target is accessible
- Increase timeout values

---

## Examples

### Complete APK Analysis Workflow
```bash
# 1. Analyze APK structure
python sectoolkit.py
# Select: 1 -> 1 -> app.apk

# 2. Check security issues
# Select: 1 -> 3 -> app.apk

# 3. Validate certificate
# Select: 1 -> 4 -> app.apk

# 4. Generate ProGuard rules for next version
# Select: 1 -> 2
```

### Bug Bounty Reconnaissance
```bash
# 1. WHOIS lookup
# Select: 5 -> 2 -> target.com

# 2. Find subdomains
# Select: 5 -> 1 -> target.com

# 3. Check SSL
# Select: 3 -> 3 -> target.com

# 4. Analyze headers
# Select: 3 -> 4 -> https://target.com
```

---

## Need Help?

- 📖 Check [README.md](README.md)
- 🐛 Report issues on [GitHub](https://github.com/kishan7878/SecToolkit/issues)
- 💬 Join discussions
- 📧 Contact maintainers

---

**Remember:** Use responsibly and ethically! 🛡️
