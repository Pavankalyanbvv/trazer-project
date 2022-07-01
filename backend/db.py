import sqlite3

conn = sqlite3.connect("tdb.sqlite")

cursor = conn.cursor()
# sql_query = """ CREATE TABLE vehicles (
#     Id integer PRIMARY KEY,
#     Date string NOT NULL,
#     Pedestain interger NOT NULL,
#     Bike interger NOT NULL,
#     MotorBike interger NOT NULL,
#     Auto interger NOT NULL,
#     eRikshaw interger NOT NULL,
#     LMV interger NOT NULL,
#     LCV interger NOT NULL,
#     Bus interger NOT NULL,
#     Truck interger NOT NULL,
#     Tractor interger NOT NULL,
#     Total interger NOT NULL
# )"""
# sql_query="""insert into vehicles values(10,'05-07-2022',1,2,3,4,5,6,7,8,9,19,64)
# """
sql_query="""select * from vehicles
"""

cursor.execute(sql_query)
conn.commit()