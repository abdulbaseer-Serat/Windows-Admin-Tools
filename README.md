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
2. Write your `.py` script - **The Script already uploaded**
3. Test it (python file`.py`)

```bash
python Windows_Tools.py
```
4. Convert to EXE
   - To convert a `.py` file into an `.exe` file, you first need to install PyInstaller. To install it, open the `Command Prompt (CMD)` and run the following command:
    
    ```python
     pip install pyinstaller
    ```
    - Navigate to your file location by opening the folder where your script is saved.
      
    ```bash
   cd path\to\your\file
   for Example C:\Users\Serat\Desktop\AutoRun Commands\Windows_Tools>
    ```
   - Create the `.exe` file by running the following command:
    ```python
     pyinstaller --onefile --console Windows_Tools.py
      ```
    Explanation:
      --onefile → makes a single `.exe` file  --console → keeps your menu visible (important for your script)

   - Find EXE in:
     ```bash
     dist/Windows_Tools.exe
      ```
## ⚠️ Important Notes

Some features require administrative privileges. Always run the `.exe` file as an administrator.
```bash
Right-click → Run as Administrator
```
## 📦 Project Structure
```bash
Windows-Admin-Tool/
│
├── Windows_Tools.py
├── README.md
└── dist/
    └── Windows_Tools.exe
```

## 📜 License
This project is open-source and free to use.

## ⭐ Support
If you like this project:

- Star the repository ⭐
- Share it with others
- Contribute improvements

---
## 🧑‍💻 Developer

Abdulbaseer Serat - MS in Computer Sciences · Abasyn University  [GitHub](https://github.com/abdulbaseer-Serat) · [LinkedIn](https://linkedin.com/in/abdul-basir-serat-65b8201ab) · info.abdulbasir@gmail.com

---
