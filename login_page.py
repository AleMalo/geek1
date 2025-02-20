import tkinter as tk
from plansza import *
from settings import *

password1 = ''
chest_answers1 = []
password2 = ''
chest_answers2 = []

class LoginPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Log in')
        self.root.geometry('1440x810')
        self.root.configure(bg=PLAYER1COLOR1)
        self.root.resizable(False, False)

        # starting page

        self.game_title = tk.Label(self.root, text='[GAME NAME]', font=FONT1)
        self.game_title.configure(bg=PLAYER1COLOR1, fg=PLAYER1COLOR3)
        self.game_title.place(relx=0.5, rely=0.3, anchor='center')

        self.game_button = tk.Button(self.root, text='START', font=FONT2, bd=0, command=self.start_tk_game)
        self.game_button.configure(bg=PLAYER1COLOR2, fg=PLAYER1COLOR3, activebackground=PLAYER1COLOR3,
                                   activeforeground=PLAYER1COLOR2)
        self.game_button.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.333, relheight=0.1)

        self.how_button = tk.Button(self.root, text='HOW TO PLAY', font=FONT2, bd=0)
        self.how_button.configure(bg=PLAYER1COLOR2, fg=PLAYER1COLOR3, activebackground=PLAYER1COLOR3,
                                    activeforeground=PLAYER1COLOR2)
        self.how_button.place(relx=0.5, rely=0.625, anchor='center', relwidth=0.333, relheight=0.1)

        # login page elements - hidden at the start

        self.player_text = tk.Label(self.root, text='PLAYER 1', font=FONT1)
        self.player_text.configure(bg=PLAYER1COLOR1, fg=PLAYER1COLOR3)
        self.player_text.place(relx=0.5, rely=-0.25, anchor='center')

        self.enter_text = tk.Label(self.root, text='Enter your password:', font=FONT2)
        self.enter_text.configure(bg=PLAYER1COLOR1, fg=PLAYER1COLOR3)
        self.enter_text.place(relx=0.5, rely=-0.425, anchor='center')

        self.password_entry = tk.Entry(self.root, show='*', font=FONT2)
        self.password_entry.configure(bg=PLAYER1COLOR2, fg=PLAYER1COLOR1)
        self.password_entry.place(relx=0.5, rely=-0.5, anchor='center', relwidth=0.5, relheight=0.067)

        self.password_entry.bind('<Button-1>', self.erase_input)

        self.info_text = tk.Label(self.root, text=INFO, font=FONT2, justify='center')
        self.info_text.configure(bg=PLAYER1COLOR1, fg=PLAYER1COLOR3)
        self.info_text.place(relx=0.5, rely=-0.625, anchor='center')

        self.change_button = tk.Button(self.root, text='CONFIRM', font=FONT2, bd=0, command=self.change_players)
        self.change_button.configure(bg=PLAYER1COLOR2, fg=PLAYER1COLOR3, activebackground=PLAYER1COLOR3,
                                     activeforeground=PLAYER1COLOR2)
        self.change_button.place(relx=0.5, rely=-0.75, anchor='center', relwidth=0.333, relheight=0.067)

        self.start_button = tk.Button(self.root, text='CONFIRM', font=FONT2, bd=0, command=self.enter_game)
        self.start_button.configure(bg=PLAYER1COLOR2, fg=PLAYER1COLOR1, activebackground=PLAYER1COLOR1,
                                    activeforeground=PLAYER1COLOR2)
        self.start_button.place(relx=0.5, rely=-0.75, anchor='center', relwidth=0.333, relheight=0.067)

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
            self.change_button.place(rely=-0.75)
            self.start_button.place(rely=0.75)
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
            self.run_pygame_game()
            print(password2)
            chest_answers1 = [password1[:3], password1[3:6], password1[6:9], password1[9:12], password1[12:]]
            chest_answers2 = [password2[:3], password2[3:6], password2[6:9], password2[9:12], password2[12:]]

    def erase_input(self, event=None):
        if self.password_entry.cget('fg') == '#ff0000':
            self.password_entry.config(fg=PLAYER1COLOR1)
            self.password_entry.delete(0, tk.END)
            print('erased')

    def run_pygame_game(self):
        self.root.destroy()
        Plansza()

    def start_tk_game(self):
        self.game_title.place(rely=-0.3)
        self.game_button.place(rely=-0.5)
        self.how_button.place(rely=-0.625)
        self.player_text.place(rely=0.25)
        self.enter_text.place(rely=0.425)
        self.password_entry.place(rely=0.5)
        self.info_text.place(rely=0.625)
        self.change_button.place(rely=0.75)

LoginPage()
