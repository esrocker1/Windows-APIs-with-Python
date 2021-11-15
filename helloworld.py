import ctypes 
user_handle = ctypes.WinDLL("User32.dll") # creating a handle to user32.dll

k_handle = ctypes.WinDLL("Kernel32.dll")# creating a handle to kernel32.dll

hWnd  = None # creating the paramteres to be passed to the widnows API
lpText = "Will you"
lpCaption = "Hire Eshan "
utype = 0x00000001
response = user_handle.MessageBoxW(hWnd,lpCaption,lpText,utype)

error = k_handle.GetLastError()
if error != 0:#if successful it returns a null values
 print (error)
 exit(1)
 
if response ==1 :
 print("User will hire")
else:
 print("User will hire")
 

