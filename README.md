# 🧰 Menu-based Windows admin tool

A powerful Python-based Windows administration toolkit with a user-friendly console menu.  
This tool provides quick access to essential Windows utilities, diagnostics, networking, and security tools.

---


## 🚀 Features

✅ One-click access to core Windows tools  
✅ Organized categories (Admin, Network, Security, Performance, etc.)  
✅ Lightweight and portable  
✅ Works as Python script or standalone EXE  
✅ Designed for system administrators and IT support  

---

## 📂 Menu Categories

- 🔧 Core Admin Tools (Computer Mgmt, Services, Registry, etc.)
- 📊 System Information & Control
- ⚡ Performance & Diagnostics
- 💾 Disk & Storage Management
- 🔐 Security Tools
- 🌐 Network Utilities
- 🔄 Windows Update & Features
- 🛠 Advanced Tools

---

## 🖥 Requirements (For Python version)

- Python 3.x  
- Windows OS  

---

## ✅ Workflow
🔹 Step-by-step:

1. Install Python
2. Write your .py script - **The Script already uploaded**
3. Test it (python file.py)

```bash
python Windows_Tools.py
```
4. Convert to EXE
   - To Convert .py file into .EXE firts Install PyInstaller and to install *PyInstaller** Open Command Prompt (CMD) and run:
    ```python
     pip install pyinstaller
    ```
    - Navigate to your file location: Go to the folder where your script is saved:
    ```bash
   cd path\to\your\file
   for Example C:\Users\Serat\Desktop\AutoRun Commands\Windows_Tools>
    ```
   - Create the EXE file: Run this command:
    ```python
     pyinstaller --onefile --console Windows_Tools.py
      ```
    Explanation:

--onefile → makes a single .exe file
--console → keeps your menu visible (important for your script)
   - Find EXE in:
     dist/Windows_Tools.exe
