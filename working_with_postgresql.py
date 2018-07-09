# working with postgresql via psycopg2
import psycopg2

# first you need create new postgresql database using pgadmin

# function that creates table
def create_table():
	# connect to db
	conn = psycopg2.connect( "dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'" )
	# create a cursor to read and write data
	cur = conn.cursor()
	cur.execute( "CREATE TABLE IF NOT EXISTS store ( item TEXT, quantity INTEGER, price REAL ) " )
	conn.commit()
	conn.close()

def insert( item, quantity, price ):
	conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
	cur = conn.cursor()
	cur.execute( "INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price) )
	conn.commit()
	conn.close()

def view():
	conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
	cur = conn.cursor()
	cur.execute( "SELECT * FROM store" )
	rows = cur.fetchall()
	conn.close()
	return rows

def delete( item ):
	conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
	cur = conn.cursor()
	cur.execute( "DELETE FROM store WHERE item=%s", (item,) )
	conn.commit()
	conn.close()

def update( quantity, price, item ):
	conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
	cur = conn.cursor()
	cur.execute( "UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item) )
	conn.commit()
	conn.close()

#insert( "Water Glass", 10, 14.1 )
#insert( "Coffee Cup", 10, 12 )
#delete( "Coffee Cup" )
#update(11, 14.9, "Coffee Cup")
#print( view() )

create_table()
update(10, 116, 'Apple')
print( view() )
#insert("Apple", 3, 15)
#insert("Pineapple", 4, 10)
#delete("Apple")
