import sqlite3, psycopg2
# from dotenv import load_dotenv
# load_dotenv()
import os

sqlitedb = sqlite3.connect('bdaybot.db', detect_types=sqlite3.PARSE_DECLTYPES)
sqlite3.register_converter("BOOLEAN", lambda val: bool(int(val)))

postgresdb = psycopg2.connect(dbname='botsdb')

# postgresdb = psycopg2.connect(dbname='botsdb',
#                               host=os.environ['host'],
#                               user=os.environ['user'],
#                               password=os.environ['password'])

lite_cursor = sqlitedb.cursor()
post_cursor = postgresdb.cursor()

# SQL Command to create TABLE guilds
create_guilds_table = """CREATE TABLE guilds(
                        guild_id BIGINT PRIMARY KEY,
                        announcements_id BIGINT,
                        role_id BIGINT,
                        today_names_cycle BYTEA,
                        nickname_notice BOOLEAN DEFAULT true
                        )"""
post_cursor.execute(create_guilds_table)

# SQL Command to create TABLE student_data
create_student_data_table = """CREATE TABLE student_data(
                                StuID INT PRIMARY KEY,
                                LastName TEXT,
                                FirstName TEXT,
                                Grd INT
                                )"""
post_cursor.execute(create_student_data_table)

# SQL Command to create TABLE discord_users
create_discord_users_table = """CREATE TABLE discord_users(
                                discord_user_id BIGINT PRIMARY KEY,
                                student_id INT UNIQUE,
                                FOREIGN KEY(student_id) REFERENCES student_data(StuID) ON DELETE CASCADE
                                )"""
post_cursor.execute(create_discord_users_table)

for guilds_data in lite_cursor.execute("SELECT * FROM guilds"):
    # Add data to PostgreSQL
    post_cursor.execute("INSERT INTO guilds VALUES(%s, %s, %s, %s, %s)", guilds_data)

for student_data in lite_cursor.execute("SELECT * FROM student_data"):
    # Add data to PostgreSQL
    post_cursor.execute("INSERT INTO student_data VALUES(%s, %s, %s, %s)", student_data)

for discord_users_data in lite_cursor.execute("SELECT * FROM discord_users"):
    # Add data to PostgreSQL
    post_cursor.execute("INSERT INTO discord_users VALUES(%s, %s)", discord_users_data)

for id, in list(lite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'"))[3:]:
    create_id_table = """CREATE TABLE {}(
                            discord_user_id BIGINT,
                            year INT,
                            PRIMARY KEY(discord_user_id, year),
                            FOREIGN KEY(discord_user_id) REFERENCES discord_users(discord_user_id)
                            ON DELETE CASCADE
                            )""".format(id)
    # Create the students
    post_cursor.execute(create_id_table)
    for id_table_data in lite_cursor.execute("SELECT * FROM {}".format(id)):
        post_cursor.execute("INSERT INTO {} VALUES(%s, %s)".format(id), id_table_data)


post_cursor.execute("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema'")
print(post_cursor.fetchall())

# postgresdb.commit()

sqlitedb.close()
postgresdb.close()
