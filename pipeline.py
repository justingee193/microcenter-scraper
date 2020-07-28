import MySQLdb
import configparser
import sql_queries as sql
import csv

def drop_tables(cur, conn):
	cur.execute(sql.foreign_key_off)
	for query in sql.drop_table_queries:
		try:
			cur.execute(query)
			conn.commit()
		except:
			break
	cur.execute(sql.foreign_key_on)
	conn.commit()

def create_tables(cur, conn):
	for query in sql.create_table_queries:
		try:
			cur.execute(query)
			conn.commit()
		except:
			break

def load_tables(cur, conn):
	source_data = csv.reader(open('output.csv', 'r'))
	next(source_data)
	for query in sql.load_table_queries:
		for row in source_data:
			cur.execute(query, [col for col in row])
			conn.commit()

def insert_tables(cur, conn):
	for query in sql.insert_table_queries:
		try:
			cur.execute(query)
			conn.commit()
		except:
			break

def main():
    config = configparser.ConfigParser()
    config.read('config.cfg')

    conn = MySQLdb.connect(host=config['mysqldb']['host'], db=config['mysqldb']['db'], user=config['mysqldb']['user'], passwd=config['mysqldb']['pass'])
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)
    load_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()