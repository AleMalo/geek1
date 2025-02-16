import tkinter as tk


class Winnerpanel:
    def __init__(self, winner):
        self.root = tk.Tk()
        self.root.title('Winner')
        self.root.geometry('800x600')
        self.root.resizable(False, False)

        winner_text = f"Winner: {winner} !"
        self.label = tk.Label(self.root, text=winner_text, font=("Arial bold", 50), fg="hot pink")
        self.label.pack(expand=True)

        # self.play_again_button = tk.Button(self.root, text="Play Again", command=self.play_again, font=("Arial", 20), fg='pink')
        # self.play_again_button.pack(pady=20)
        #
        self.root.mainloop()
        #
        # def play_again(self):
        #
        #     self.root.destroy()


winner = "Player 1"
panel = Winnerpanel(winner)
