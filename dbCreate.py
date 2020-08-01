import mysql.connector
from mysql.connector import errorcode


def login(username, password):
    config = {'user': username, 'password': password, 'host': 'localhost', 'database': 'Secretariat', 'auth_plugin': 'mysql_native_password'}
    return connect_db(config)


def connect_db(config):
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
    cnx = login('behafarin', '127281')
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
        "  PRIMARY KEY (`SSN`)"
        ") ENGINE=InnoDB")
    tables['department'] = (
        "CREATE TABLE `department` ("
        "  `ID` INT NOT NULL,"
        "  `title` varchar(100) NOT NULL,"
        "  `budget` INT,"
        "  `manager` INT,"
        "  PRIMARY KEY (`ID`), UNIQUE KEY `title` (`title`)"
        ") ENGINE=InnoDB")
    tables['letter'] = (
        "CREATE TABLE `letter` ("
        "  `ID` INT NOT NULL,"
        "  `type` INT NOT NULL,"
        "  `security_level` INT NOT NULL,"
        "  `origin` VARCHAR(150) NOT NULL,"
        "  `destination` varchar(150) not  null,"
        "  `attachment` blob,"
        "  `sent_on` DATETIME,"
        "  `received_on` DATETIME,"
        "  `text` varchar(1000),"
        "  PRIMARY KEY (`ID`)"
        ")")
    tables['document'] = (
        "CREATE TABLE `document`("
        "  `ID` INT NOT NULL,"
        "  `type` INT NOT NULL,"
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


def add_employee(SSN, name, role, department, supervisor, salary, NO, zip_code, phone):
    cnx = connect_db()
    cnx.close()


def main():
    # print('please enter your username and password')
    # username = input('username: ')
    # password = input('password: ')
    # login(username, password)
    create_tables()


if __name__ == '__main__':
    main()

