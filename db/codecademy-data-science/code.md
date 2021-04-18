# First project: Create a Table
```sql
CREATE TABLE friends (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  birthday DATE NOT NULL
);

INSERT INTO friends(name, birthday)
VALUES
	('Jane Doe', '30-05-1990'),
  ('Isa', '02-05-1998'),
  ('Tomaz', '19-09-1997');

UPDATE friends
SET name = 'Jane Smith'
WHERE name = 'Jane Doe';

ALTER TABLE friends
ADD COLUMN email TEXT NOT NULL;

UPDATE friends
SET email = 'jane@codecademy.com'
WHERE name = 'Jane Smith';

UPDATE friends
SET email = 'jane@codecademy.com'
WHERE name = 'Isa';

UPDATE friends
SET email = 'jane@codecademy.com'
WHERE name = 'Tomaz';

DELETE FROM friends
WHERE name = 'Jane Smith';

SELECT *
FROM friends;
```

```sql
select
	name,
  case
  	when genre = 'romance' or genre = 'comedy' then 'Chill'
  	else 'Intense'
  end as 'Mood'
from movies;
```

# Code Challenge: Aggregate Functions
Database Schema
payments
id	INTEGER
user_id	INTEGER
amount	REAL
status	TEXT
pay_date	TEXT

users
id	INTEGER
first_name	TEXT
last_name	TEXT
email	TEXT
password	TEXT

watch_history
id	INTEGER
user_id	INTEGER
watch_date	TEXT
watch_duration_in_minutes	REAL

## 1
Use COUNT() and a LIKE operator to determine the number of users that have an email ending in ‘.com’.
```sql
select count(*)
from users
where email like '%.com';
```

## 2
What are the most popular first names on Codeflix?

Use COUNT(), GROUP BY, and ORDER BY to create a list of first names and occurrences within the users table.
```sql
select first_name, count(first_name)
from users
group by first_name
order by count(first_name) desc;
```

## 3
The UX Research team wants to see a distribution of watch durations. They want the result to contain:

duration, which is the watch event duration, rounded to the closest minute
count, the number of watch events falling into this “bucket”
Your result should look like:

duration	count
1.0			9
2.0			21
3.0			19
…			…

Use COUNT(), GROUP BY, and ORDER BY to create this result and order this data by increasing duration.
```sql
select
	watch_duration_in_minutes as 'duration',
  id as 'count'
from watch_history
group by 1;
```

## 4
Find all the users that have successfully made a payment to Codeflix and find their total amount paid.

Sort them by their total payments (from high to low).

Use SUM(), WHERE, GROUP BY, and ORDER BY.
```sql
select
	user_id,
  sum(amount) as 'total'
from payments
where status = 'paid'
group by 1
order by 2 desc;
```

## 5
Generate a table of user ids and total watch duration for users who watched more than 400 minutes of content.

Use SUM(), GROUP BY, and HAVING to achieve this.
```sql
select
	user_id,
	sum(watch_duration_in_minutes) as 'total watched'
from watch_history
group by 1 having sum(watch_duration_in_minutes) > 400;
```

## 6
To the nearest minute, how many minutes of content were streamed on Codeflix?
```sql
select round(sum(watch_duration_in_minutes))
from watch_history;
```

## 7
Which days in this period did Codeflix collect the most money?

Your result should have two columns, pay_date and total amount, sorted by the latter descending.

This should only include successful payments (status = 'paid').

Use SUM(), GROUP BY, and ORDER BY.
```sql
select
	pay_date,
  sum(amount)
from payments
where status = 'paid'
group by 1
order by 2 desc;
```

## 8
When users successfully pay Codeflix (status = 'paid'), what is the average payment amount?
```sql
select
	avg(amount)
from payments
where status = 'paid';
```

## 9
Of all the events in the watch_history table, what is the duration of the longest individual watch event? What is the duration of the shortest?

Use one query and rename the results to max and min.
```sql
select
	max(watch_duration_in_minutes) as 'max',
  min(watch_duration_in_minutes) as 'min'
from watch_history;
```

## Cross Join
```sql
select count(*)
from newspaper
where
	start_month <= 3
  and end_month >= 3;

select *
from newspaper
cross join months;

select *
from newspaper
cross join months
where
	start_month <= month
  and end_month >= month;

select
	month,
  count(*)
from newspaper
cross join months
where
	start_month <= month
  and end_month >= month;
group by 1;
```

## With
```sql
with previous_query as (
  select
		customer_id,
  	count(subscription_id) as 'subscriptions'
	from orders
	group by 1
)
select
	customers.customer_name,
  previous_query.subscriptions
from previous_query
inner join customers
on previous_query.customer_id = customers.customer_id;
```

## In - non-correlated subquery
```sql
select *
from flights
where origin in (
	select code
	from airports
	where elevation < 2000);
```
```sql
select
	a.dep_month,
  a.dep_day_of_week,
  round(avg(a.flight_distance),2) as average_distance
from (
  select
    dep_month,
    dep_day_of_week,
    dep_date,
    sum(distance) as 'flight_distance'
  from flights
  group by 1,2,3
  ) a
group by 1,2
order by 1,2;
```

## Correlated subquery
```sql
select id
from flights as fouter
where distance < (
  select avg(distance)
  from flights
  where carrier = fouter.carrier
);
```

- Subqueries are used to complete an SQL transformation by nesting one query within another query.

- A non-correlated subquery is a subquery that can be run independently of the outer query and can be used to complete a multi-step transformation.

- A correlated subquery is a subquery that cannot be run independently of the outer query. The order of operations in a correlated subquery is as follows:

1. A row is processed in the outer query.

2. Then, for that particular row in the outer query, the subquery is executed.