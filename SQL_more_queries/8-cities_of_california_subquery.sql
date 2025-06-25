-- List all cities of California in hbtn_0d_usa database
USE hbtn_0d_usa;
SELECT * FROM cities WHERE state_id=(SELECT id FROM states WHERE name='California');
 