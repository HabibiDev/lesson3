from tkinter import *
from mygame.mygame import *

def restart(event):
	play_board = player.new_game()
	play_board = player.random_two_or_four(2)
	label_play_board['text'] = '{}\n{}\n{}\n{}'.format(play_board[3], play_board[2], play_board[1], play_board[0])
	return label_play_board

def up(event):
	play_board = player.move_up()
	label_play_board['text'] = '{}\n{}\n{}\n{}'.format(play_board[3], play_board[2], play_board[1], play_board[0])
	return label_play_board

def down(event):
	play_board = player.move_down()
	label_play_board['text'] = '{}\n{}\n{}\n{}'.format(play_board[3], play_board[2], play_board[1], play_board[0])
	return label_play_board

def left(event):
	play_board = player.move_left()
	label_play_board['text'] = '{}\n{}\n{}\n{}'.format(play_board[3], play_board[2], play_board[1], play_board[0])
	return label_play_board

def right(event):
	play_board = player.move_right()
	label_play_board['text'] = '{}\n{}\n{}\n{}'.format(play_board[3], play_board[2], play_board[1], play_board[0])
	return label_play_board

root = Tk()
root.minsize(width=700, height=250)
root.maxsize(width=700, height=250)
top_frame = Frame(root)
top_frame.pack()

play_board=[] 
for i in range(4):
    play_board.append([])
    for c in range(4):
        play_board[i].append(0)
player = Game(play_board)
print(list(zip(*play_board))[0][0])
play_board = player.random_two_or_four(2)
label_play_board = Label(top_frame, text='{}\n{}\n{}\n{}'.format(play_board[3], play_board[2], play_board[1], play_board[0]), font=('Courier', 20))
label_play_board.grid(row=0, column=0, columnspan=4, rowspan=4)

button_left=Button(top_frame, text='left', fg='black')
button_left.grid(row=5, column=0)
button_left.bind('<Button-1>', left)

button_down=Button(top_frame, text='down', fg='black')
button_down.grid(row=5, column=1)
button_down.bind('<Button-1>', down)

button_up=Button(top_frame, text='up', fg='black')
button_up.grid(row=5, column=2)
button_up.bind('<Button-1>', up)

button_right=Button(top_frame, text='right', fg='black')
button_right.grid(row=5, column=3)
button_right.bind('<Button-1>', right)

button_new_game=Button(top_frame, text='New game', fg='black')
button_new_game.grid(row=7, column=0, columnspan=4)
button_new_game.bind('<Button-1>', restart)

root.mainloop()
