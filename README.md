# OSINT Username Scanner

A Python-based OSINT tool designed to search for public username profiles across multiple websites and online platforms using Maigret.

The project aims to simplify username investigations by automating searches and organizing results into structured reports.

## Features

- Search usernames across hundreds of websites.
- Social media and community platform discovery.
- Developer and technology platform searches.
- HTML and JSON report generation.
- Organized investigation results.
- Cross-platform support.

## Requirements

- Python 3.10 or newer.
- Git.
- Internet connection.

## Installation

### Windows

**1. Install Python**

Download Python from:

https://www.python.org/downloads/windows/

During installation, enable **Add Python to PATH**.

**2. Clone the repository**

```bash
git clone https://github.com/SEU-USUARIO/OsintUsername.git
cd OsintUsername
```

**3. Create a virtual environment**

```bash
py -m venv venv
```

**4. Activate the environment**

```powershell
.\venv\Scripts\Activate.ps1
```

**5. Install dependencies**

```bash
py -m pip install -r requirements.txt
```

**6. Run the application**

```bash
py osint_username.py
```

### Kali Linux

**1. Update your system**

```bash
sudo apt update
```

**2. Install requirements**

```bash
sudo apt install python3 python3-pip python3-venv git -y
```

**3. Clone the repository**

```bash
git clone https://github.com/SEU-USUARIO/OsintUsername.git
cd OsintUsername
```

**4. Create a virtual environment**

```bash
python3 -m venv venv
```

**5. Activate the environment**

```bash
source venv/bin/activate
```

**6. Install dependencies**

```bash
pip install -r requirements.txt
```

**7. Run the application**

```bash
python3 osint_username.py
```

### Ubuntu / Debian

**1. Install requirements**

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git -y
```

**2. Clone the repository**

```bash
git clone https://github.com/SEU-USUARIO/OsintUsername.git
cd OsintUsername
```

**3. Create and activate the virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Run the application**

```bash
python3 osint_username.py
```

### macOS

**1. Install Python**

Download Python from:

https://www.python.org/downloads/macos/

**2. Clone the repository**

```bash
git clone https://github.com/SEU-USUARIO/OsintUsername.git
cd OsintUsername
```

**3. Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Run the application**

```bash
python3 osint_username.py
```

## Usage

After launching the application, enter the username you want to investigate.

Example:

```text
=======================================================
       OSINT - USERNAME SCANNER
=======================================================

Enter username: example_user

[+] Starting username search...
[+] Searching available platforms...
[+] Generating reports...
```

## Results

Search results are saved automatically in the `resultados_osint/` directory.

The application generates:

- HTML reports.
- JSON reports.
- Organized investigation folders.

## Technologies

- Python
- Maigret
- OSINT
- Git

## Disclaimer

This project is intended for educational purposes and authorized OSINT research.

Only publicly accessible information should be investigated. Respect website terms of service, privacy regulations, and applicable laws.

The existence of a profile cannot always be conclusively verified through automated searches. Results may include false positives or inconclusive matches.

## Author

**João Vitor Rosado**

GitHub: https://github.com/JVRosado

---

*Developed for learning, research, and responsible OSINT investigations.*