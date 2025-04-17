
class GameEntry:
    def __init__(self, name, score) -> None:
        self._name = name # Sets the name
        self._score = score # Sets the score

    # Not a single problem in below the functions:
    def get_name(self):
        return self._name
        
    def get_score(self):
        return self._score
    
    def __str__(self) -> str:
        return '({}, {})'.format(self._name, self._score)



# Class to get the working of the score board:

class Scoreboard(GameEntry):
    def __init__(self, name, score, capacity) -> None:
        super().__init__(name, score)
        self._board = [None]*capacity
        self._n = 0
        
    def get_item(self, k): # Returns the score at the index k
        return self._board[k]
    
    def __str__(self) -> str:
        '''Returns the string representation of the high score list'''
        return '\n'.join(str(self._board[j]) for j in range(self._n))
    
    # i don't know what the fuck is going on 
    
    def add(self, entry):
        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1
            j = self._n -1 
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry


# person = Scoreboard("shubham", )
