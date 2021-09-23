from AVL_Tree_player import Player,Tree,print2D,AVL_from_list,PreOrder,InOrder,PostOrder,search
from random import randrange,randint
    
def players_list_creation():
    players_list = []

    for i in range(100):
        player = Player()
        players_list.append(player)
    
    return players_list
    
def random_score(players):
    for player in players:
        player.score += randint(0,12)
    return players

def update_score(tree,players_list):
    tree.root = None
    for p in players_list:
        tree.root = tree.insert(tree.root, p)
    return tree.root

def assignement_completed(game_list):
    for i in range(len(game_list)):
        if(len(game_list[i])!=10):
            return False
    return True
            

def random_assignment(root,game_list):
    curr = root
    if(curr==None or assignement_completed(game_list)):
        return
    else:
        random_assignment(curr.left,game_list)
        random_assignment(curr.right,game_list)
        index = randrange(0,10)
        while(len(game_list[index])==10):
            index = randrange(0,10)
        game_list[index].append(curr.val)
        

def ranking_assigment(root,game_list):
    curr = root
    if(curr==None or assignement_completed(game_list)):
        return
    else:
        index = 0
        ranking_assigment(curr.left,game_list)
        if(len(game_list[index])==10):
            index += 1
        game_list[index].append(curr.val)
        ranking_assigment(curr.right,game_list)
        
def ranking_games(tree,nb_games):
    game_list = []
    for i in range(nb_games):
        game_list.append([])
    ranking_assigment(tree.root,game_list)
    return game_list
    
def random_games(tree):
    game_list = []
    for i in range(10):
        game_list.append([])
    random_assignment(tree.root, game_list)
    return game_list
  
     
def eliminated_players_list(root,eliminated_players):
    curr = root
    if(curr==None):
        return
    else:
        eliminated_players_list(curr.left,eliminated_players)
        if(len(eliminated_players)<10):
            eliminated_players.append(curr.val)
        eliminated_players_list(curr.right,eliminated_players)
        
    return eliminated_players

def remove_by_id(id,list):
    for i in range(len(list)):
        if (list[i].id == id):
            list.remove(list[i])
            break
    return list

def drop_players(tree,eliminated_players,players_list):
    for p in eliminated_players:
        eliminated_players = remove_by_id(p.id, players_list)
    return tree,players_list

def winners(root):
    curr = root
    if(curr==None):
        return
    else:
        winners(curr.right)
        print(curr.val.to_string())
        winners(curr.left)
        
        
if __name__ == "__main__":
    #initialisation
    players_list = players_list_creation()
    players_tree = Tree()
    players_tree.root = update_score(players_tree,players_list)
    #print2D(players_tree.root)
    
    #random games
    for i in range(3):
        #creation de partie
        game_list  = random_games(players_tree)
        random_assignment(players_tree.root,game_list)
        #update
        for g in game_list:
            random_score(g)
        players_tree.root = update_score(players_tree,players_list)
    #ranked games        
    nb_games=10
    while(len(players_list)>10):
        game_list = ranking_games(players_tree,nb_games)
        nb_games -=1
        ranking_assigment(players_tree.root,game_list)
        for g in game_list:
            random_score(g)
        players_tree.root = update_score(players_tree,players_list)
        #eliminer des joueurs
        eliminated_players = []
        eliminated_players_list(players_tree.root,eliminated_players)
        players_tree,players_list = drop_players(players_tree, eliminated_players, players_list) 
        players_tree.root = update_score(players_tree,players_list)
        
    #final game
    game_list = ranking_games(players_tree,1) 
    ranking_assigment(players_tree.root,game_list)
    for g in game_list:
           random_score(g)
    players_tree.root = update_score(players_tree,players_list)
    #methode pour afficher  l'arbre dans la console
    #print2D(players_tree.root)
    
    print("-------------winners----------")
    
    winners(players_tree.root)
    
    
    #print2D(players_tree.root)
    
    
    print("---------------------------")
        
        
        
        
    
    
    