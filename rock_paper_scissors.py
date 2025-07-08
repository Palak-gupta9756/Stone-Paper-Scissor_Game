import tkinter as tk
import random

choices = ['Stone', 'Paper', 'Scissors']

def get_winner(player, computer):
    if player == computer:
        return "It's a Draw!"
    elif (player == "Stone" and computer == "Scissors") or \
         (player == "Paper" and computer == "Stone") or \
         (player == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"


def play(choice):
    computer_choice = random.choice(choices)
    result = get_winner(choice, computer_choice)

    player_choice_label.config(text=f"Your Choice: {choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)


window = tk.Tk()
window.title("Stone Paper Scissors Game")
window.geometry("450x400")
window.configure(bg="#e6f2ff")  

title = tk.Label(window, text="Stone Paper Scissors", font=("Helvetica", 22, "bold"), bg="#e6f2ff", fg="#003366")
                
title.pack(pady=20)


button_frame = tk.Frame(window, bg="#e6f2ff")
button_frame.pack(pady=10)

btn_style = {"width": 12, "font": ("Arial", 14), "bg": "#cce0ff", "fg": "#003366", "activebackground": "#99ccff"}

stone_btn = tk.Button(button_frame, text="Stone", command=lambda: play("Stone"), **btn_style)
stone_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", command=lambda: play("Paper"), **btn_style)
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", command=lambda: play("Scissors"), **btn_style)
scissors_btn.grid(row=0, column=2, padx=10)

player_choice_label = tk.Label(window, text="Your Choice: ", font=("Arial", 14),bg="#e6f2ff", fg="#003366")
                               
player_choice_label.pack(pady=10)

computer_choice_label = tk.Label(window, text="Computer's Choice: ", font=("Arial", 14),bg="#e6f2ff", fg="#003366")
                                 
computer_choice_label.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 16, "bold"),bg="#e6f2ff", fg="#ff3300") 
                        
result_label.pack(pady=20)


window.mainloop()
