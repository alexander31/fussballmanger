class Level(object):
    def __init__(self,text):
        self.lines=len(text.splitlines())
        self.cols=len(text.splitlines()[1])
        self.text=text
        
levels=[]
players=[]
levels.append(Level('''
+-----------------------------------------------------------------+
|                                .                                |
|                                .                                |
|----------|                     .                     |----------|
|          |                     .                     |          |
|          |                    ...                    |     -----|
|----|     |                   .    .                  |     |    |
|--  |     |                  .      .                 |     |  --|
|    |     |                  .      .                 |     |    |
|    |     |                   .    .                  |     |    |
|--  |     |                    ...                    |     |  --|
|    |     |                     .                     |     |    |
|----|     |                     .                     |     |----|
|          |                     .                     |          |
|----------|                     .                     |----------|
|                                .                                |
|                                .                                |
+-----------------------------------------------------------------+
'''))

level=0



        

#65 Zeilen lang

class Player(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
players.append(Player(34,10))
def main():
    while True:
        x=0
        y=0
        for line in levels[level].text.splitlines():
            textline = ""
            x=0
            for char in line:
                for player in players:
                    if player.x==x and player.y==y:
                        textline+='$'
                    else:
                        textline+=char
                    x+=1
                
            print textline
            y+=1
        print ('Bitte W,A,S,D tippen')
        kommando=raw_input().lower()
        if kommando=='w':
            players[0].y-=1
        if kommando=='s':
            players[0].y+=1
        if kommando=='a':
            if players[0].x>0:
                players[0].x-=1
        if kommando=='d':
            if players[0].x< levels[level].cols-1:
                players[0].x+=1
        if kommando=='q':
            break
        
main()
