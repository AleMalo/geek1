import tkinter as tk
from tkinter import *
from plansza import *
from settings import *

class LoginPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Log in')
        self.root.geometry('1440x810')
        self.root.configure(bg=GC1)
        self.root.resizable(False, False)

        self.p1 = ''
        self.password1 = ''
        self.chest_answers1 = []
        self.password2 = ''
        self.chest_answers2 = []
        self.player_on = 1

        # START PAGE

        # text

        self.game_title = tk.Label(self.root, text='[GAME NAME]', font=FONT2)
        self.game_title.configure(bg=GC1, fg=GC3)
        self.game_title.place(relx=0.5, rely=0.3, anchor='center')

        # buttons

        self.game_button = tk.Button(self.root, text='START', font=FONT3, bd=0, command=self.start_tk_game)
        self.game_button.configure(bg=GC2, fg=GC3, activebackground=GC3,
                                   activeforeground=GC2)
        self.game_button.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.333, height=75)

        self.how_button = tk.Button(self.root, text='HOW TO PLAY', font=FONT3, bd=0, command=self.open_how)
        self.how_button.configure(bg=GC2, fg=GC3, activebackground=GC3,
                                  activeforeground=GC2)
        self.how_button.place(relx=0.5, rely=0.625, anchor='center', relwidth=0.333, height=75)


        # 'HOW TO PLAY' PAGE

        # images

        self.chest_open1_image = PhotoImage(file='images/co1_big.PNG')
        self.chest_closed1_image = PhotoImage(file='images/cc1_big.PNG')
        self.chest_open2_image = PhotoImage(file='images/co2_big.PNG')
        self.chest_closed2_image = PhotoImage(file='images/cc2_big.PNG')
        self.player1_image = PhotoImage(file='images/hacker1.PNG')
        self.player2_image = PhotoImage(file='images/hacker2.PNG')

        self.co1_label = tk.Label(self.root, image=self.chest_open1_image, borderwidth=0)
        self.co1_label.place(x=1231, y=-662, anchor='center')
        self.cc1_label = tk.Label(self.root, image=self.chest_closed1_image, borderwidth=0)
        self.cc1_label.place(x=1070, y=-442, anchor='center')
        self.p1_label = tk.Label(self.root, image=self.player1_image, borderwidth=0)
        self.p1_label.configure(bg=GC1)
        self.p1_label.place(x=920, y=-185, anchor='center')

        self.co2_label = tk.Label(self.root, image=self.chest_open2_image, borderwidth=0)
        self.co2_label.place(x=1231, y=-676, anchor='center')
        self.cc2_label = tk.Label(self.root, image=self.chest_closed2_image, borderwidth=0)
        self.cc2_label.place(x=1070, y=-456, anchor='center')
        self.p2_label = tk.Label(self.root, image=self.player2_image, borderwidth=0)
        self.p2_label.configure(bg=GC1)
        self.p2_label.place(x=920, y=-185, anchor='center')

        # text

        self.rules_label = tk.Label(self.root, text=RULES, font=FONT4)
        self.rules_label.configure(bg=GC1, fg=GC3)
        self.rules_label.place(relx=0.25, y=-343.75, anchor='center')

        self.p1_images_label = tk.Label(self.root, text='Player 1 Elements', font=FONT3)
        self.p1_images_label.configure(bg=GC1, fg=GC3)
        self.p1_images_label.place(relx=0.75, y=-56, anchor='center')

        self.p2_images_label = tk.Label(self.root, text='Player 2 Elements', font=FONT3)
        self.p2_images_label.configure(bg=GC1, fg=GC3)
        self.p2_images_label.place(relx=0.75, y=-56, anchor='center')

        # button

        self.back_button = tk.Button(self.root, text='BACK', font=FONT3, borderwidth=0, command=self.return_to_start)
        self.back_button.configure(bg=GC2, fg=GC3, activebackground=GC3, activeforeground=GC2)
        self.back_button.place(relx=0.5, y=-760, relwidth=0.33, height=75, anchor='center')


        # PASSWORD ENTERING

        # text

        self.player_text = tk.Label(self.root, text='PLAYER 1', font=FONT2)
        self.player_text.configure(bg=GC1, fg=GC3)
        self.player_text.place(relx=0.5, rely=-0.25, anchor='center')

        self.enter_text = tk.Label(self.root, text='Enter your password:', font=FONT4)
        self.enter_text.configure(bg=GC1, fg=GC3)
        self.enter_text.place(relx=0.5, rely=-0.425, anchor='center')

        self.info_text = tk.Label(self.root, text=INFO, font=FONT4, justify='center')
        self.info_text.configure(bg=GC1, fg=GC3)
        self.info_text.place(relx=0.5, rely=-0.625, anchor='center')

        # entry

        self.password_entry = tk.Entry(self.root, show='*', font=FONT4)
        self.password_entry.configure(bg=GC2, fg=GC3)
        self.password_entry.place(relx=0.5, rely=-0.5, anchor='center', relwidth=0.5, relheight=0.067)

        # buttons

        self.password_entry.bind('<Button-1>', self.erase_input)

        self.change_button = tk.Button(self.root, text='CONFIRM', font=FONT3, bd=0, command=self.change_players)
        self.change_button.configure(bg=GC2, fg=GC3, activebackground=GC3,
                                     activeforeground=GC2)
        self.change_button.place(relx=0.5, rely=-0.75, anchor='center', relwidth=0.333, height=75)

        self.start_button = tk.Button(self.root, text='CONFIRM', font=FONT3, bd=0, command=self.enter_game)
        self.start_button.configure(bg=GC2, fg=GC3, activebackground=GC3,
                                    activeforeground=GC2)
        self.start_button.place(relx=0.5, rely=-0.75, anchor='center', relwidth=0.333, height=75)

        self.root.mainloop()

    def change_players(self):
        self.password1 = self.password_entry.get()
        if not CHECK_WITH_RULES(self.password1):
            self.password_entry.config(fg='#ff0000')
            self.root.focus()
            # self.password_entry.bind('<Button-1>', self.erase_input)
            print('password is wrong')
        else:
            self.player_on = 2
            self.player_text.config(text='PLAYER 2')
            self.password_entry.delete(0, tk.END)
            self.p1 = self.password1
            self.chest_answers1 = [self.p1[:3], self.p1[3:6], self.p1[6:9], self.p1[9:12], self.p1[12:]]
            print(self.p1, self.password1, self.chest_answers1)

    def enter_game(self):
        self.password2 = self.password_entry.get()
        print(self.p1, self.password1)
        if not CHECK_WITH_RULES(self.password2):
            self.password_entry.config(fg='#ff0000')
            self.root.focus()
            # self.password_entry.bind('<Button-1>', self.erase_input)
            print('password is wrong', self.password1)
        else:
            self.chest_answers1 = [self.p1[:3], self.p1[3:6], self.p1[6:9], self.p1[9:12], self.p1[12:]]
            self.chest_answers2 = [self.password2[:3], self.password2[3:6], self.password2[6:9], self.password2[9:12], self.password2[12:]]
            print(self.p1, self.password1, self.password2, self.chest_answers1, self.chest_answers2)
            self.run_pygame_game()

    def erase_input(self, event=None):
        if self.password_entry.cget('fg') == '#ff0000':
            if self.player_on == 1:
                self.password_entry.config(fg=P1C1)
            if self.player_on == 2:
                self.password_entry.config(fg=P2C3)
            self.password_entry.delete(0, tk.END)
            print('erased')

    def run_pygame_game(self):
        self.root.destroy()
        Plansza(self.chest_answers1, self.chest_answers2)

    def start_tk_game(self):
        self.root.config(bg=GC1)
        self.game_title.place(rely=-0.3)
        self.game_button.place(rely=-0.5)
        self.how_button.place(rely=-0.625)
        self.player_text.place(rely=0.25)
        self.enter_text.place(rely=0.425)
        self.password_entry.place(rely=0.5)
        self.info_text.place(rely=0.625)
        self.change_button.place(rely=0.75)

    def open_how(self):
        self.game_title.place(rely=-0.3)
        self.game_button.place(rely=-0.5)
        self.how_button.place(rely=-0.625)

        self.rules_label.place(y=343.75)
        self.p1_images_label.place(y=76)
        self.p2_images_label.place(y=377)
        self.back_button.place(y=725)

        self.co1_label.place(y=205)
        self.cc1_label.place(y=205)
        self.p1_label.place(y=205)
        self.co2_label.place(y=510)
        self.cc2_label.place(y=510)
        self.p2_label.place(y=510)

    def return_to_start(self):
        self.game_title.place(rely=0.3)
        self.game_button.place(rely=0.5)
        self.how_button.place(rely=0.625)

        self.rules_label.place(y=-343.75)
        self.p1_images_label.place(y=-76)
        self.p2_images_label.place(y=-377)
        self.back_button.place(y=-725)

        self.co1_label.place(y=-205)
        self.cc1_label.place(y=-205)
        self.p1_label.place(y=-205)
        self.co2_label.place(y=-510)
        self.cc2_label.place(y=-510)
        self.p2_label.place(y=-510)


LoginPage()
