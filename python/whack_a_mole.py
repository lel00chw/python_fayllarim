import tkinter as tk
import random

class WhackAMole:
    def __init__(self, root):
        self.root = root
        self.root.title("Whack-A-Mole")
        self.score = 0
        self.time_left = 60
        self.canvases = []  
        self.widgets()
        self.update_timer()  
        self.spawnpoint()
    
    def widgets(self):
        self.score_label = tk.Label(self.root, text=f"Score:{self.score}", font=("Arial", 14))
        self.score_label.pack()
        
        self.time_label = tk.Label(self.root, text=f"Time Left: {self.time_left}", font=("Arial", 14))
        self.time_label.pack()

        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack()

        for i in range(3):
            row = []
            for j in range(3):
                canvas = tk.Canvas(self.grid_frame, width=100, height=100, bg="lightgreen", highlightthickness=1, highlightbackground="black")
                canvas.grid(row=i, column=j, padx=5, pady=5)
                canvas.bind("<Button-1>", lambda event, x=i, y=j: self.whack_mole(x, y))  
                row.append(canvas)  
            self.canvases.append(row)  

    def spawnpoint(self):
        for row in self.canvases:  
            for canvas in row:
                canvas.config(bg="white")
        self.mole_x = random.randint(0, 2)
        self.mole_y = random.randint(0, 2)
        self.canvases[self.mole_x][self.mole_y].config(bg="black")  

    def whack_mole(self, x, y):
        if x == self.mole_x and y == self.mole_y:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.spawnpoint()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Time Left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        for row in self.canvases:  
            for canvas in row:
                canvas.unbind("<Button-1>")
        self.time_label.config(text="Vaxt bitti!")
        self.grid_frame.pack_forget()
        tk.Label(self.root, text=f"Final Score: {self.score}", font=("Arial", 16)).pack()

if __name__ == "__main__":
    root = tk.Tk()  
    game = WhackAMole(root)
    root.mainloop()