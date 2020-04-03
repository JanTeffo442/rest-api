import psycopg2

connection = psycopg2.connect(database="pure_sql"
,user="myuser",password="pass", host="localhost",port=5432)
cursor = connection.cursor()

query = """INSERT INTO Computers(id, hard_drive_type, processor, amount_ram, max_ram, hard_drive_size,form_factor) 
VALUES
(1,'ssd','intel dual core', '5GB', '64 GB','1TB', 'mini'),
(2,'hdd','amd', '8GB','16GB', '500GB','medium'),
(3,'ssd','intel atom','2GB','16GB','256GB','medium')"""

query = """SELECT * FROM computers"""

cursor.execute(query)
connection.commit()