import tkinter as tk
import time
from settings import *

password1 = ''
password2 = ''

class LoginPage():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Log in')
        self.root.geometry('600x600')
        self.root.configure(bg=PLAYER1COLOR1)
        self.root.resizable(False, False)

        self.player_text = tk.Label(self.root, text='PLAYER 1', font=FONT1)
        self.player_text.configure(bg=PLAYER1COLOR1, fg=PLAYER1COLOR3)
        self.player_text.place(relx=0.5, rely=0.25, anchor='center')

        self.enter_text = tk.Label(self.root, text='Enter your password:', font=FONT2)
        self.enter_text.configure(bg=PLAYER1COLOR1, fg=PLAYER1COLOR3)
        self.enter_text.place(relx=0.5, rely=0.425, anchor='center')

        self.password_entry = tk.Entry(self.root, show='*', font=FONT2)
        self.password_entry.configure(bg=PLAYER1COLOR2, fg=PLAYER1COLOR1)
        self.password_entry.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5, relheight=0.067)

        self.password_entry.bind('<Button-1>', self.erase_input)

        self.info_text = tk.Label(self.root, text=INFO, font=FONT2, justify='center')
        self.info_text.configure(bg=PLAYER1COLOR1, fg=PLAYER1COLOR3)
        self.info_text.place(relx=0.5, rely=0.625, anchor='center')

        self.player_1_button = tk.Button(self.root, text='CONFIRM', font=FONT2, bd=0, command=self.change_players)
        self.player_1_button.configure(bg=PLAYER1COLOR2, fg=PLAYER1COLOR3, activebackground=PLAYER1COLOR3, activeforeground=PLAYER1COLOR2)
        self.player_1_button.place(relx=0.5, rely=0.75, anchor='center', relwidth=0.333, relheight=0.067)

        self.player_2_button = tk.Button(self.root, text='CONFIRM', font=FONT2, bd=0, command=self.enter_game)
        self.player_2_button.configure(bg=PLAYER1COLOR2, fg=PLAYER1COLOR1, activebackground=PLAYER1COLOR1, activeforeground=PLAYER1COLOR2)
        self.player_2_button.place(relx=0.5, rely=-0.75, anchor='center', relwidth=0.333, relheight=0.067)

        self.root.mainloop()

    def change_players(self):
        password1 = self.password_entry.get()
        if not CHECK_WITH_RULES(password1):
            self.password_entry.config(fg='#ff0000')
            self.root.focus()
            self.password_entry.bind('<Button-1>', self.erase_input)
            print('password is wrong')
        else:
            self.root.configure(bg=PLAYER1COLOR3)
            self.player_text.config(text='PLAYER 2', bg=PLAYER1COLOR3, fg=PLAYER1COLOR1)
            self.enter_text.config(bg=PLAYER1COLOR3, fg=PLAYER1COLOR1)
            self.password_entry.config(fg=PLAYER1COLOR1)
            self.info_text.config(bg=PLAYER1COLOR3, fg=PLAYER1COLOR1)
            self.player_1_button.place(rely=-0.75)
            self.player_2_button.place(rely=0.75)
            self.password_entry.delete(0, tk.END)
            print(password1)

    def enter_game(self):
        password2 = self.password_entry.get()
        if not CHECK_WITH_RULES(password2):
            self.password_entry.config(fg='#ff0000')
            self.root.focus()
            self.password_entry.bind('<Button-1>', self.erase_input)
            print('password is wrong')
        else:
            self.info_text.config(text='☺')
            print(password1)

    def erase_input(self, event=None):
        if self.password_entry.cget('fg') == '#ff0000':
            self.password_entry.config(fg=PLAYER1COLOR1)
            self.password_entry.delete(0, tk.END)
            print('erased')
