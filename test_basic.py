#!/usr/bin/env python3
"""
Basic tests for SecToolkit
"""

import sys
import os

def test_imports():
    """Test if all modules can be imported"""
    print("Testing module imports...")
    
    try:
        from modules.android_security import AndroidSecurity
        print("✓ AndroidSecurity imported successfully")
    except Exception as e:
        print(f"✗ AndroidSecurity import failed: {e}")
        return False
    
    try:
        from modules.pentest_tools import PentestTools
        print("✓ PentestTools imported successfully")
    except Exception as e:
        print(f"✗ PentestTools import failed: {e}")
        return False
    
    try:
        from modules.utility_tools import UtilityTools
        print("✓ UtilityTools imported successfully")
    except Exception as e:
        print(f"✗ UtilityTools import failed: {e}")
        return False
    
    try:
        from modules.bugbounty_tools import BugBountyTools
        print("✓ BugBountyTools imported successfully")
    except Exception as e:
        print(f"✗ BugBountyTools import failed: {e}")
        return False
    
    try:
        from modules.dev_tools import DevTools
        print("✓ DevTools imported successfully")
    except Exception as e:
        print(f"✗ DevTools import failed: {e}")
        return False
    
    return True

def test_file_structure():
    """Test if all required files exist"""
    print("\nTesting file structure...")
    
    required_files = [
        'sectoolkit.py',
        'requirements.txt',
        'README.md',
        'LICENSE',
        'modules/__init__.py',
        'modules/android_security.py',
        'modules/pentest_tools.py',
        'modules/utility_tools.py',
        'modules/bugbounty_tools.py',
        'modules/dev_tools.py'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} missing")
            all_exist = False
    
    return all_exist

def test_syntax():
    """Test Python syntax"""
    print("\nTesting Python syntax...")
    
    import py_compile
    
    files_to_check = [
        'sectoolkit.py',
        'modules/android_security.py',
        'modules/pentest_tools.py',
        'modules/utility_tools.py',
        'modules/bugbounty_tools.py',
        'modules/dev_tools.py'
    ]
    
    all_valid = True
    for file in files_to_check:
        try:
            py_compile.compile(file, doraise=True)
            print(f"✓ {file} syntax valid")
        except py_compile.PyCompileError as e:
            print(f"✗ {file} syntax error: {e}")
            all_valid = False
    
    return all_valid

def main():
    """Run all tests"""
    print("="*60)
    print("SecToolkit Basic Tests")
    print("="*60)
    
    results = []
    
    # Test 1: File structure
    results.append(("File Structure", test_file_structure()))
    
    # Test 2: Syntax
    results.append(("Python Syntax", test_syntax()))
    
    # Test 3: Imports
    results.append(("Module Imports", test_imports()))
    
    # Summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    
    passed = 0
    failed = 0
    
    for test_name, result in results:
        status = "PASSED" if result else "FAILED"
        symbol = "✓" if result else "✗"
        print(f"{symbol} {test_name}: {status}")
        
        if result:
            passed += 1
        else:
            failed += 1
    
    print(f"\nTotal: {passed} passed, {failed} failed")
    print("="*60)
    
    # Exit with appropriate code
    sys.exit(0 if failed == 0 else 1)

if __name__ == "__main__":
    main()
