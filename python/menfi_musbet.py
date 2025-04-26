num = int(input('Eded daxil edin:'))
if num > 0:
    print('Eded musbetdir.')
elif num < 0:
    print('Eded menfidir.')
else:
    print('Eded sifirdir.')
#for row in ayxan:
#            frame = tk.Frame(self.root)
#            frame.pack(expand=True, fill="both")
#            for btn_text in row:
#                button = tk.Button(frame, text=btn_text, font=("Arial", 18), command=lambda b=btn_text: self.on_button_click(b))
#                button.pack(side="left", expand=True, fill="both")
#
#    def on_button_click(self, char):
#        if char == "C":
#            self.expression = ""
#        elif char == "=":
#            try:
#                self.expression = str(eval(self.expression))
#            except Exception as e:
#                self.expression = "Error"
#        else:
#            self.expression += str(char)
#        self.update_display()
#
#    def update_display(self):
#        self.display.delete(0, tk.END)
#        self.display.insert(tk.END, self.expression)
#
#
#if __name__ == "__main__":
#    root = tk.Tk()
#    app = Calculator(root)
#    root.mainloop()
#