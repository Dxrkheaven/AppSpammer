from tkinter import *

window = Tk()
window.geometry( "600x300" )
window.config( bg = "#333333" )
window.title( "App spammer" )

def spamWindows():
    for _ in range(20):
        anoWin = window.Toplevel(window)
        anoWin.title( "Just another window." )
        anoWin.geometry( "600x300" )
        
        closeButton = Button( anoWin, text = "Click to close", command = anoWin.destroy )
        closeButton.place( x = 20, y = 20 )

Label( window, text = "App spammer", bg = "#333333", fg = "#ffffff" ).pack()
Button( window, text = "Click to start", bg = "#333333", fg = "#ffffff", command = spamWindows ).pack()

window.mainloop()
