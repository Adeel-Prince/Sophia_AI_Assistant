import sqlite3;


conn = sqlite3.connect("sophia.db")

cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# to insert values
# query = "INSERT INTO sys_command VALUES (null,'OneNote', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft OneNote 2010')"
# cursor.execute(query)
# conn.commit()
# conn.close()  # Don't forget to close the connection when done


# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# to insert values
# query = "INSERT INTO web_command VALUES (null,'Google', 'https://google.com')"
# cursor.execute(query)
# conn.commit()
# conn.close()  # Don't forget to close the connection when done

#testing module
query = "OneNote"
cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (query,))
results = cursor.fetchall()
print(results[0][0])