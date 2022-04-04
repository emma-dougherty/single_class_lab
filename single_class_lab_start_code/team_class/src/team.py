class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0
        
    def add_player (self, new_player):
        self.players.append(new_player)
        
    def has_player (self, name_to_check):
        for player in self.players:
            if name_to_check == player:
                return True
        else:
            return False
            
    def play_game (self, won_or_lost):
        if won_or_lost == True:
            self.points += 3
