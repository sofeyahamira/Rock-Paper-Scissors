import tkinter as tk
import random
from colorama import Fore

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("300x300")

welcome = tk.Label(text="Welcome to this game of Rock Paper Scissors.\nTo play, choose rock, paper or scissors.")
welcome.pack()
#keeping scores
user_score = 0
computer_score = 0
# options
options = ['rock', 'paper', 'scissors']

def scissors():
  num = random.randint(0,2)
  computer_choice = options[num]
  if computer_choice == 'scissors':
    result = tk.Label(text="It's a draw!")
    result.pack()
  if computer_choice == 'rock':
    result = tk.Label(text="computer played rock and won!", fg="red")
    result.pack()
    global computer_score
    computer_score += 1
  if computer_choice == 'paper':
    result = tk.Label(text="computer played paper and lost!", fg="green")
    result.pack()
    global user_score
    user_score += 1
def rock():
  num = random.randint(0,2)
  computer_choice = options[num]
  if computer_choice == 'rock':
    result = tk.Label(text="It's a draw!")
    result.pack()
  if computer_choice == 'paper':
    result = tk.Label(text="computer played paper and won!", fg="red")
    result.pack()
    global computer_score
    computer_score += 1
  if computer_choice == 'scissors':
    result = tk.Label(text="computer played scissors and lost!", fg="green")
    result.pack()
    global user_score
    user_score += 1
def paper():
  num = random.randint(0,2)
  computer_choice = options[num]
  if computer_choice == 'paper':
    result = tk.Label(text="It's a draw!")
    result.pack()
  if computer_choice == 'scissors':
    result = tk.Label(text="computer played scissors and won!", fg="red")
    result.pack()
    global computer_score
    computer_score += 1
  if computer_choice == 'rock':
    result = tk.Label(text="computer played paper and lost!", fg="green")
    result.pack()
    global user_score
    user_score += 1

rock_button = tk.Button(text="Rock", command=rock)
rock_button.pack()

paper_button = tk.Button(text="Paper", command=paper)
paper_button.pack()

scissors_button = tk.Button(text="Scissors", command=scissors)
scissors_button.pack()
