import tkinter as tk
from tkinter import messagebox
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Bilimsel Hesap Makinesi")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        # Input Frame
        input_frame = self.create_input_frame()
        input_frame.pack(side=tk.TOP)

        # Buttons Frame
        btns_frame = self.create_buttons_frame()
        btns_frame.pack()

    def create_input_frame(self):
        frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        frame.pack(side=tk.TOP)

        input_field = tk.Entry(frame, font=('arial', 24, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=15) # interior padding to increase height
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        
        # Button Layout
        # Row 1
        self.create_button(frame, "C", 1, 0, 1, 1, "#ffcccc", lambda: self.btn_clear())
        self.create_button(frame, "/", 1, 1, 1, 1, "#fff", lambda: self.btn_click("/"))
        self.create_button(frame, "*", 1, 2, 1, 1, "#fff", lambda: self.btn_click("*"))
        self.create_button(frame, "x²", 1, 3, 1, 1, "#eee", lambda: self.btn_click("**2"))

        # Row 2
        self.create_button(frame, "7", 2, 0, 1, 1, "#fff", lambda: self.btn_click("7"))
        self.create_button(frame, "8", 2, 1, 1, 1, "#fff", lambda: self.btn_click("8"))
        self.create_button(frame, "9", 2, 2, 1, 1, "#fff", lambda: self.btn_click("9"))
        self.create_button(frame, "-", 2, 3, 1, 1, "#fff", lambda: self.btn_click("-"))

        # Row 3
        self.create_button(frame, "4", 3, 0, 1, 1, "#fff", lambda: self.btn_click("4"))
        self.create_button(frame, "5", 3, 1, 1, 1, "#fff", lambda: self.btn_click("5"))
        self.create_button(frame, "6", 3, 2, 1, 1, "#fff", lambda: self.btn_click("6"))
        self.create_button(frame, "+", 3, 3, 1, 1, "#fff", lambda: self.btn_click("+"))

        # Row 4
        self.create_button(frame, "1", 4, 0, 1, 1, "#fff", lambda: self.btn_click("1"))
        self.create_button(frame, "2", 4, 1, 1, 1, "#fff", lambda: self.btn_click("2"))
        self.create_button(frame, "3", 4, 2, 1, 1, "#fff", lambda: self.btn_click("3"))
        self.create_button(frame, "√", 4, 3, 1, 1, "#eee", lambda: self.btn_sqrt())

        # Row 5
        self.create_button(frame, "0", 5, 0, 1, 2, "#fff", lambda: self.btn_click("0")) # Span 2 cols
        self.create_button(frame, ".", 5, 2, 1, 1, "#fff", lambda: self.btn_click("."))
        self.create_button(frame, "=", 5, 3, 1, 1, "#ccffcc", lambda: self.btn_equal())

        # Row 6 (Scientific)
        self.create_button(frame, "sin", 6, 0, 1, 1, "#e6f2ff", lambda: self.btn_scientific("sin"))
        self.create_button(frame, "cos", 6, 1, 1, 1, "#e6f2ff", lambda: self.btn_scientific("cos"))
        self.create_button(frame, "tan", 6, 2, 1, 1, "#e6f2ff", lambda: self.btn_scientific("tan"))
        self.create_button(frame, "π", 6, 3, 1, 1, "#e6f2ff", lambda: self.btn_click(str(math.pi)))

        # Row 7 (Scientific)
        self.create_button(frame, "(", 7, 0, 1, 1, "#e6f2ff", lambda: self.btn_click("("))
        self.create_button(frame, ")", 7, 1, 1, 1, "#e6f2ff", lambda: self.btn_click(")"))
        self.create_button(frame, "log", 7, 2, 1, 1, "#e6f2ff", lambda: self.btn_scientific("log"))
        self.create_button(frame, "exp", 7, 3, 1, 1, "#e6f2ff", lambda: self.btn_scientific("exp"))

        return frame

    def create_button(self, frame, text, row, col, rowspan, colspan, bg, command):
        tk.Button(frame, text=text, width=7*colspan, height=3, bd=0, bg=bg, cursor="hand2",
                  command=command).grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=1, pady=1, sticky="nsew")
        
        # Configure grid weight to make buttons expand evenly
        frame.grid_columnconfigure(col, weight=1)
        frame.grid_rowconfigure(row, weight=1)

    def btn_click(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def btn_clear(self):
        self.expression = ""
        self.input_text.set("")

    def btn_equal(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except ZeroDivisionError:
            self.input_text.set("Hata")
            self.expression = ""
        except SyntaxError:
            self.input_text.set("Hata")
            self.expression = ""
        except Exception as e:
            self.input_text.set("Hata")
            self.expression = ""

    def btn_sqrt(self):
        try:
            result = str(math.sqrt(float(eval(self.expression))))
            self.input_text.set(result)
            self.expression = result
        except Exception:
            self.input_text.set("Hata")
            self.expression = ""

    def btn_scientific(self, func_name):
        try:
            value = float(eval(self.expression))
            if func_name == "sin":
                result = str(math.sin(math.radians(value))) # Assuming degree input for convenience
            elif func_name == "cos":
                result = str(math.cos(math.radians(value)))
            elif func_name == "tan":
                result = str(math.tan(math.radians(value)))
            elif func_name == "log":
                result = str(math.log10(value))
            elif func_name == "exp":
                result = str(math.exp(value))
            
            self.input_text.set(result)
            self.expression = result
        except Exception:
            self.input_text.set("Hata")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
