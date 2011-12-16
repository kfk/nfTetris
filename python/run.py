import item_from_file
import random

items_l=["LINE","LLINE","ILLINE","BLINE","SQUARE"]

def board():
	XLEN=20
	YLEN=20
	board_out=""
	board_l=[]
	for y in range(YLEN):
		l=[]
		if y+1 !=YLEN:
			for x in range(XLEN):
				if x == 0 or x == 19:
					l.append("*")
				else:
					l.append(" ")
		else:
			for x in range(XLEN):
				l.append("*")
		board_l.append(l)
	return board_l

def item_to_board(play_board, select, x, y, item_pos):
	item=item_from_file.get_item(select)
	board_l=play_board
	new_item=0
		
	if item_pos!=[] and y!=17:	
		for i in item_pos:
			board_l[i[0]][i[1]]=" "	
	
	item_pos=[]
	for fi in range(4):
		for si in range(4):
			pos=si+9
			if y==17:
				new_item=1
			if y<17:
				board_l[fi + y][pos + x]=item[fi][si]
				l=[]
				if item[fi][si]=="*":
					l.append(fi + y)
					l.append(pos + x)
					item_pos.append(l)
	return board_l, item_pos, new_item

def write_out(MATRIX):
	item_out=""
	for row in MATRIX:
			if len(row) != 0:
				for i in range(len(row)):
					item=row[i]	
					item_out+=str(item)
					if i+1==len(row):
						item_out+="\n"
	return item_out

def run(rot_cou, play_board, select,x,y,item_pos):
	if play_board==[]:
		play_board=board()
		play_board, item_pos, new_item =item_to_board(play_board,select,x,y, item_pos=[])
	print write_out(play_board)
	user_input =raw_input("""What you want to do?
			a - move piece left \n
			d - move piece right \n
			w - rotate piece counter clockwise\n
			s - rotate piece clockwise \n""")
	if user_input=="a":
		x-=1
	if user_input=="d":
		x+=1
	if user_input=="s":
		if rot_cou==4:
			rot_cou=0
		rot_cou+=1
		select[1]=str(rot_cou)
	if user_input=="w":
		if rot_cou>1:
			rot_cou = rot_cou - 1
		else:
			rot_cou = 4
		select[1]=str(rot_cou)
	y=y+1

	play_board, item_pos, new_item  = item_to_board(play_board,select,x,y, item_pos)
	if new_item==1:
		insert_new_item(play_board)
	#print write_out(play_board)
	run(rot_cou, play_board, select,x,y,item_pos)

def insert_new_item(play_board):
	select=[]
	select.append(random.choice(items_l))
	select.append("1")
	rot_cou=1
	run(rot_cou,play_board,select,x=0,y=0, item_pos=[])

insert_new_item(play_board=[])
