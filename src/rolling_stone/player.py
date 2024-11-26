class Player:
    def __init__(self):
        self.score = 0
        self.name = None

    
    def receive_score(self, score):
        self.score = score

    def _get_name_for_player_from_input(self):
        return self.name
    
    def prompt_for_name(self):
        self.name = self._get_name_for_player_from_input()