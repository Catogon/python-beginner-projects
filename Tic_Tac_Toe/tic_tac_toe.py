import tkinter
import tkinter.messagebox
from functools import partial


DEFAULT = ''
PLAYER = ('X', 'O')
COLOR = {
    # (background, foreground)
    PLAYER[0]: ('white', 'red'),
    PLAYER[1]: ('white', 'blue')
}
SIZE = 3

root = tkinter.Tk()
root.title('Tic Tac Toe')

button = {}
# Initiate a 2D list with DEFAULT values
board = [[DEFAULT for x in range(SIZE)] for x in range(SIZE)]
turn = 0


def init_button():
    # Create all buttons and put them in a dictionary (button) with a key based
    # on their position (row, column)
    for r in range(SIZE):
        for c in range(SIZE):
            button[(r, c)] = tkinter.Button(root, height=5, width=10,
                                            text=DEFAULT, font='Arial 13 bold',
                                            command=partial(click, (r, c)))
            button[(r, c)].grid(row=r, column=c)


def click(pos):
    if button[pos]['text'] == DEFAULT:
        global turn
        turn += 1
        curr_player = PLAYER[0] if turn % 2 != 0 else PLAYER[1]
        bg, fg = COLOR[curr_player]
        button[pos].configure(text=curr_player, background=bg, foreground=fg)
        # Update board
        board[pos[0]][pos[1]] = button[pos]['text']
        winner = get_winner()
        if winner is not None or turn == SIZE**2:
            result = 'Draw!' if winner is None else f'Winner: {winner}'
            tkinter.messagebox.showinfo('Game Over', result)
            disable()


# Generate all index combinations to check the winner
def win_index(n):
    # Horizontal
    for r in range(n):
        yield ((r, c) for c in range(n))
    # Vertical
    for c in range(n):
        yield ((r, c) for r in range(n))
    # Diagonal
    yield ((x, x) for x in range(n))
    yield ((x, n - x - 1) for x in range(n))


def get_winner():
    for i in win_index(SIZE):
        row = [board[r][c] for r, c in i]
        if len(set(row)) == 1 and DEFAULT not in row:
            return row[0]
    return None


def disable():
    for b in button.values():
        b.configure(state='disabled')


if __name__ == "__main__":
    init_button()
    root.mainloop()
