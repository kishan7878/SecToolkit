# SecToolkit Examples

Example scripts demonstrating how to use SecToolkit modules programmatically.

## Available Examples

### 1. Quick Web Scan (`quick_scan.py`)
Performs a quick security assessment of a website.

**Usage:**
```bash
python examples/quick_scan.py https://example.com
```

**What it does:**
- SSL/TLS certificate check
- HTTP security headers analysis
- Common port scanning

### 2. APK Analysis (`apk_analysis.py`)
Comprehensive security analysis of Android APK files.

**Usage:**
```bash
python examples/apk_analysis.py path/to/app.apk
```

**What it does:**
- APK structure analysis
- Security vulnerability checks
- Certificate validation
- Security recommendations

## Creating Your Own Scripts

You can import and use any SecToolkit module in your own scripts:

```python
#!/usr/bin/env python3
import sys
sys.path.append('..')

from modules.android_security import AndroidSecurity
from modules.pentest_tools import PentestTools
from modules.utility_tools import UtilityTools
from modules.bugbounty_tools import BugBountyTools
from modules.dev_tools import DevTools

# Use any tool
AndroidSecurity.apk_analyzer('app.apk')
PentestTools.port_scanner('192.168.1.1', 1, 1000)
UtilityTools.hash_generator('file.txt')
```

## Tips

- Always check permissions before scanning
- Use try-except for error handling
- Add logging for automation
- Combine multiple tools for comprehensive analysis
- Respect rate limits and timeouts

## More Examples Coming Soon

- Automated bug bounty reconnaissance
- CI/CD integration scripts
- Batch APK analysis
- Network security audit
- API security testing workflow

---

**Remember:** Use these examples responsibly and only on systems you own or have permission to test! 🛡️
