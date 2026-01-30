# 🛡️ SecToolkit - Complete Security Toolkit

[![Tests](https://github.com/kishan7878/SecToolkit/actions/workflows/test.yml/badge.svg)](https://github.com/kishan7878/SecToolkit/actions/workflows/test.yml)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/kishan7878/SecToolkit?style=social)](https://github.com/kishan7878/SecToolkit/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/kishan7878/SecToolkit?style=social)](https://github.com/kishan7878/SecToolkit/network/members)

A comprehensive security toolkit combining **Android Security Analysis**, **Penetration Testing**, **Development Tools**, and **Bug Bounty Helpers** - all in one place!

## ⚠️ Disclaimer
**FOR EDUCATIONAL PURPOSES ONLY**
- Use only on systems/networks you own or have explicit permission to test
- Unauthorized access to computer systems is illegal
- Author is not responsible for misuse

---

## 🎯 Features Overview

<table>
<tr>
<td width="50%">

### 🤖 Android Security Tools
- **APK Analyzer** - Deep APK structure analysis
- **ProGuard Config Generator** - Auto-generate obfuscation rules
- **Security Checker** - Detect vulnerabilities
- **Certificate Validator** - Verify APK signatures

</td>
<td width="50%">

### 🔧 Development Tools
- **Build Automation** - Automated APK building
- **Version Manager** - Semantic versioning
- **Dependency Checker** - Find outdated libraries
- **Code Quality Analyzer** - Code metrics

</td>
</tr>
<tr>
<td width="50%">

### 🔍 Penetration Testing
- **Network Scanner** - Discover active hosts
- **Port Scanner** - Find open ports
- **SSL/TLS Checker** - Certificate validation
- **Header Analyzer** - HTTP security headers

</td>
<td width="50%">

### 🎁 Utility Tools
- **File Hash Generator** - MD5/SHA checksums
- **QR Code Generator** - Create QR codes
- **Encryption Tool** - AES encryption/decryption
- **Password Checker** - Strength analysis

</td>
</tr>
<tr>
<td colspan="2">

### 🐛 Bug Bounty Helpers
- **Subdomain Finder** - Enumerate subdomains
- **WHOIS Lookup** - Domain information
- **URL Parameter Analyzer** - Test parameters
- **API Testing Tool** - Test API endpoints

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/kishan7878/SecToolkit.git
cd SecToolkit

# Install dependencies
pip install -r requirements.txt

# Run the toolkit
python sectoolkit.py
```

### Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for some tools)

---

## 📖 Usage

### Interactive Mode (Recommended)
```bash
python sectoolkit.py
```
Navigate through the beautiful menu interface and select your desired tool!

### Direct Tool Access
```bash
# APK Analysis
python sectoolkit.py --tool apk-analyzer --file app.apk

# Port Scanning
python sectoolkit.py --tool port-scanner --target 192.168.1.1

# Hash Generation
python sectoolkit.py --tool hash-generator --file document.pdf
```

### Programmatic Usage
```python
from modules.android_security import AndroidSecurity
from modules.pentest_tools import PentestTools

# Analyze APK
AndroidSecurity.apk_analyzer('app.apk')

# Scan ports
PentestTools.port_scanner('192.168.1.1', 1, 1000)
```

---

## 📚 Documentation

- **[Usage Guide](USAGE.md)** - Comprehensive guide for all tools
- **[Examples](examples/)** - Example scripts and use cases
- **[Contributing](CONTRIBUTING.md)** - How to contribute
- **[Security Policy](SECURITY.md)** - Ethical use guidelines
- **[License](LICENSE)** - MIT License

---

## 🎬 Screenshots

### Main Menu
```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   ███████╗███████╗ ██████╗████████╗ ██████╗  ██████╗ ██╗  ║
║   ██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║  ║
║   ███████╗█████╗  ██║        ██║   ██║   ██║██║   ██║██║  ║
║   ╚════██║██╔══╝  ██║        ██║   ██║   ██║██║   ██║██║  ║
║   ███████║███████╗╚██████╗   ██║   ╚██████╔╝╚██████╔╝███████╗║
║   ╚══════╝╚══════╝ ╚═════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝║
║                                                           ║
║              Complete Security Toolkit v1.0              ║
║              Educational Purpose Only                    ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 🛠️ Tools Breakdown

### Android Security Tools

#### APK Analyzer
Comprehensive APK analysis including:
- File hash calculation (SHA256)
- APK structure analysis
- DEX files detection
- Native libraries and architectures
- Signing status verification
- ProGuard configuration detection

#### Security Checker
Scans for common vulnerabilities:
- Unsigned APKs
- Hardcoded secrets
- Debuggable flags
- Backup allowance
- Clear text traffic

### Penetration Testing Tools

#### Network Scanner
- Fast network host discovery
- Multi-threaded scanning
- CIDR notation support
- Active host detection

#### Port Scanner
- Customizable port ranges
- Service identification
- Multi-threaded scanning
- Common ports database

### Bug Bounty Helpers

#### Subdomain Finder
- DNS resolution
- Common subdomain enumeration
- A record lookup
- Integration suggestions (Sublist3r, Amass)

#### API Testing Tool
- Multiple HTTP methods (GET, POST, PUT, DELETE)
- Custom headers support
- JSON payload handling
- Response analysis

---

## 🧪 Testing

Run the test suite:
```bash
python test_basic.py
```

The toolkit includes automated tests that verify:
- File structure integrity
- Python syntax validation
- Module imports
- Basic functionality

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📋 Roadmap

- [ ] Add more Android security checks
- [ ] Implement automated reporting
- [ ] Add web vulnerability scanner
- [ ] Create GUI version
- [ ] Add Docker support
- [ ] Integrate with CI/CD pipelines
- [ ] Add more bug bounty tools
- [ ] Create mobile app version

---

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Additional Disclaimer:** This software is provided for educational and ethical security research purposes only. Users must comply with all applicable laws and regulations.

---

## 👨‍💻 Author

Created with ❤️ for the security community

---

## 🔗 Links

- **Repository:** [github.com/kishan7878/SecToolkit](https://github.com/kishan7878/SecToolkit)
- **Issues:** [Report bugs](https://github.com/kishan7878/SecToolkit/issues)
- **Discussions:** [Join the community](https://github.com/kishan7878/SecToolkit/discussions)

---

## 📞 Support

- 📖 Check the [Usage Guide](USAGE.md)
- 🐛 [Report Issues](https://github.com/kishan7878/SecToolkit/issues)
- 💬 [Discussions](https://github.com/kishan7878/SecToolkit/discussions)
- ⭐ Star the repo if you find it useful!

---

## 🙏 Acknowledgments

- Thanks to all contributors
- Inspired by the security research community
- Built with Python and love for ethical hacking

---

<div align="center">

**Made for Educational Purposes | Use Responsibly | Stay Ethical** 🛡️

[![GitHub](https://img.shields.io/badge/GitHub-SecToolkit-blue?style=for-the-badge&logo=github)](https://github.com/kishan7878/SecToolkit)

</div>
