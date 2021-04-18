DROP TABLE foo;
CREATE TABLE foo(bar int);
INSERT INTO foo (bar) VALUES (1), (null), (2);
SELECT COUNT(*), COUNT(bar) FROM foo;
