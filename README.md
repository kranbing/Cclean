# Cclean

Cclean is a Windows desktop C drive cleanup tool. The first milestone sets up
the project structure, application entry point, base GUI shell, and logging.

## Development Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Current Scope

- PySide6 desktop application shell
- Basic main window layout
- Application logging
- Project structure for scanner, cleaner, safety, permissions, and UI modules

Cleanup features will be implemented in later phases.
