

# MySQLga ulanish
 #!/usr/bin/env python3
import MySQLdb

db = MySQLdb.connect(
     host="82.97.253.34",
     user="gen_user",
     passwd="alpomish",
     db="default_db",
     port=3306
)

table = """
     CREATE TABLE IF NOT EXISTS attlog (
     ID VARCHAR(45),
     DateTime Datetime,
     Date Date,
     Time Time,
     Direction
     
     )
"""

# Cursor yaratish
cursor = db.cursor()

# SQL so'rovini bajarish

db.close()
