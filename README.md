# PyCompiler

> **Transform Python scripts into standalone Windows executables with one command**

## What is PyCompiler?

PyCompiler converts Python applications into Windows executables (.exe files). Simple, fast, and reliable.

**Why use PyCompiler?**
- ✅ **Simple setup** - Just configure and build
- ✅ **Standalone executables** - Run without Python installed
- ✅ **Beautiful CLI** - Progress tracking with feedback
- ✅ **Auto-dependencies** - Installs what you need
- ✅ **Clean builds** - Removes temporary files

## Quick Start

### 1. Configure
Create `config.yaml`:

```yaml
# Required
project_name: "my_app"
main_file: "main.py"
output_name: "my_app.exe"

# Optional
project_libs:
  - "requests"
```

### 2. Build
```bash
python compiler.py
```

### 3. Done!
Your `my_app.exe` is ready to distribute! 🎉

---

## Usage

```bash
# Build project
python compiler.py

# Check configuration
python compiler.py --info

# Use custom config
python compiler.py --config my.yaml

# Show help
python compiler.py --show-help
```

### What You'll See
```
┌─ PyCompiler - Python to Native Builder ─┐

✓ Environment created
✓ Dependencies installed
✓ Compilation completed
✓ Cleanup finished

┌─ Success ─────────────────────────────────────┐
│ Build completed successfully!                 │
│ Output: my_app.exe                           │
└───────────────────────────────────────────────┘
```

---

## Configuration

### Required Fields (3 only)
```yaml
project_name: "my_app"      # App name
main_file: "main.py"        # Main Python file
output_name: "my_app.exe"   # Output executable
```

### Optional Fields
```yaml
# Your dependencies
project_libs:
  - "requests"
  - "pandas"

# Packages to include
include_packages:
  - "src"

# Windows icon
icon_file: "icon.ico"

# Executable properties
windows_metadata:
  product_name: "My App"
  file_description: "My Python Application"
  product_version: "1.0.0.0"
  copyright: "My Company"
```

---

## Example

### Python Script (`main.py`)
```python
import requests

def main():
    response = requests.get("https://api.github.com")
    print(f"Status: {response.status_code}")

if __name__ == "__main__":
    main()
```

### Configuration (`config.yaml`)
```yaml
project_name: "github_checker"
main_file: "main.py"
output_name: "github_checker.exe"
project_libs:
  - "requests"
```

### Build
```bash
python compiler.py
```

**Result:** `github_checker.exe` (standalone executable)

---

## Installation

```bash
pip install -r requirements.txt
```

**Requirements:**
- Python 3.7+
- Windows (for .exe output)

---

## How It Works

1. **Creates environment** - Isolated build space
2. **Installs dependencies** - Your libraries + tools
3. **Compiles with Nuitka** - Python to native code
4. **Applies optimizations** - Compression, metadata
5. **Cleans up** - Removes temporary files
6. **Delivers executable** - Ready to use

---

## Use Cases

- **Desktop apps** - GUI applications
- **CLI tools** - Command-line utilities
- **Data tools** - Analysis scripts
- **Web scrapers** - Standalone scrapers
- **API clients** - Web service tools
- **Automation** - Task automation

---

## Tips

### Getting Started
- Start with required fields only
- Test your exe on clean Windows machine
- Add dependencies as needed

### Best Practices
- Use clear project names
- Include all required libraries
- Test thoroughly before distribution

### Troubleshooting
- **Missing dependencies** → Add to `project_libs`
- **Large file size** → UPX compression is enabled
- **Build errors** → Check Python syntax and dependencies

---

## Project Structure

```
pycompiler/
├── compiler.py          # Build tool
├── src/
│   ├── cli.py          # Command interface
│   └── builder.py      # Build engine
├── config.yaml         # Configuration
└── requirements.txt    # Dependencies
```

---

**Made with ❤️ for Python developers** 