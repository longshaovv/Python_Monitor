# Python_Monitor
Using python to monitoring equipment ,by meaning of get system server information
The database is mysql,database name =jiankong,table is test1_fuwu,detailed fields in the table as follows:
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int(11)      | NO   | PRI | NULL    | auto_increment |
| name        | varchar(20)  | NO   |     | NULL    |                |
| info        | varchar(100) | NO   |     | NULL    |                |
| flag        | tinyint(1)   | NO   |     | NULL    |                |
| openflag    | tinyint(1)   | NO   |     | NULL    |                |
| downflag    | tinyint(1)   | NO   |     | NULL    |                |
| opencommand | varchar(100) | NO   |     | NULL    |                |
| downcommand | varchar(100) | NO   |     | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
