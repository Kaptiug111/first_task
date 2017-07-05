import mysql.connector
from mysql.connector import errorcode
import time

query_dict = {
    "select_all" : "SELECT  * FROM new_base.new_table",
    "select_by_id" : "SELECT * FROM new_base.new_table WHERE new_base.new_table.idnew_table={0}"}


def commonSelect (query):
    print 0
    returnvalue = None
    try:
        cnx = mysql.connector.connect(user='root', password='ma',
                                      host='127.0.0.1',
                                      database='new_base')
        cursor = cnx.cursor()

        cursor.execute(query)

        returnvalue = list()
        for line in cursor:
            returnvalue.append(line)

        cursor.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return returnvalue

def selectAll():
    return commonSelect(query_dict["select_all"])

def selectByID(id):
    return commonSelect(query_dict["select_by_id"].format(id))


#print(selectByID(1))



#insert value
query_dict = {
"insert" : "INSERT INTO 'new_base'.'new_table'('idnew_table','name') VALUES({0},'{1}')"
}

def commonInsert (query):

	try:
	    cnx = mysql.connector.connect(user='root', password='ma',
		                          host='127.0.0.1',
		                          database='new_base')
	    cursor = cnx.cursor()

	    cursor.execute(query)

	    cnx.commit()
	    cursor.close()

	except mysql.connector.Error as err:
	    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	    elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	    else:
		print(err)
	else:
	    cnx.close()

def insert(idnew_table, name):
    return commonInsert(query_dict["insert"].format(idnew_table, name))

#print insert(3, 'Mike')



#delete value
query_dict = {
"delete" : "DELETE FROM 'new_base'.'new_table'('idnew_table','name')WHERE idnew_table= {0}"
}

def commonDelete (query):

	try:
	    cnx = mysql.connector.connect(user='root', password='ma',
		                          host='127.0.0.1',
		                          database='new_base')
	    cursor = cnx.cursor()

	    cursor.execute(query)

	    cnx.commit()
	    cursor.close()

	except mysql.connector.Error as err:
	    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	    elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	    else:
		print(err)
	else:
	    cnx.close()

def delete(idnew_table):
    return commonDelete(query_dict["delete"].format(idnew_table))

#print delete(3)
