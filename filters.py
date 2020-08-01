import dbCreate


def origin(user, SSN):
    cnx = dbCreate.connect_db()
    cursor = cnx.cursor()
    query = "SELECT * FROM letter WHERE origin = %s"
    cursor.execute(query, (SSN,))
    letters = cursor.fetchall()
    cnx.close()
    return letters


def destination(user, SSN):
    cnx = dbCreate.connect_db()
    cursor = cnx.cursor()
    query = "SELECT * FROM letter WHERE destination = %s"
    cursor.execute(query, (SSN,))
    letters = cursor.fetchall()
    cnx.close()
    return letters


def letter_type(user, num):
    cnx = dbCreate.connect_db()
    cursor = cnx.cursor()
    query = "SELECT * FROM letter WHERE type = %s"
    cursor.execute(query, (num,))
    letters = cursor.fetchall()
    cnx.close()
    return letters


def doc_security_level(user, num):
    cnx = dbCreate.connect_db()
    cursor = cnx.cursor()
    query = "SELECT * FROM document WHERE security_level = %s"
    cursor.execute(query, (num,))
    docs = cursor.fetchall()
    cnx.close()
    return docs


def letter_security_level(user, num):
    cnx = dbCreate.connect_db()
    cursor = cnx.cursor()
    query = "SELECT * FROM document WHERE security_level = %s"
    cursor.execute(query, (num,))
    letters = cursor.fetchall()
    cnx.close()
    return letters


def role(user, job):
    cnx = dbCreate.connect_db()
    cursor = cnx.cursor()
    query = "SELECT * FROM employee WHERE role = %s"
    cursor.execute(query, (job,))
    employees = cursor.fetchall()
    cnx.close()
    return employees
