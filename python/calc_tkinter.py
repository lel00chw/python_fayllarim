import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.expression = ""
        self.widgets()
        
    def widgets(self):
        self.display = tk.Entry(self.root, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
        self.display.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        ayxan = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", "C", "=", "+"]
        ]

        for row in ayxan:
            frame = tk.Frame(self.root)
            frame.pack(expand=True, fill="both")
            for btn_text in row:
                button = tk.Button(frame, text=btn_text, font=("Arial", 18), command=lambda b=btn_text: self.tiklama(b))
                button.pack(side="left", expand=True, fill="both")

    def tiklama(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += str(char)
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    proqram = Calculator(root)
    root.mainloop()

