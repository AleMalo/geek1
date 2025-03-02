import tkinter as tk
from settings import *


class WinnerPanel:
    def __init__(self, p1, p2):
        self.root = tk.Tk()
        self.root.title('Hacking')
        self.root.geometry('1440x810')
        self.root.configure(bg=GC1)
        self.root.resizable(False, False)

        self.correct_password1 = p1
        self.guessed_password1 = ''
        self.correct_password2 = p2
        self.guessed_password2 = ''

        # PLAYER 1

        self.p1_label = tk.Label(self.root, text='PLAYER 1', font=FONT2)
        self.p1_label.configure(bg=GC1, fg=GC3)
        self.p1_label.place(relx=0.25, rely=0.25, anchor='center')

        self.p1_enter_label = tk.Label(self.root, text='Enter the suspected password', font=FONT4)
        self.p1_enter_label.configure(bg=GC1, fg=GC3)
        self.p1_enter_label.place(relx=0.25, rely=0.3625, anchor='center')

        self.p1_password_entry = tk.Entry(self.root, show='*', font=FONT4)
        self.p1_password_entry.configure(bg=GC2, fg=GC3)
        self.p1_password_entry.place(relx=0.25, rely=0.45, relwidth=0.333, relheight=0.067, anchor='center')

        self.p1_info_label = tk.Label(self.root, text='password had the clues given in the game', font=FONT4)
        self.p1_info_label.configure(bg=GC1, fg=GC3)
        self.p1_info_label.place(relx=0.25, rely=0.5375, anchor='center')

        self.p1_input_button = tk.Button(self.root, text='INPUT', font=FONT3, bd=0)
        self.p1_input_button.configure(bg=GC2, fg=GC3, activebackground=GC3, activeforeground=GC2)
        self.p1_input_button.place(relx=0.25, rely=0.65, relwidth=0.25, height=75, anchor='center')

        # PLAYER 2

        self.p2_label = tk.Label(self.root, text='PLAYER 2', font=FONT2)
        self.p2_label.configure(bg=GC1, fg=GC3)
        self.p2_label.place(relx=0.75, rely=0.25, anchor='center')

        self.p2_enter_label = tk.Label(self.root, text='Enter the suspected password', font=FONT4)
        self.p2_enter_label.configure(bg=GC1, fg=GC3)
        self.p2_enter_label.place(relx=0.75, rely=0.3625, anchor='center')

        self.p2_password_entry = tk.Entry(self.root, show='*', font=FONT4)
        self.p2_password_entry.configure(bg=GC2, fg=GC3)
        self.p2_password_entry.place(relx=0.75, rely=0.45, relwidth=0.333, relheight=0.067, anchor='center')

        self.p1_info_label = tk.Label(self.root, text='password had the clues given in the game', font=FONT4)
        self.p1_info_label.configure(bg=GC1, fg=GC3)
        self.p1_info_label.place(relx=0.75, rely=0.5375, anchor='center')

        self.p1_input_button = tk.Button(self.root, text='INPUT', font=FONT3, bd=0)
        self.p1_input_button.configure(bg=GC2, fg=GC3, activebackground=GC3, activeforeground=GC2)
        self.p1_input_button.place(relx=0.75, rely=0.65, relwidth=0.25, height=75, anchor='center')

        # TOGETHER

        self.check_button = tk.Button(self.root, text='CHECK', font=FONT3, bd=0)
        self.check_button.configure(bg=GC2, fg=GC3, activebackground=GC3, activeforeground=GC2)
        self.check_button.place(relx=0.5, rely=0.85, relwidth=0.667, height=75, anchor='center')

        self.root.mainloop()

WinnerPanel()