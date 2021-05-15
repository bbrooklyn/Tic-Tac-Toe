from guizero import App, Text, Waffle

app = App(title="Tic-Tac-Toe Game")

# Globals
player = 1
win = False

title = Text(app, text="Tic-Tac-Toe Game",size=20)
description = Text(app, text="2 Players, local play only, online implementation coming soon.",size=10)
turn = Text(app,text="Player 1's turn",size=10,color="Red")

def tictac(x,y):
    global player
    global win
    if not win:
        if player == 1:
            colour = "Red"
            if waffle.get_pixel(x,y) == "Blue":
                return
            else:
                waffle.set_pixel(x,y,colour)
        else:
            colour = "Blue"
            if waffle.get_pixel(x,y) == "Red":
                return
            else:
                waffle.set_pixel(x,y,colour)
        values = 0
        # Check Y Axis - for vetical win
        for v in range(0,3):
            if waffle.get_pixel(x,v) == colour:
                values += 1    
        if values == 3: win = True
        values = 0
        # Check X Axis - for horizontal win
        for v in range(0,3):
            if waffle.get_pixel(v,y) == colour:
                values += 1
        if values == 3: win = True
        values = 0
        # Corner Checks - for diagonal win
        if waffle.get_pixel(1,1) == colour:
            for v in range(0,3,2):
                if waffle.get_pixel(v,0) == colour:
                    if v == 0:
                        if waffle.get_pixel(2,2) == colour:
                            win = True
                    else:
                        if waffle.get_pixel(0,2) == colour:
                            win = True
        if win:
            w = 'Player %s has won!'%player
            print(w)
            Text(app,text=w,color=colour)
            turn.visible = False
            return
        if player == 1:
            player = 2
            turn.value = "Player %s's turn"%player
            turn.text_color = "Blue"
        else:
            player = 1
            turn.value = "Player %s's turn"%player
            turn.text_color = "Red"
    
waffle = Waffle(app,dim=50,command=tictac)
app.display()
