import sqlite3
from dbconfig import NAME_COL, SCORE_COL, HIGHSCORES_TABLE_NAME, fetchAllSQL, executeSQL

class Scores(object):
    """ service class that offer abunch of db services 
        like create, remove, update, delete 
    """
    # user score
    curr_score = 0

    def __init__(self):
        self.curr_score = 0

    def add_to_score(self, amt=0, mul=1):
        """ method adds to current score 
            amt == how many pts to add
            mul == multiplier for bonus pts
        """
        self.curr_score += amt * mul

    def save_score(self, name="Player1"):
        """ method saves score to db 
            name == name of user
        """
        sql = "INSERT INTO Highscores VALUES (" + str(self.curr_score) + ", '" + name + "')"
        executeSQL(sql)

    def get_all_scores_and_names(self):
        """ method returns all scores in db 
            limit == how many scores you want
        """
        sql = "SELECT * FROM " + HIGHSCORES_TABLE_NAME;
        scores = fetchAllSQL(sql)
        return scores

    def get_scores_for_user(self, name="Player1"):
        """ method returns user scores 
            name == name of user
        """
        sql = "SELECT " + SCORE_COL + " FROM " + HIGHSCORES_TABLE_NAME + " WHERE " + NAME_COL + " = '" + name + "'"
        scores = fetchAllSQL(sql)
        return scores 

    def get_top_ten_scores(self):
        """ method returns top 10 high scores """
        scores = self.get_all_scores_and_names();
        scores.sort(key=lambda x: x[0], reverse=True)
        return scores[:10]

    def reset_score(self):
        """ method resets score """
        self.curr_score = 0
