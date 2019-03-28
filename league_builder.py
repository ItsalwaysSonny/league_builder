import csv 

def read_csv(filename):
    lines = []
    with open (filename, mode='r') as file:
        lines = file.readlines()
    lines = lines[1:]
    players = {}
    for line in lines:
        name, height, exp, guardians = line.split(',')
        players[name] = [height, exp, guardians]
    return players 
        

def sort_players(ep):
    exp = []
    no_exp = []
    for k, v in ep.items():
        if v[1].upper() == 'YES':
            exp.append(k)
        if v[1].upper() == 'NO':
            no_exp.append(k)
    return exp, no_exp

def assign_exp_players(exp_players):
    sharks,dragons, raptors = [], [], []
    players_per_team = len(exp_players)//3
    sharks = exp_players[:players_per_team]
    dragons = exp_players [players_per_team :2*players_per_team]
    raptors = exp_players [2*players_per_team :3*players_per_team]
    return (sharks,dragons,raptors)

def assign_no_exp_players(no_exp_players):
    sharks,dragons, raptors = [], [], []
    players_per_team = len(no_exp_players)//3
    sharks = no_exp_players[:players_per_team]
    dragons = no_exp_players [players_per_team :2*players_per_team]
    raptors = no_exp_players [2*players_per_team :3*players_per_team]
    return (sharks,dragons,raptors)
    
    
    
    
    
    
    
    
if __name__=='__main__':
    players = read_csv('soccer_players.csv')
    exp_players, no_exp_players = sort_players(players)
    sharks, dragons, raptors = assign_exp_players(exp_players)
    sharks2, dragons2, raptors2, = assign_no_exp_players(no_exp_players)
    sharks = sharks + sharks2
    dragons = dragons + dragons2
    raptors = raptors + raptors2
    print(sharks,dragons,raptors)
    with open('teams.txt', 'w') as file:                        
        file.write('Sharks\n')                                    
        for player in sharks:                                   
             file.write(player + ', ' + players[player][1] + ', ' + players[player][2])  
    with open('teams.txt', 'a') as file:                        
        file.write('Raptors\n')                                    
        for player in raptors:                                   
             file.write(player + ', ' + players[player][1] + ', ' + players[player][2])
    with open('teams.txt', 'a') as file:                        
        file.write('Dragons\n')                                    
        for player in dragons:                                   
             file.write(player + ', ' + players[player][1] + ', ' + players[player][2])  
    for player in raptors:
        name = player.split(" ")
        filename= f"{name[0]}_{name[1]}.txt"
        s = f"Dear {players[player][2]} \n{player} is on the raptors, and his or her first practice is on  march, 27th 2019"
        with open(filename, 'a') as file:
            file.write(s)
    for player in dragons:
        name = player.split(" ")
        filename= f"{name[0]}_{name[1]}.txt"
        s = f"Dear {players[player][2]} \n{player} is on the dragons, and his or her first practice is on  march, 27th 2019"
        with open(filename, 'a') as file:
            file.write(s)
    for player in sharks:
        name = player.split(" ")
        filename= f"{name[0]}_{name[1]}.txt"
        s = f"Dear {players[player][2]} \n{player} is on the sharks, and his or her first practice is on  march, 27th 2019"
        with open(filename, 'a') as file:
            file.write(s)