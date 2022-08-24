from UserInterfaceLayer import *
from tkinter import *

# Create object
splashScreen = Tk()
splashScreen.overrideredirect(True)

imgSematec = PhotoImage(file='Semateclogo.png')

# Adjust size
w = str(imgSematec.width())
h = str(imgSematec.height())
splashScreen.geometry(f'{w}x{h}')
# splashScreen.title('splash Screen')
# splashScreen.resizable(None, None)
positionRight = int(splashScreen.winfo_screenwidth() / 2 - 400 / 2)
positionDown = int(splashScreen.winfo_screenheight() / 2 - 100 / 2)
splashScreen.geometry("+{}+{}".format(positionRight, positionDown))

lblSematecImage = Label(splashScreen, image=imgSematec)
lblSematecImage.pack()


# main window function
def main():
    # destroy splash window
    splashScreen.destroy()
    login = LoginUI()
    login.loginFormLoad()


# Set Interval
splashScreen.after(500, main)

# Execute tkinter
splashScreen.mainloop()
