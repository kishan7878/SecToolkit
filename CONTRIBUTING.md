# Contributing to SecToolkit

Thank you for your interest in contributing to SecToolkit! 🎉

## Code of Conduct

- Be respectful and professional
- Focus on educational and ethical security research
- Do not submit malicious code or exploits
- Follow responsible disclosure practices

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported
2. Create a detailed issue with:
   - Description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version)

### Suggesting Features

1. Open an issue with the "enhancement" label
2. Describe the feature and its use case
3. Explain why it would be valuable

### Submitting Code

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Code Guidelines

### Python Style

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Add comments for complex logic

### Security

- Never include hardcoded credentials
- Validate all user inputs
- Handle errors gracefully
- Add appropriate warnings for dangerous operations
- Include ethical use disclaimers

### Testing

- Test on multiple platforms (Linux, macOS, Windows)
- Verify all dependencies work
- Check for edge cases
- Ensure error handling works

## Module Structure

When adding new tools:

```python
class NewToolCategory:
    """Description of tool category"""
    
    @staticmethod
    def tool_name():
        """Tool description"""
        print(f"\n{Fore.CYAN}[*] Tool Name{Style.RESET_ALL}\n")
        # Implementation
    
    @staticmethod
    def handle_choice(choice):
        """Handle menu choice"""
        # Menu logic
```

## Documentation

- Update README.md if adding new features
- Add usage examples
- Document any new dependencies
- Include screenshots if relevant

## Questions?

Open an issue with the "question" label or start a discussion.

---

**Remember:** This toolkit is for educational and ethical purposes only. All contributions must align with this principle.
