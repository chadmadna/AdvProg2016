#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk

class SubmitaTipForm(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)
        self.withdraw()     # hide until ready to show
        self.title("Submit a Tip")
        self.descText = ttk.Text(root, height=18, width=20)
        self.descText.grid(row=0, column=0, sticky=(tk.W, tk.E), padx="0.75m", pady="0.75m")
        self.descText.insert(END, "Use this electronic form to submit information regarding suspicious, nuisance and criminal activity to the Philadelphia Police Department. You may submit a tip anonymously.

If you are filling out a tip on a potential or wanted suspect, fill out as much information that you may know, including physical description, any known addresses, gang affiliations, and other locations where he/she may be found.

If you are reporting a crime in progress, or require emergency service, please dial 9-1-1, from a phone now.")
        self.subjectLabel = ttk.Label(self, text="Subject:")
        self.subjectLabel.grid(row=1, column=0, sticky=tk.W, padx="0.75m", pady="0.75m")
        self.subjectEntry = ttk.Entry(self)
        self.subjectEntry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx="0.75m", pady="0.75m")
        self.locationLabel = ttk.Label(self, text="Location:")
        self.locationLabel.grid(row=2, column=0, sticky=tk.W, padx="0.75m", pady="0.75m")
        self.locationEntry = ttk.Entry(self)
        self.locationEntry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx="0.75m", pady="0.75m")
        self.tipMessageLabel = ttk.Label(self, text="Tip/Message:")
        self.tipMessageLabel.grid(row=3, column=0, sticky=tk.W, padx="0.75m", pady="0.75m")
        self.tipEntry = ttk.Entry(self)
        self.tipEntry.grid(row=3, column=1, sticky=(tk.W, tk.E), padx="0.75m", pady="0.75m")
        self.submitButton = ttk.Button(self, text="Submit")
        self.submitButton.grid(row=4, column=0, padx="0.75m", pady="0.75m")
        self.bind("<Escape>", lambda *args: self.destroy())
        self.deiconify()    # show when widgets are created and laid out
        if self.winfo_viewable():
            self.transient(master)
        self.wait_visibility()
        self.grab_set()
        self.wait_window(self)

if __name__ == "__main__":
    application = tk.Tk()
    window = SubmitaTipForm(application)
    application.protocol("WM_DELETE_WINDOW", application.quit)
    application.mainloop()
