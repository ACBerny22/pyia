import tkinter as tk
from tree_for_UI import *
from tkinter import messagebox
from tkinter import ttk


yellow_player = "⚪"
blue_player = "⚫"

root = tk.Tk()
s = ttk.Style()
s.theme_use('winnative')

progress = tk.IntVar()

s.configure("red.Horizontal.TProgressbar", foreground='white', background='black')
progressbar = ttk.Progressbar(orient=tk.HORIZONTAL, length=610, style='red.Horizontal.TProgressbar', variable=progress)


xs = 2
os = 2
progress.set(30)

# Example 8x8 board (initially filled with zeros)
board = [[' ' for _ in range(8)] for _ in range(8)]

board[3][3] = board[4][4] = yellow_player
board[3][4] = board[4][3] = blue_player

# Creating a nested list to store buttons
buttons = []

last_IA_pos = [0,0]

def count_blanks(board):
    count = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] == ' ':
                count += 1
    return count

def on_enter(event, row, col):
    if [row, col] != last_IA_pos:
        buttons[row][col].config(bg='DodgerBlue2')

def on_leave(event, row, col):
    if [row, col] != last_IA_pos:
        buttons[row][col].config(bg='white')

def upadte_buttons(buttons, board): 
    print("I can do the next moves:", get_all_valid_moves(board, '⚪'))
    if(len(get_all_valid_moves(board, '⚪')) == 0):
        if xs > os:
            messagebox.showinfo("Ganaste!!", "Chingon.") 
    for row in range(8):
        for col in range(8):
            if board[row][col] == 'ㅤ':
                buttons[row][col].config(text=str(" "))
            else:
                buttons[row][col].config(text=board[row][col])

def clear_buttons(buttons):
    for row in range(8):
        for col in range(8):
            buttons[row][col].config(bg="white")

def play(row, col):
    current_player = yellow_player
    # Update the board value at the given row and column
    # For example, you can change the board[row][col] here
    if(is_valid_move(board, row, col, current_player)):
        is_valid, xs, os = make_move(board, row, col, current_player)
        if is_valid:
            clear_buttons(buttons)
            upadte_buttons(buttons, board)
            current_player = blue_player
            root.update()  # Update the GUI

    else:
        print("Invalid move. Try again.")
        messagebox.showinfo("Movimiento Invalido", "Intenta otro movimiento.") 
    print(count_blanks(board))

    print(xs)
    print(os)
    
    progress.set((os*100)/(xs+os))
    root.update()  # Update the GUI

    # IA's Turn!!

    if current_player == blue_player:
        print("AI can do the next moves:", get_all_valid_moves(board, '⚫'))
        if(len(get_all_valid_moves(board, '⚫')) == 0):
            if os > xs:
                messagebox.showinfo("Gana la IA", "Chale, perdiste, ni modo pa, pa la otra.") 

        root_node = create_tree(board, current_player, 5)
        best_play_node, _ = find_best_play(root_node)
        #print_tree(root_node)
        print(f"Best Play: {best_play_node.move}, Score: {best_play_node.score}")
        row, col = best_play_node.move

        is_valid, xs, os = make_move(board, row, col, current_player)
        if is_valid:
            clear_buttons(buttons)
            upadte_buttons(buttons, board)
            buttons[row][col].config(bg = "khaki1")

            # Guardamos la casilla de la ultima posicion jugada de la IA
            last_IA_pos[0] = row
            last_IA_pos[1] = col

            current_player = blue_player
        else:
            print("Invalid move. Try again.")

    print(count_blanks(board))
    
    print(xs)
    print(os)
    progress.set((os*100)/(xs+os))
    print("The blacks have a:", (os*100)/(xs+os), "dominance")
    #root.update()  # Update the GUI

def main_UI():

    root.title("Othello")
    root.configure(bg='white')


    # Create a label on top of the button grid
    label = tk.Label(root, text="Let´s Play Othello!!", font=("Arial", 18))
    label.grid(row=0, column=0, columnspan=8)  # Span the label across the grid width
  
    for i in range(8):
        row_buttons = []
        for j in range(8):           
            # Create a button and assign a command to update its value
            btn = tk.Button(root, text=str(board[i][j]), command=lambda row=i, col=j: play(row, col), font=("Noto Color Emoji", 35), 
                            bg="white")
            btn.grid(row=i+1, column=j)
            btn.bind("<Enter>", lambda event, row=i, col=j: on_enter(event, row, col))
            btn.bind("<Leave>", lambda event, row=i, col=j: on_leave(event, row, col))
            row_buttons.append(btn)
        buttons.append(row_buttons)

    progressbar.grid(row=9, column=0, columnspan=8)
    print("The blacks have a:", (os*100)/(xs+os), "dominance")
    progressbar.step(10)

    root.mainloop()


main_UI()
