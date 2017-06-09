import werkzeug
from werkzeug.security import generate_password_hash, \
     check_password_hash

class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "localhost",
            "user": "root",
            "passwd": "lookroker13",
            "db": "weerstationdb"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def getDataFromDatabase(self,tablename):
        # Query zonder parameters
        sqlQuery = "SELECT * FROM {param1}"
        sqlCommand = sqlQuery.format(param1=tablename)
        
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getDataFromDatabaseMetVoorwaarde(self, voorwaarde):
        # Query met parameters
        sqlQuery = "SELECT * FROM tablename WHERE columnname = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)
        
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def setDataToDatabase(self, value1):
        # Query met parameters
        sqlQuery = "INSERT INTO tablename (columnname) VALUES ('{param1}')"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def login(self,naam,passwoord):
        # Query met parameters
        sqlQuery = "SELECT * FROM gebruiker WHERE naam ='{param1}' and wachtwoord ='{param2}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=naam,param2=passwoord)
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()

        if result!=[]:
            return result
        else:
            return False
