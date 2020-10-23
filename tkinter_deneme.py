import tkinter as tk
from tkinter import filedialog
import pandas as pd
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.check_string = tk.Text()
        self.check_string.pack(side="top")
        self.check_string.configure(height=20)

        self.convert_string_but = tk.Button(text="Convert string", command=self.convert_string)
        self.convert_string_but.pack(side="top")

        self.widgt = tk.Frame()
        self.widgt.pack(side="left")

        self.check_file_but = tk.Button(self.widgt, text="Select json file", command=self.check_file)
        self.check_file_but.pack()

        self.info_lab = tk.Label(text="CHOSED :")
        self.info_lab.pack(side="left")

        self.convert_file_but = tk.Button(self.widgt, text="Convert File", command=self.convert_file)
        self.convert_file_but.pack()


    def check_file(self):
        self.file_name = filedialog.askopenfilename()
        self.info_lab.config(text="CHOSED : {}".format(self.file_name))

    def convert_string(self):
        self.json_data = pd.read_json(self.check_string.get(1.0, "end"))
        self.export = filedialog.asksaveasfilename(defaultextension=".csv")
        self.json_data.to_csv(self.export)
        messagebox.showinfo("SUCCESFULL", "Succesfully created")


    def convert_file(self):
        with open(self.file_name) as f:
            self.json_file_data = pd.read_json(f)
            self.export = filedialog.asksaveasfilename(defaultextension=".csv")
            self.json_file_data.to_csv(self.export)
            
        messagebox.showinfo("SUCCESFULL", "Succesfully created")



if __name__ == "__main__":
    app = App()
    app.geometry("600x460")
    app.title("JSON to CSV")
    app.resizable(False, False)
    app.mainloop()
