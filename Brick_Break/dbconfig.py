import sqlite3

HIGHSCORES_FILE = "highscores.db"
HIGHSCORES_TABLE_NAME = "Highscores"
SCORE_COL = "Score"
NAME_COL = "Name"
COL_TYPE_1 = "Text"
COL_TYPE_2 = "Int"
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS " + HIGHSCORES_TABLE_NAME + " ( " + SCORE_COL + " " + COL_TYPE_2 + ", " + NAME_COL + " " + COL_TYPE_1 + ")"

_conn = sqlite3.connect(HIGHSCORES_FILE)
_context = _conn.cursor()
_context.execute(CREATE_TABLE)

_conn.commit()
_conn.close()

def executeSQL(sql):
    """ executes a sql command """
    _conn = sqlite3.connect('highscores.db', timeout=2)
    _context = _conn.cursor()
    _context.execute(sql)
    if _context.rowcount == 0:
        _conn.commit()
        _conn.close()
        return False
    _conn.commit()
    _conn.close()

def fetchAllSQL(sql):
    """ fetches sql data """
    data = []
    _conn = sqlite3.connect('highscores.db', timeout=1)
    _context = _conn.cursor()
    _context.execute(sql)
    data = _context.fetchall()
    _conn.close()
    return data