import sqlite3

def connect(dbname):
    conn = sqlite3.connect(dbname)

    conn.execute("CREATE TABLE IF NOT EXISTS JOBS (COMPANY_NAME TEXT, REQUIRED_SKILLS TEXT, JOB_LINK TEXT)")

    print("Table created successfully!")

    conn.close()

def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)
    print("Inserted into table " + str(values))
    insert_query = "INSERT INTO JOBS (COMPANY_NAME, REQUIRED_SKILLS, JOB_LINK) VALUES (?, ?, ?)"

    conn.execute(insert_query, values)

    conn.commit()
    conn.close()

def get_job_info(dbname):
    conn = sqlite3.connect(dbname)

    cur = conn.cursor()

    cur.execute("SELECT * FROM JOBS")

    table_data = cur.fetchall()

    for record in table_data:
        print(record)

    conn.close()
