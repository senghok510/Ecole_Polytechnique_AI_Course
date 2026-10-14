import psycopg2
import sys
def main():
    # Database connection variables:
    host = "localhost"
    dbname="postgres"
    user="postgres"
    password=""
    port=5432
    # Opening a connection to Postgres:  
    con = psycopg2.connect(host=host, dbname=dbname,  user=user, password=password, port=port)
    query = "SELECT tablename
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND
    schemaname != 'information_schema'; "
    print(query)
    # Via the connection, opening a cursor: 
    cur = con.cursor()
    # Running the query: 
    cur.execute(query)
    # Getting all the cursor results in a list: 
    result = cur.fetchall()
    # print("The full cursor result is: ")
    # print(result)
    # Iterating over the result in Python to see them one by one: 
    response = "The tables in the database " + dbname + " are: [\n "
    for table in result:
      response += table[0]+",\n"
    response+="]"
    print(response)
if __name__ == "__main__":
	main()
