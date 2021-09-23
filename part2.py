
from random import randint
class Point:
    id = 0
    def __init__(self):
        self.id = Point.id
        self.color = "sus-2nd-imp"
        self.bridge = []
        Point.id += 1
   
    def to_string(self):
        text = "Id : " + str(self.id )+ "\n" + "Bridge :"
        for i in range(len(self.bridge)):
            text += " Id : " + str(self.bridge[i].id) + " , "
        text += "\n" "Color :" + self.color
        return text

def make_bridge(point1,point2):
    point1.bridge.append(point2)
    point2.bridge.append(point1)

def get_player_by_id(id,players):
    for i in range(len(players)):
        if(players[i].id == id):
            return players[i]
    
def dead(id,players):
    players.remove(get_player_by_id(id,players))
    return players

def make_connexions(co_per_player,players):    
    for p in players:
        for i in range(co_per_player):
            make_bridge(p,(players[randint(0,len(players)-1)]))
    return players

def suspicious (dead_player,players):
    sus = []
    safe = []
    for p in dead_player.bridge:
        sus.append(p)
    for p in sus:
        for b in p.bridge:
            safe.append(b)
    for p in safe:
        p.color = "safe"
    for p in sus :
        p.color = "sus-killer"
    dead_player.color = "dead"
        
def print_players(players):
    for p in players :
        print(p.to_string())
        print()
        
        
def impostors(players):
    impostors=[]
    for p in players:
        if(p.color!="safe" and p.color!="dead"):
            impostors.append(p)
    return impostors

if __name__ == "__main__":
    #initilisation
    players=[]
    for i in range(10):
        players.append(Point())
    
    #connexion
    make_connexions(2, players)
    dead_player = get_player_by_id(0,players)
    suspicious(dead_player, players)
    print_players(players)
    
    
    print("possible impostors : ")
    print_players(impostors(players))