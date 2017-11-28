#Database Settings
import MySQLdb

HOST = os.environ['DB_HOST']
USER = os.environ['DB_USER']
PWD = os.environ['DB_PWD']
DBNAME = "news_articles"

db = MySQLdb.connect(HOST,USER,PWD,DBNAME)
cursor = db.cursor()

def save_data_db(data, table_name, publication, scrape_time):
	for key, value in data.iteritems():
		category = key

		#TODO: if link exists in metadata table, set metadata to 1
		metadata = 0

		for link in value:
			sql = """INSERT INTO {0}(publication, scrape_time, link, category, metadata) VALUES ('{1}', '{2}', '{3}', '{4}')""".format(table_name, publication, scrape_time, link, category, metadata)
			#print sql
			cursor.execute(sql)
			db.commit()
	db.close()


def save_metadata_db(metadata_table_name, data_table_name, url, article_text, meta_keywords, title, tags, nlp_keywords, nlp_summary, url_sections):


	sql = """INSERT INTO {0}(link, article_text, meta_keywords, title, tags, nlp_keywords, nlp_summary, url_sections) VALUES ("{1}", "{2}", "{3}", "{4}", "{5}", "{6}", "{7}", "{8}")""".format(metadata_table_name, url, article_text, meta_keywords, title, tags, nlp_keywords, nlp_summary, url_sections)
	# print sql

	cursor = db.cursor()
	cursor.execute(sql)
	cursor.close()

	sql_update = """UPDATE {0} SET metadata = 1 WHERE link = '{1}'""".format(data_table_name, url)

	print sql_update
	cursor = db.cursor()
	cursor.execute(sql_update)

	cursor.close()

	db.commit()
	return 1

def get_article_list(table_name):
	#get articles for which metadata not collected
	sql = """SELECT link from {0} WHERE metadata = 0""".format(table_name)
	cursor.execute(sql)

	#collect all links
	data = [i[0] for i in cursor.fetchall()]

	#return only unique links
	return set(data)
