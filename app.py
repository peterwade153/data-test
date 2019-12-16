
import logging
import sqlite3

from flask import Flask, render_template
from sqlite3 import Error


db = "./database.db" #SQLite database is used for this task, this is document that is easy to use and no installations required

app = Flask(__name__)
app.config['DEBUG'] = True


# Referenced this resource for the handler below -->  https://gitlab.com/abarad/sqlite-python-logging-handler
class SQLiteHandler(logging.Handler):
    """
    Handler which extends the logging handler. This sends the log records to the SQLite database.
    Creates a table with columns for all attributes in the log record and inserts the values in the table.
    """
    _sql_create_log_table = "CREATE TABLE IF NOT EXISTS log ('name', 'msg', 'args', 'levelname', 'levelno', 'pathname', 'filename', 'module', 'exc_info', 'exc_text', 'stack_info', 'lineno', 'funcName', 'created', 'msecs', 'relativeCreated', 'thread', 'threadName', 'processName', 'process', 'message');"
    _sql_insert = "INSERT INTO log ('name', 'msg', 'args', 'levelname', 'levelno', 'pathname', 'filename', 'module', 'exc_info', 'exc_text', 'stack_info', 'lineno', 'funcName', 'created', 'msecs', 'relativeCreated', 'thread', 'threadName', 'processName', 'process', 'message') VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

    def __init__(self, db="./database.db"):
        logging.Handler.__init__(self)
        self.db = db
        conn = sqlite3.connect(self.db)
        conn.execute(self._sql_create_log_table)
        conn.commit()
        conn.close()

    def emit(self, record):
        self.format(record)
        try:
            conn = sqlite3.connect(self.db)
            conn.execute(self._sql_insert, [str(value) for value in (record.__dict__.values())])
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("failed to log to database")
            raise e

@app.route("/")
def get_temperature():
    """
    Serves temperature data from the database, in a simple html format
    """
    
    logger = logging.getLogger("logger")
    #sqlite handler
    sql_handler = SQLiteHandler()
    logger.addHandler(sql_handler)
    logger.setLevel(logging.INFO)

    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("select * from temperatures")
    rows = cur.fetchall()
    cur.close()

    logger.info("Temperatures data was requested.")

    return render_template("temp.html", rows=rows)


if __name__ == "__main__":
    app.run()

