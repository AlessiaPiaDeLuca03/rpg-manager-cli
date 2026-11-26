from database.db_connection import get_connection


def get_all_roles():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT *
    FROM roles
    """)

    roles = cursor.fetchall()

    connection.close()

    return roles