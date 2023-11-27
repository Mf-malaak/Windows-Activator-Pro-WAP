import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import platform
import subprocess
import os
import subprocess
import ctypes
import sys
from PIL import Image, ImageTk

root = tk.Tk()
root.attributes("-toolwindow")
root.title("WAPro")
root.geometry("275x265")
#root.iconbitmap("icon.ico") ##This for Icon
root.configure(bg="#064789")
root.resizable(False, False)
btn_bg_color = "#427aa1"
btn_bgg_color = "#064789"
btn_txt_color = "#ebf2fa"

def mini_size():
        root.geometry("275x265")
        tk.Button(root, width="2",relief="flat",height="1", fg=btn_txt_color, bg=btn_bgg_color,font=("Arial", 10, "bold"),text="[+]",command=resize,bd=0).place(x='2',y='240')
        return
def resize():
        root.geometry("275x600")
        tk.Button(root, width="2",relief="flat",height="1", fg=btn_txt_color, bg=btn_bgg_color,font=("Arial", 10, "bold"),text="[-]",command=mini_size,bd=0).place(x='2',y='240')
        return

tk.Button(root, width="2",relief="flat",height="1", fg=btn_txt_color, bg=btn_bgg_color,font=("Arial", 10, "bold"),text="[+]",command=resize,bd=0).place(x='2',y='240')

###########################################################
#Debugger detected, exiting program.
def Debugger_finder():
    return ctypes.windll.kernel32.IsDebuggerPresent()
if Debugger_finder():
    sys.exit()
###########################################################

txt_t = tk.Label(root,fg=btn_txt_color, bg=btn_bgg_color,font=("Arial",8, "bold"), text="W i n d o w s   A c t i v a t o r   P R O  [ W A P ]\nDev.Mina.lfn\n__________")#.place(x=5, y=0)
txt_t.pack()

# Create the first combobox for selecting the version
version_label = tk.Label(root,fg=btn_txt_color, bg=btn_bgg_color,font=("Arial",11, "bold"), text="Select Version*")#.place(x=5, y=0)
version_label.pack()

version_combobox = ttk.Combobox(root, values=["Windows 7", "Windows 8", "Windows 8.1", "Windows 10", "Windows 11"])
version_combobox.pack()

# Create the second combobox for selecting the edition
edition_label = tk.Label(root,fg=btn_txt_color, bg=btn_bgg_color,font=("Arial",11, "bold"), text="Select Edition*")#.place(x=5, y=30)
edition_label.pack()

edition_combobox = ttk.Combobox(root)#.place(x=90, y=30)
edition_combobox.pack()##, fill="y")

# Get Windows activation status information
def windows_activation_status():
    subprocess.check_output("slmgr.vbs /xpr", shell=True)

# Deactivate Windows
def deactivate_windows():
    selected_values_label["text"] = "Please Rester your PC\nto continue without ERROR"
    subprocess.check_output("slmgr.vbs /upk", shell=True)


# Reset  Windows
def resets_licensing_status_machine():
    selected_values_label["text"] = "Please Rester your PC\nto continue without ERROR"
    subprocess.check_output("slmgr.vbs /rearm", shell=True)


# Previous Activation Windows
def previous_activation():
    selected_values_label["text"] = "Please Rester your PC\nto continue without ERROR"
    subprocess.check_output("slmgr.vbs /ato", shell=True)
    

# Define a function to update the edition combobox options based on the selected version
def update_edition_options(event):
    selected_version = version_combobox.get()
    if selected_version == "Windows 7":
        edition_combobox["values"] = ["Home", "Home Single Language", "Professional", "Professional N", "Professional WMC", "Enterprice", "Enterprice N"]
    elif selected_version == "Windows 8":
        edition_combobox["values"] = ["Home", "Home Single Language", "Professional", "Professional N", "Professional WMC", "Enterprice", "Enterprice N"]
    elif selected_version == "Windows 8.1":
        edition_combobox["values"] = ["Home", "Home N", "Home Single Language", "Professional", "Professional N", "Professional WMC", "Enterprice", "Enterprice N"]
    elif selected_version == "Windows 10":
        edition_combobox["values"] = ["Home", "Home N", "Home Single Language", "Home Country Specific", "Professional", "Professional N", "Education", "Education N", "Enterprice", "Enterprice N"]
    elif selected_version == "Windows 11":
        edition_combobox["values"] = ["Home", "Home N", "Home Single Language", "Home Country Specific", "Professional", "Professional N", "Education", "Education N", "Enterprice", "Enterprice N"]

# Bind the function to the version combobox selection event
version_combobox.bind("<<ComboboxSelected>>", update_edition_options)

def tk_lable():
    return ctypes.windll.kernel32.IsDebuggerPresent()

if tk_lable():
    print("Debugger detected!")
else:
    print("No debugger detected.")
    


# Create a label to display the selected values
selected_values_label = tk.Label(root,fg=btn_txt_color, bg=btn_bgg_color,font=("Arial",9, "bold","italic"), text="")
selected_values_label.pack(padx=0, pady=53)


def windows_info():
# Get Windows version information using systeminfo command
    windows_info = subprocess.check_output("systeminfo | findstr /B \"OS Name\"", shell=True).decode() 
    windows_info = windows_info.replace("Microsoft", "")
    windows_info = windows_info.replace("OS Name:                    ", "")
    windows_info = windows_info.replace(" ", "")
    windows_info_lines = windows_info.split("\n")
    windows_info_lines = tk.Label(root, fg=btn_bgg_color, bg=btn_txt_color,font=("Arial",10, "bold"),text=windows_info_lines[0])
    windows_info_lines.pack()

def get_product_key():
    # VBScript to retrieve the product key
    vbs_script = """
    Set WshShell = CreateObject("WScript.Shell")
    MsgBox ConvertToKey(WshShell.RegRead("HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\DigitalProductId"))

    Function ConvertToKey(Key)
        Const KeyOffset = 52
        isWin8 = (Key(66) \ 6) And 1
        Key(66) = (Key(66) And &HF7) Or ((isWin8 And 2) * 4)
        i = 24
        Chars = "BCDFGHJKMPQRTVWXY2346789"
        Do
            Cur = 0
            x = 14
            Do
                Cur = Cur * 256
                Cur = Key(x + KeyOffset) + Cur
                Key(x + KeyOffset) = (Cur \ 24)
                Cur = Cur Mod 24
                x = x -1
            Loop While x >= 0
            i = i -1
            KeyOutput = Mid(Chars, Cur + 1, 1) & KeyOutput
            If (((29 - i) Mod 6) = 0) And (i <> -1) Then
                i = i -1
                KeyOutput = "-" & KeyOutput
            End If
        Loop While i >= 0
        ConvertToKey = KeyOutput
    End Function
    """

    # Save the VBScript to a temporary file
    with open("temp.vbs", "w") as f:
        f.write(vbs_script)

    # Run the VBScript and capture its output
    output = subprocess.check_output(["cscript", "//nologo", "temp.vbs"], encoding="utf-8")
    product_key = output.strip().split("\n")[-1]

    # Delete the temporary file
    os.remove("temp.vbs")



def display_about():
        about_message = """
    WAPro - Windows Activator PRO
    
    Version: 1.0
    
    Developed by: [m.Malaak]
    
    About:
    WAPro is a tool designed for educational purposes to demonstrate Windows activation mechanisms. 
    This tool is not intended for illegal use and should be used responsibly.
    
    Disclaimer:
    The developer holds no responsibility for any unauthorized use or consequences arising 
    from the use of this tool. Use it at your own risk.
    """
    # Display the About message using a messagebox
        messagebox.showinfo("About", about_message)


def display_help():
    help_message = """
    Welcome to WAPro - Windows Activator PRO!
    
    How to Use:
    1. Select the Windows version from the 'Select Version' dropdown.
    2. Choose the edition of the selected Windows version from the 'Select Edition' dropdown.
    3. Click 'Active Now!' to activate the chosen Windows version and edition.
    
    Additional Options:
    - 'Get Product Key': Retrieve the product key information.
    - 'Activation Status!': Check the current activation status of Windows.
    - 'Deactivate Windows': Deactivate the Windows activation.
    - 'Reset Key [Get Trial Activation]': Reset Windows licensing status.
    - 'Previous Activation': Restore the previous Windows activation.
    - 'Get Windows Version & Edition': View the Windows version and edition information.
    
    Note:
    - This script is for educational purposes only.
    - Usage for unauthorized activation of Windows may be illegal.
    - Please use at your own risk and responsibility.
    """
    messagebox.showinfo("Help", help_message)

# Define a function to update the label with the selected values and open a command prompt to execute a specific command based on the selected values
def update_selected_values():
    selected_version = version_combobox.get()
    selected_edition = edition_combobox.get()

    if not selected_version:
        selected_values_label["text"] = "Please select version!"
        return
    
    if not selected_edition:
        selected_values_label["text"] = "Please select edition!"
        return
    
    selected_values_label["text"] = f"Version: {selected_version}\nEdition: {selected_edition}\nActivated"
    
    
    # Open a command prompt and execute your specific command here based on the selected values
    ##                     Windows 7                        ##
    if selected_version == "Windows 7" and selected_edition == "Home":
        os.system("slmgr /ipk BN3D2-R7TKB-3YPBD-8DRP2-27GG4")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")

    elif selected_version == "Windows 7" and selected_edition == "Home Single Language":
        os.system("slmgr /ipk 2WN2H-YGCQR-KFX6K-CD6TF-84YXQ")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")

    elif selected_version == "Windows 7" and selected_edition == "Professional":
        os.system("slmgr /ipk NG4HW-VH26C-733KW-K6F98-J8CK4")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")

    elif selected_version == "Windows 7" and selected_edition == "Professional N":
        os.system("slmgr /ipk XCVCF-2NXM9-723PB-MHCB7-2RYQQ")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 7" and selected_edition == "Professional WMC":
        os.system("slmgr /ipk GNBB8-YVD74-QJHX6-27H4K-8QHDG")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 7" and selected_edition == "Enterprice":
        os.system("slmgr /ipk 32JNW-9KQ84-P47T8-D8GGY-CWCK7")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 7" and selected_edition == "Enterprice N":
        os.system("slmgr /ipk JMNMF-RHW7P-DMY6X-RF3DR-X2BQT")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")

    ##                     Windows 8                       ##
    if selected_version == "Windows 8" and selected_edition == "Home":
        os.system("slmgr /ipk BN3D2-R7TKB-3YPBD-8DRP2-27GG4")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")

    elif selected_version == "Windows 8" and selected_edition == "Home Single Language":
        os.system("slmgr /ipk 2WN2H-YGCQR-KFX6K-CD6TF-84YXQ")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")

    elif selected_version == "Windows 8" and selected_edition == "Professional":
        os.system("slmgr /ipk NG4HW-VH26C-733KW-K6F98-J8CK4")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")

    elif selected_version == "Windows 8" and selected_edition == "Professional N":
        os.system("slmgr /ipk XCVCF-2NXM9-723PB-MHCB7-2RYQQ")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 8" and selected_edition == "Professional WMC":
        os.system("slmgr /ipk GNBB8-YVD74-QJHX6-27H4K-8QHDG")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 8" and selected_edition == "Enterprice":
        os.system("slmgr /ipk 32JNW-9KQ84-P47T8-D8GGY-CWCK7")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 8" and selected_edition == "Enterprice N":
        os.system("slmgr /ipk JMNMF-RHW7P-DMY6X-RF3DR-X2BQT")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    ##                     Windows 8.1                       ##
    elif selected_version == "Windows 8.1" and selected_edition == "Home":
        os.system("slmgr /ipk M9Q9P-WNJJT-6PXPY-DWX8H-6XWKK")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 8.1" and selected_edition == "Home N":
        os.system("slmgr /ipk 7B9N3-D94CG-YTVHR-QBPX3-RJP64")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 8.1" and selected_edition == "Home Single Language":
        os.system("slmgr /ipk BB6NG-PQ82V-VRDPW-8XVD2-V8P66")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 8.1" and selected_edition == "Professional":
        os.system("slmgr /ipk GCRJD-8NW9H-F2CDX-CCM8D-9D6T9")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 8.1" and selected_edition == "Professional N":
        os.system("slmgr /ipk HMCNV-VVBFX-7HMBH-CTY9B-B4FXY")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 8.1" and selected_edition == "Professional WMC":
        os.system("slmgr /ipk 789NJ-TQK6T-6XTH8-J39CJ-J8D3P")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 8.1" and selected_edition == "Enterprice":
        os.system("slmgr /ipk MHF9N-XY6XB-WVXMC-BTDCT-MKKG7")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 8.1" and selected_edition == "Enterprice N":
        os.system("slmgr /ipk TT4HM-HN7YT-62K67-RGRQJ-JFFXW")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")

    ##                     Windows 10                       ##
    elif selected_version == "Windows 10" and selected_edition == "Home":
        os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 10" and selected_edition == "Home N":
        os.system("slmgr /ipk 3KHY7-WNT83-DGQKR-F7HPR-844BM")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 10" and selected_edition == "Home Single Language":
        os.system("slmgr /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 10" and selected_edition == "Home Country Specific":
        os.system("slmgr /ipk PVMJN-6DFY6-9CCP6-7BKTT-D3WVR")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 10" and selected_edition == "Professional":
        os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 10" and selected_edition == "Professional N":
        os.system("slmgr /ipk MH37W-N47XK-V7XM9-C7227-GCQG9")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 10" and selected_edition == "Education":
        os.system("slmgr /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 10" and selected_edition == "Education N":
        os.system("slmgr /ipk 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 10" and selected_edition == "Enterprice":
        os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 10" and selected_edition == "Enterprice N":
        os.system("slmgr /ipk DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")

    
    ##                     Windows 11                       ##
    elif selected_version == "Windows 11" and selected_edition == "Home":
        os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 11" and selected_edition == "Home N":
        os.system("slmgr /ipk 3KHY7-WNT83-DGQKR-F7HPR-844BM")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 11" and selected_edition == "Home Single Language":
        os.system("slmgr /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 11" and selected_edition == "Home Country Specific":
        os.system("slmgr /ipk PVMJN-6DFY6-9CCP6-7BKTT-D3WVR")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 11" and selected_edition == "Professional":
        os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 11" and selected_edition == "Professional N":
        os.system("slmgr /ipk MH37W-N47XK-V7XM9-C7227-GCQG9")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 11" and selected_edition == "Education":
        os.system("slmgr /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 11" and selected_edition == "Education N":
        os.system("slmgr /ipk 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 11" and selected_edition == "Enterprice":
        os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    elif selected_version == "Windows 11" and selected_edition == "Enterprice N":
        os.system("slmgr /ipk DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
    
    else:
        edition_combobox.set("Please select a Version first!")
# Create a button to print the selected values to the label and open a command prompt to execute a specific command based on the selected values
print_button = tk.Button(root, width="17",relief="flat",height="2",text="Active Now!", fg=btn_txt_color, bg=btn_bg_color,font=("Arial", 10, "bold"), command=update_selected_values).place(x="66",y="150")

# edge box
btn_frame = tk.Frame(root,bg=btn_txt_color, bd=2, relief="flat")
btn_frame.pack(padx=0, pady=0)
more_options = "More Options"
windows_version_label = tk.Label(btn_frame, width="17",height="1", fg=btn_bgg_color, bg=btn_txt_color,font=("Arial",15, "bold"),text=more_options)
windows_version_label.pack()
# But get activation status
print_button = tk.Button(btn_frame,relief="flat", width="25",height="1", fg=btn_txt_color,bg=btn_bg_color,font=("Arial", 10, "bold"),text="Get Product Key",command=get_product_key)
print_button.pack(padx=1, pady=1)
print_button = tk.Button(btn_frame,relief="flat", width="25",height="1", fg=btn_txt_color, bg=btn_bg_color,font=("Arial", 10, "bold"),text="Activation Status!", command=windows_activation_status)
print_button.pack(padx=1, pady=1)

# Btn Deactivate Windows
print_button = tk.Button(btn_frame,relief="flat", width="25",height="1", fg=btn_txt_color,bg=btn_bg_color,font=("Arial", 10, "bold"),text="Deactivate Windows", command=deactivate_windows)
print_button.pack(padx=1, pady=1)

# Btn Reset Windows License
print_button = tk.Button(btn_frame,relief="flat", width="25",height="1", fg=btn_txt_color,bg=btn_bg_color,font=("Arial", 10, "bold"),text="Reset Key [Get Trial Activation]", command=resets_licensing_status_machine)
print_button.pack(padx=1, pady=1)

# Btn Previous Activation Windows
print_button = tk.Button(btn_frame,relief="flat", width="25",height="1", fg=btn_txt_color,bg=btn_bg_color,font=("Arial", 10, "bold"),text="Previous Activation", command=previous_activation)
print_button.pack(padx=1, pady=1)

windows_version_label = tk.Button(btn_frame,relief="flat", width="25",height="1", fg=btn_txt_color,bg=btn_bg_color,font=("Arial", 10, "bold"), text="Get Windows Version & Edition",command=windows_info)
windows_version_label.pack()

about_button = tk.Button(btn_frame,relief="flat",fg=btn_bgg_color,bg=btn_txt_color,font=("Arial", 9, "bold"),text="About", command=display_about)
about_button.pack(side="left")

help_button = tk.Button(btn_frame,relief="flat",fg=btn_bgg_color,bg=btn_txt_color,font=("Arial", 9, "bold"), text="Help", command=display_help)
help_button.pack(side="right")

############################################################################################


def open_link1(event):
    import webbrowser
    webbrowser.open_new(r"https://github.com/Mf-malaak/Windows-Activator-Pro-WAP")

frame = tk.Frame(root)
frame.pack(side="bottom", anchor="c")

label1 = tk.Label(frame, text="Developer Github", bg=btn_txt_color, cursor="hand2")
label1.pack(side="left")
label1.bind("<Button-1>", open_link1)
root.mainloop()
