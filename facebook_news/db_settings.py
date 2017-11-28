import MySQLdb

#Database
HOST = os.environ['DB_HOST']
USER = os.environ['DB_USER']
PASSWORD = os.environ['DB_PWD']
DATABASE = "social_media"
table_name = "facebook_news_articles"

#Connect to database
db = MySQLdb.connect(HOST,USER,PASSWORD,DATABASE)
cursor = db.cursor()

def insert_into_database(status_data, cursor, db, table_name):
    formatted_status_data = []
    for i in status_data:
        formatted_status_data.append(MySQLdb.escape_string(str(i)))

    sql = """INSERT INTO """ +  table_name + """ (page_id,status_id,status_message,link_name,status_type,status_link,status_published,num_reactions,num_comments,num_shares,num_likes,num_loves,num_wows,num_hahas,num_sads,num_angrys) VALUES ( "{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}", {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15})""".format(*formatted_status_data)

    cursor.execute(sql)
    db.commit()
