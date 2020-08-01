import mysql.connector
from mysql.connector import errorcode
import filters


def login(username, password):
    cnx = connect_db()
    cursor = cnx.cursor()
    query = 'SELECT * FROM employee WHERE username = %s AND password = %s;'
    login_value = (username, password)
    cursor.execute(query, login_value)
    current_user = cursor.fetchone()
    cnx.close()
    return current_user


def connect_db():
    config = {'user': 'behafarin', 'password': '127281', 'host': 'localhost', 'database': 'Secretariat',
              'auth_plugin': 'mysql_native_password'}
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        else:
            print(err)
    else:
        return cnx


def create_tables():
    cnx = connect_db()
    cursor = cnx.cursor()
    tables = {}
    tables['employee'] = (
        "CREATE TABLE `employee` ("
        "  `SSN` INT NOT NULL,"
        "  `name` varchar(150) NOT NULL,"
        "  `role` varchar(150) NOT NULL,"
        "  `department` INT NOT NULL,"
        "  `supervisor` INT,"
        "  `salary` INT,"
        "  `HNo` INT,"
        "  `zip_code` INT,"
        "  `phone` INT,"
        "  `username` varchar(50) NOT NULL,"
        "  `password` varchar(50) NOT NULL,"
        "  PRIMARY KEY (`SSN`)"
        ") ENGINE=InnoDB")
    tables['department'] = (
        "CREATE TABLE `department` ("
        "  `ID` INT NOT NULL,"
        "  `title` varchar(100) NOT NULL,"
        "  `budget` INT,"
        "  `manager` INT,"
        "  PRIMARY KEY (`ID`), UNIQUE KEY `title` (`title`),"
        "  FOREIGN KEY (`manager`) REFERENCES employee(`SSN`)"
        ") ENGINE=InnoDB")
    tables['letter'] = (
        "CREATE TABLE `letter` ("
        "  `ID` INT NOT NULL,"
        "  `type` INT NOT NULL,"
        "  `security_level` INT NOT NULL,"
        "  `origin` INT NOT NULL,"
        "  `destination` INT not  null,"
        "  `attachment` blob,"
        "  `sent_on` DATETIME,"
        "  `received_on` DATETIME,"
        "  `text` varchar(1000),"
        "  PRIMARY KEY (`ID`),"
        "  FOREIGN KEY (`origin`) REFERENCES employee(`SSN`),"
        "  FOREIGN KEY (`destination`) REFERENCES employee(`SSN`)"
        ")")
    tables['document'] = (
        "CREATE TABLE `document`("
        "  `ID` INT NOT NULL,"
        "  `security_level` INT NOT NULL,"
        "  `text` varchar(1000),"
        "  PRIMARY KEY (`ID`)"
        ")")

    for table_name in tables.keys():
        table_description = tables[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.close()


def add_employee(SSN, name, role, department, supervisor, salary, HNo, zip_code, phone, username, password):
    cnx = connect_db()
    cursor = cnx.cursor()
    query = "INSERT INTO employee (SSN, name, role, department, supervisor, salary, HNo, zip_code, phone, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    employee_values = (SSN, name, role, department, supervisor, salary, HNo, zip_code, phone, username, password)
    cursor.execute(query, employee_values)
    cnx.commit()
    cnx.close()


def save_departments():
    cnx = connect_db()
    cursor = cnx.cursor()
    query = "INSERT INTO department (ID, title, budget, manager) VALUES (%s, %s, %s, %s)"
    dept_values = [
        (36, 'computer', 12000, 123456),
        (37, 'biology', 20000, 987654),
        (38, 'literature', 10000, 111111),
        (39, 'mechanic', 15000, 222222),
        (40, 'architecture', 12000, 333333)
    ]
    cursor.executemany(query, dept_values)
    cnx.commit()
    cnx.close()


def add_letter(ID, type, security_level, origin, destination, attachment, sent_on, received_on, text):
    cnx = connect_db()
    cursor = cnx.cursor()
    query = "INSERT INTO letter (ID, type, security_level, origin, destination, attachment, sent_on, recieved_on, text) VALUES (%d, %d, %d, %s, %s, %s, %s, %s, %s)"
    letter_values = (ID, type, security_level, origin, destination, attachment, sent_on, received_on, text)
    cursor.execute(query, letter_values)
    cnx.commit()
    cnx.close


def add_document(ID, security_level, text):
    cnx = connect_db()
    cursor = cnx.cursor()
    query = "INSERT INTO document (ID, security_level, text) VALUES (%d, %d, %s)"
    doc_values = (ID, security_level, text)
    cursor.execute(query, doc_values)
    cnx.commit()
    cnx.close()


def create_employee(user, SSN, name, role, department, supervisor, salary, HNo, zip_code, phone, username, password):
    if user[2] == 'manager':
        add_employee(SSN, name, role, department, supervisor, salary, HNo, zip_code, phone, username, password)
        return 'employee added successfully'
    else:
        return "you do not have the access"


def main():
    current_user = login('Emad', 'Emad')
    print(filters.role(current_user, 'manager'))


if __name__ == '__main__':
    main()

