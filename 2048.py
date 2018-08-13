from tkinter import *
from logic2048 import Game

N = 4
color = {'' : 'light gray',
         2 : 'pink',
         4 : 'red',
         8 : 'orange',
         16: 'yellow',
         32: 'light blue',
         64: 'blue',
         128: 'light green',
         256: 'green'}


def left(event):
    game.left()
    draw(game)
    if game.game_over():
        print('GAME OVER')

def right(event):
    game.right()
    draw(game)
    if game.game_over():
        print('GAME OVER')
    
def up(event):
    game.up()
    draw(game)
    if game.game_over():
        print('GAME OVER')
    
def down(event):
    game.down()
    draw(game)
    if game.game_over():
        print('GAME OVER')

def draw(game):
    for i in range(N):
        for j in range(N):
            table[i][j]['text'] = game[i][j]
            try:
                table[i][j]['bg'] = color[game[i][j]]
            except KeyError:
                table[i][j]['bg'] = 'white'

root = Tk()
table = [[Label(root, height=2, width=4, font='Arial 24') for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        table[i][j].grid(row=i, column=j)

for i in range(N):
    root.grid_rowconfigure(i, pad=10)
    root.grid_columnconfigure(i, pad=10)

game = Game()
draw(game)
root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Up>', up)
root.bind('<Down>', down)
root.mainloop()