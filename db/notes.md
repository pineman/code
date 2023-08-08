# SQL
* select returns a table (or column or scalar), so it can be used wherever a table is (or column or scalar)
* `group by` and `having` are useful for aggregrate functions
* convert timestamp to date: `select DATE(<timestamp like created_at>) as day order by day`
* more timestamp things: `to_char(ts_column, 'mm/yyyy')`, `extract(month from ts_column)`
* can join a table with itself
* dimensionality must match in a select: `select column, max(column2)` doesn't work as you're trying to match up a column nx1 with a scalar 1x1

## PostgreSQL
* `\d+ table_name` shows foreign keys pointing to table_name (referenced_by)
* VACUUM reclaims dead tuples - expensive! ANALYZE rebuilds stats for the query planner - fast and good!! why run them both at the same time?!
* note "state='active'"!!
```sql
SELECT *, (now() - query_start) AS running_time
FROM pg_stat_activity
WHERE (now() - pg_stat_activity.query_start) > interval '1 minutes' AND state='active' ORDER BY running_time DESC;
```
* count number of rows fast estimate: `SELECT reltuples AS estimate FROM pg_class where relname = 'mytable';`
