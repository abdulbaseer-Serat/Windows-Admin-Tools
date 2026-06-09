import os
import subprocess

def run(cmd):
    subprocess.run(cmd, shell=True)

def pause():
    os.system("pause")

while True:
    os.system("cls")
    print("=" * 57)
    print("        Menu-based Windows admin tool")
    print("            Windows System Admin Tool\n")
    print("        Developed by: Abdul Baseer SERAT")
    print("          Senior ICT Officer - NE ACTED")
    print("=" * 57)

    print("\n-------- CORE ADMIN --------")
    print(" [ 1] Computer Management")
    print(" [ 2] Disk Management")
    print(" [ 3] Event Viewer")
    print(" [ 4] Services")
    print(" [ 5] Device Manager")
    print(" [ 6] Task Manager")
    print(" [ 7] Registry Editor")
    print(" [ 8] Local Users and Groups")

    print("\n-------- SYSTEM INFO & CONTROL --------")
    print(" [ 9] System Information")
    print(" [10] System Configuration (MSCONFIG)")
    print(" [11] Control Panel")
    print(" [12] God Mode")
    print(" [13] Advanced System Properties")
    print(" [14] Environment Variables")

    print("\n-------- PERFORMANCE & DIAGNOSTICS --------")
    print(" [15] Performance Monitor")
    print(" [16] Resource Monitor")
    print(" [17] Reliability Monitor")
    print(" [18] DirectX Diagnostic Tool")
    print(" [19] Windows Memory Diagnostic")

    print("\n-------- DISK & STORAGE --------")
    print(" [20] Disk Cleanup")
    print(" [21] Check Disk (CHKDSK)")
    print(" [22] Defragment / Optimize Drives")
    print(" [23] Storage Spaces")
    print(" [24] Volume Shadow Copy")

    print("\n-------- SECURITY --------")
    print(" [25] Windows Defender")
    print(" [26] Firewall (Advanced)")
    print(" [27] Local Security Policy")
    print(" [28] Group Policy Editor")
    print(" [29] Credential Manager")

    print("\n-------- NETWORK --------")
    print(" [30] Network Connections")
    print(" [31] Network Reset")
    print(" [32] IP Configuration (IPCONFIG)")
    print(" [33] Windows Firewall Logs")

    print("\n-------- WINDOWS UPDATE & FEATURES --------")
    print(" [34] Windows Update Settings")
    print(" [35] Optional Features")
    print(" [36] Installed Updates")

    print("\n-------- BOOT & RECOVERY --------")
    print(" [37] Startup Folder")
    print(" [38] Recovery Options")
    print(" [39] System Restore")
    print(" [40] Boot Configuration (BCDEDIT)")

    print("\n-------- ADVANCED TOOLS --------")
    print(" [41] Power Options")
    print(" [42] Task Scheduler")
    print(" [43] Windows Terminal (Admin)")
    print(" [44] Command Prompt (Admin)")
    print(" [45] PowerShell (Admin)")

    print("\n [ 0] Exit\n")

    choice = input("Select an option: ").strip()

    commands = {
        "1": "compmgmt.msc",
        "2": "diskmgmt.msc",
        "3": "eventvwr.msc",
        "4": "services.msc",
        "5": "devmgmt.msc",
        "6": "taskmgr",
        "7": "regedit",
        "8": "lusrmgr.msc",

        "9": "msinfo32",
        "10": "msconfig",
        "11": "control",
        "12": "explorer shell:::{ED7BA470-8E54-465E-825C-99712043E01C}",
        "13": "sysdm.cpl",
        "14": "rundll32 sysdm.cpl,EditEnvironmentVariables",

        "15": "perfmon",
        "16": "resmon",
        "17": "perfmon /rel",
        "18": "dxdiag",
        "19": "mdsched.exe",

        "20": "cleanmgr",
        "21": "powershell Start-Process cmd -Verb runAs -ArgumentList '/k chkdsk'",
        "22": "dfrgui",
        "23": "control /name Microsoft.StorageSpaces",
        "24": "vssadmin list shadows",

        "25": "windowsdefender:",
        "26": "wf.msc",
        "27": "secpol.msc",
        "28": "gpedit.msc",
        "29": "control /name Microsoft.CredentialManager",

        "30": "ncpa.cpl",
        "31": "ms-settings:network-reset",
        "32": "powershell ipconfig /all; pause",
        "33": "explorer %systemroot%\\system32\\LogFiles\\Firewall",

        "34": "ms-settings:windowsupdate",
        "35": "optionalfeatures",
        "36": "control update",

        "37": "shell:startup",
        "38": "ms-settings:recovery",
        "39": "rstrui",
        "40": "powershell Start-Process cmd -Verb runAs -ArgumentList '/k bcdedit'",

        "41": "powercfg.cpl",
        "42": "taskschd.msc",
        "43": "powershell Start-Process wt -Verb runAs",
        "44": "powershell Start-Process cmd -Verb runAs",
        "45": "powershell Start-Process powershell -Verb runAs"
    }

    if choice == "0":
        break

    if choice in commands:
        run(commands[choice])
    else:
        print("Invalid selection!")

    pause()