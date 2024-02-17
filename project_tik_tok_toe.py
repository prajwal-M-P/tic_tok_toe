import tkinter as tk

window = tk.Tk()  # Create the main window
window.title("Tic Tac Toe")  # Set the window title

buttons = []  # List to store the game buttons

for i in range(3):
    for j in range(3):
        button = tk.Button(
            window, text=" ", font=("Arial", 40), width=3, height=1, command=lambda r=i, c=j: click_button(r, c)
        )
        button.grid(row=i, column=j)
        buttons.append(button)

def click_button(row, col):
    global player
    if buttons[row * 3 + col]["text"] == " ":
        buttons[row * 3 + col]["text"] = player
        check_winner()
        switch_player()

def check_winner():
    global winner
    # Check for horizontal wins
    for i in range(3):
        if buttons[i * 3]["text"] == buttons[i * 3 + 1]["text"] == buttons[i * 3 + 2]["text"] != " ":
            winner = buttons[i * 3]["text"]
            display_winner()
            return
    # Check for vertical wins
    for i in range(3):
        if buttons[i]["text"] == buttons[i + 3]["text"] == buttons[i + 6]["text"] != " ":
            winner = buttons[i]["text"]
            display_winner()
            return
    # Check for diagonal wins
    if buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"] != " ":
        winner = buttons[0]["text"]
        display_winner()
        return
    if buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"] != " ":
        winner = buttons[2]["text"]
        display_winner()
        return
    # Check for a tie
    if all(button["text"] != " " for button in buttons):
        winner = "Tie"
        display_winner()

def switch_player():
    global player
    player = "X" if player == "O" else "O"

def display_winner():
    label = tk.Label(window, text=f"{winner} wins!", font=("Arial", 40))
    label.grid(row=3, column=0, columnspan=3)

player = "X"  # Start with player X
winner = None

window.mainloop()  # Start the main event loop

