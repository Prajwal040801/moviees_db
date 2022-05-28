import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_moviees(conn, moviees):
    """
    Create a new project into the projects table
    :param conn:
    :param moviees:
    :return: movie_name
    """
    sql = ''' INSERT INTO moviees(movie_name,act_name,dir_name,actress_name,release_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, moviees)
    conn.commit()
    return cur.lastrowid





def main():
    database = r"C:\sqlite\db\moviees.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new moviees
        moviees= ('ajay', 'punith', 'john','ramya','2002');
        movie_name = create_moviees(conn, moviees)





if __name__ == '__main__':
    main()

