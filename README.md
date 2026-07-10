# MemoirAI

A lightweight tool that converts AI-generated “memoir JSON” exports into formatted PDF documents.

It supports:

* LaTeX rendering via **TinyTeX (XeLaTeX)**
* Cross-platform execution (Windows / macOS / Linux)
* Local Python virtual environment (`venv` included)

This project takes structured memoir data (usually extracted from an AI conversation export) and converts it into a polished PDF document. To find out more about the memoir JSON object, see `training.text`

### Pipeline:

```
LM Studio conversation JSON
        ↓
extract.py
        ↓
memoir JSON object
        ↓
main.py
        ↓
latex.py
        ↓
PDF output
```

## Project structure

```
Root/
│
├── main.py                  # Entry point of the application
├── extract.py              # Extracts memoir JSON from conversation logs
├── latex.py                # Converts memoir JSON → LaTeX / PDF
│
├── run_windows.bat         # Windows launcher (auto-detect Python + installer fallback)
├── run_unix.sh             # macOS/Linux launcher
│
├── TinyTeX/                # Bundled LaTeX distribution (XeLaTeX)
│
├── resources/
│   └── template.tex        # LaTeX template used for PDF generation
│
├── venv/                   # Python virtual environment (preconfigured)
│
└── python-3.14.6-amd64.exe # Optional Python installer for Windows fallback
```

## Requirements

Requires:

* Python 3.10+

Check:

```bash
python --version
```

or

```bash
python3 --version
```

## How to run

### Windows (recommended)

Run:

```bat
run_windows.bat
```

Behavior:

* Detects Python automatically
* If missing, launches bundled installer (`python-3.14.6-amd64.exe`)
* Runs `main.py`

### MacOS / Linux

Run:

```bash
chmod +x run_unix.sh
./run_unix.sh
```

Behavior:

* Checks for Python 3
* Warns if not installed
* Runs `main.py` if available

## Output

The system generates:

```
memoir-YYYY-MM-DD.pdf
```

Saved in the project root.

## Rendering system

* XeLaTeX (via TinyTeX)

## Core modules

### `main.py`

* Entry point
* Orchestrates extraction → rendering

### `extract.py`

* Parses LM Studio `.conversation.json`
* Extracts latest assistant memoir JSON

### `latex.py`

* Escapes LaTeX content
* Builds document body
* Compiles PDF using:

  * TinyTeX (XeLaTeX)
  * fallback HTML renderer

## TinyTeX setup

TinyTeX is included in:

```
TinyTeX/
```

No system installation required.

The program directly calls:

```
TinyTeX/bin/windows/xelatex.exe
```

## Notes

* This project assumes local file-based execution (not web service)
* Windows installer is bundled for convenience only
* Designed for offline document generation pipelines
