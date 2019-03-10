"""
Following are the topics we will cover today.

1)  Create SQLight3 database
2)  Database connection
3)  CRUD Operation
4)  Python ORM for database operation

"""

# #############################################################################
# 1)  Create SQLight3 database
# #############################################################################

import sqlite3


# db = sqlite3.connect("class_12.db")
# cur = db.cursor()
#
# USERS = {
#     'id': 'INTEGER PRIMARY KEY',
#     'name': 'TEXT',
#     'phone': 'TEXT',
#     'email': 'TEXT unique',
#     'password': 'TEXT',
# }
#
# command = "CREATE TABLE IF NOT EXISTS users ("
#
# command += ", ".join([
#     "{} {}".format(key, value) for key, value in USERS.items()
# ])
# command += ")"
#
# cur.execute(command)
# db.close()


class DatabaseORM(object):
    """
    Database ORM
    """

    def __init__(self):
        """initialize class object"""
        self.con = None
        self.cur = None
        self.data = None
        self.database_info = dict()
        self.methods = {
            'create_table': self.create_table,
            'insert_record': self.insert_record,
            'select_record': self.select_record
        }

    def main(self, **kwargs):
        """
        Main method of class
        :return:
        """
        self.create_db_connection()
        self.create_cursor()

        self.data = kwargs.get('data')
        method = kwargs.get('method')

        if method not in self.methods:
            return {
                'status': False,
                'message': 'Method does not supported.'
            }

        self.methods.get(method)()

    def create_db_connection(self):
        """
        Create database connection
        :return:
        """
        self.con = sqlite3.connect("class_12.db")

    def create_cursor(self):
        """
        Create database cursor
        :return:
        """
        self.cur = self.con.cursor()

    def generate_create_table_command(self):
        """
        Generate crete table command based on self.data
        :return:
        """
        statement = "CREATE TABLE IF NOT EXISTS {} (".format(
            self.data.get('table_name'))

        statement += ", ".join([
            "{} {}".format(key, value)
            for key, value in self.data.get('table_structure').items()
        ])
        statement += ")"

        return statement

    def create_table(self):
        """
        Create table
        :return:
        """
        command = self.generate_create_table_command()
        try:
            self.cur.execute(command)
            print("Table has been created. ")
        except Exception as err:
            print(F"Due to following error Table has not been created\n{err}")

    def generate_insert_statement(self):
        """
        Generate insert statement based on the provided data
        :return:
        """
        insert_data = self.data.get('insert_data')
        _fields = ", ".join([
            field for field in insert_data.keys()
        ])

        place_holder = ", ".join(['?' for value in insert_data.values()])

        return F"INSERT INTO {self.data.get('table_name')}({_fields}) " \
            F"VALUES({place_holder})"

    def insert_record(self):
        """
        Insert record in specified record
        :return:
        """
        command = self.generate_insert_statement()
        self.cur.execute(command, tuple(self.data.get('insert_data').values()))
        self.con.commit()

    def generate_select_statement(self):
        """
        Generate select statement
        :return:
        """
        select_data = self.data.get('select_data')
        _fields = ", ".join([
            field for field in select_data
        ])
        command = F"SELECT {_fields} FROM {self.data.get('table_name')}"

        if not self.data.get('filter'):
            return command

        condition = ", ".join([
            "{}={}".format(key, value)
            for key, value in self.data.get('filter').items()
        ])

        command += F" WHERE {condition}"
        return command

    def select_record(self):
        """
        :return:
        """
        command = self.generate_select_statement()
        print(command)
        for i in self.cur.execute(command):
            print(i)

    def __del__(self):
        """

        :return:
        """
        self.con.close()


create_table_payload = {
    'method': 'create_table',
    'data': {
        'table_name': 'user',
        'table_structure': {
            'id': 'INTEGER PRIMARY KEY',
            'name': 'TEXT',
            'phone': 'TEXT',
            'email': 'TEXT unique',
            'password': 'TEXT',
        }
    }
}

insert_record_payload = {
    'method': 'insert_record',
    'data': {
        'table_name': 'user',
        'insert_data': {
            'id': '1234335535',
            'name': 'Kiran',
            'phone': '8689086344',
            'email': 'kirank@gmail.com',
            'password': 'PasswordIsPassword',
        }
    },

}

select_records_payload = {
    'method': 'select_record',
    'data': {
        'table_name': 'user',
        'select_data': [
            'id', 'name', 'email', 'phone', 'password'
        ],
        # 'filter': {
        #     'id': '1234335535'
        # }
    }
}

DatabaseORM().main(**select_records_payload)
