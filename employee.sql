PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE employee(id integer primary key, name text);
INSERT INTO "employee" VALUES(1,'Tu Nguyen');
INSERT INTO "employee" VALUES(2,'Ben Stones');
COMMIT;
