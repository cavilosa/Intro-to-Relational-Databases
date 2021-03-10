# "Database code" for the DB Forum.

import datetime
import psycopg2

DBNAME = 'forum'

def get_posts():
    """Return all posts from the 'database', most recent first."""
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute('select content, time from posts order by time desc')
    return cursor.fetchall()
    conn.close()

def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute("insert into posts values ('%s')" % content)
    conn.commit()
    conn.close()
