CREATE DATABASE student_grades;
CREATE USER leonphoenix21 WITH PASSWORD 'vtlt123@dck';
ALTER ROLE leonphoenix21 SET client_encoding TO 'utf8';
ALTER ROLE leonphoenix21 SET default_transaction_isolation TO 'read committed';
ALTER ROLE leonphoenix21 SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE student_grades TO leonphoenix21;
