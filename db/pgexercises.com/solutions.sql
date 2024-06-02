-- Basic
-- Retrieve everything from a table
select * from cd.facilities;

-- Retrieve specific columns from a table
select name, membercost from cd.facilities;

-- Control which rows are retrieved
select * from cd.facilities where membercost > 0;

-- Control which rows are retrieved - part 2
select facid, name, membercost, monthlymaintenance
from cd.facilities
where membercost > 0 and membercost < monthlymaintenance/50;

-- Basic string searches
select * from cd.facilities where name like '%Tennis%';

-- Matching against multiple possible values
select * from cd.facilities where facid in (1, 5);

-- Classify results into buckets
select name, case
  when monthlymaintenance > 100 then 'expensive'
  else 'cheap' end
from cd.facilities;

-- Working with dates
select memid, surname, firstname, joindate
from cd.members
where joindate >= '2012-09-01';

-- Removing duplicates, and ordering results
select distinct(surname) from cd.members order by surname asc limit 10;

-- Combining results from multiple queries
select surname from cd.members
union
select name from cd.facilities;

-- Simple aggregation
select max(joindate) from cd.members;

-- More aggregation
select firstname, surname, joindate from cd.members order by joindate desc limit 1;

-- Joins and Subqueries
-- Retrieve the start times of members' bookings
select starttime from cd.bookings b
join cd.members m on b.memid = m.memid
where m.firstname = 'David' and m.surname = 'Farrell';

-- Work out the start times of bookings for tennis courts
select b.starttime, f.name from cd.bookings b
inner join cd.facilities f on b.facid = f.facid
where f.name ilike 'tennis court%'
  and b.starttime >= '2012-09-21 00:00:00'
  and b.starttime < '2012-09-22 00:00:00'
order by b.starttime;

-- Produce a list of all members who have recommended another member
--select firstname, surname from cd.members where memid in (select distinct(recommendedby) from cd.members) order by (surname,firstname);
select distinct m1.firstname, m1.surname from cd.members m1
join cd.members m2 on m2.recommendedby = m1.memid
order by m1.surname, m1.firstname;

-- Produce a list of all members, along with their recommender
select m1.firstname, m1.surname, m2.firstname, m2.surname from cd.members m1
left outer join cd.members m2 on m1.recommendedby = m2.memid
order by m1.surname, m1.firstname;

-- Produce a list of all members who have used a tennis court
select distinct m1.firstname || ' ' || m1.surname as member, f.name as facility
from cd.members m1
inner join cd.bookings b on m1.memid = b.memid
inner join cd.facilities f on b.facid = f.facid
where f.name ilike 'tennis court%' order by member, facility;

-- Produce a list of costly bookings
select
  firstname || ' ' || surname as member,
  name as facility,
  case when m.memid = 0
    then guestcost*slots
    else membercost*slots
  end as cost
from cd.members m
inner join cd.bookings b on m.memid = b.memid
inner join cd.facilities f on b.facid = f.facid
where b.starttime::date = date('2012-09-14')
  and (case when m.memid = 0 then guestcost*slots else membercost*slots end) > 30
order by cost desc;

-- Produce a list of all members, along with their recommender, using no joins.
--select distinct m1.firstname || ' ' || m1.surname as member,
--  m2.firstname || ' ' || m2.surname as recommender
--from cd.members m1
--left join cd.members m2 on m1.recommendedby = m2.memid
--order by member;
select distinct m1.firstname || ' ' || m1.surname as member, (
  select m2.firstname || ' ' || m2.surname
  from cd.members m2
  where m2.memid = m1.recommendedby
) from cd.members m1 order by member;

-- Produce a list of costly bookings, using a subquery
select * from (
  select
    firstname || ' ' || surname as member,
    name as facility,
    case when m.memid = 0
      then guestcost*slots
      else membercost*slots
    end as cost
  from cd.members m
  inner join cd.bookings b on m.memid = b.memid
  inner join cd.facilities f on b.facid = f.facid
  where b.starttime::date = date('2012-09-14')
  order by cost desc
) as sub where cost > 30;

-- Modifying data
-- Insert some data into a table
insert into cd.facilities values (9, 'Spa', 20, 30, 100000, 800)

-- Insert multiple rows of data into a table
insert into cd.facilities values (9,'Spa',20,30,100000,800), (10,'Squash Court 2',3.5,17.5,5000,80);

-- Insert calculated data into a table
insert into cd.facilities(facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
  values ((select max(facid)+1 from cd.facilities),'Spa', 20, 30, 100000, 800);

-- Update some existing data
update cd.facilities set initialoutlay = 10000 where name = 'Tennis Court 2';

-- Update multiple rows and columns at the same time
update cd.facilities set membercost = 6, guestcost=30 where name ilike 'tennis court%';

-- Update a row based on the contents of another row
update cd.facilities f
set
  membercost=f1.membercost*1.1,
  guestcost=f1.guestcost*1.1
from (select membercost,guestcost from cd.facilities where name ilike 'tennis court 1') f1
where f.name ilike 'tennis court 2';

-- Delete all bookings
truncate table cd.bookings

-- Delete a member from the cd.members table
delete from cd.members where memid = 37;

-- Delete based on a subquery
delete from cd.members where memid not in (select distinct memid from cd.bookings);

-- Aggregation
-- Count the number of facilities
select count(1) from cd.facilities;

-- Count the number of expensive facilities
select count(*) from cd.facilities where guestcost >=10

-- Count the number of recommendations each member makes.
select recommendedby, count(*) from cd.members
where recommendedby is not null
group by recommendedby order by recommendedby;

-- List the total slots booked per facility
select b.facid, sum(b.slots) as "Total Slots" from cd.bookings b
group by b.facid order by b.facid;

-- List the total slots booked per facility in a given month
select b.facid, sum(b.slots) as "Total Slots" from cd.bookings b
where to_char(starttime, 'mm/yyyy') = '09/2012'
group by b.facid order by "Total Slots";

-- List the total slots booked per facility per month
select facid,
  extract(month from starttime) as month,
  sum(slots) as "Total Slots"
from cd.bookings
where extract(year from starttime) = 2012
group by facid, month order by facid, month;

-- Find the count of members who have made at least one booking
select count(distinct(m.memid))
from cd.members m
join cd.bookings b on b.memid=m.memid;

-- List facilities with more than 1000 slots booked
select facid, sum(slots) as "Total Slots" from cd.bookings
group by facid having sum(slots) > 1000 order by facid;

-- Find the total revenue of each facility
select f.name, sum(slots *
  case
    when b.memid = 0 then f.guestcost
    else f.membercost
  end
) as revenue from cd.bookings b join cd.facilities f on b.facid=f.facid group by f.facid order by revenue;

-- Find facilities with a total revenue less than 1000
select name, revenue
from (
  select f.name, sum(slots * case when b.memid = 0 then f.guestcost else f.membercost end) as revenue
  from cd.bookings b
  join cd.facilities f on b.facid=f.facid
  group by f.facid
) as agg
where revenue < 1000
order by revenue;

-- Output the facility id that has the highest number of slots booked
--select facid, sum(slots) as "Total Slots" from cd.bookings group by facid order by "Total Slots" desc limit 1;
--select facid, sum(slots) as "Total Slots"
--from cd.bookings b
--group by facid
--having sum(slots) = (
--  select max(sum_slots) from (select sum(slots) as sum_slots from cd.bookings group by facid) as sum
--);

with sum as (
  select facid, sum(slots) as sum_slots from cd.bookings group by facid
)
select facid, sum_slots from sum where sum_slots = (select max(sum_slots) from sum);

-- List the total slots booked per facility per month, part 2
select facid,
  extract(month from starttime) as month,
  sum(slots)
from cd.bookings b
where extract(year from starttime) = 2012
group by rollup(facid, month)
order by facid, month;

-- List the total hours booked per named facility
select f.facid,
  f.name,
  round(sum(b.slots)/2.0, 2) as "Total Hours"
from cd.bookings b
inner join cd.facilities f on b.facid=f.facid
group by f.facid
order by f.facid;

-- List each member's first booking after September 1st 2012
select
  m.surname, m.firstname, m.memid,
  min(b.starttime)
from cd.members m
inner join cd.bookings b on m.memid = b.memid
where b.starttime > '2012-09-1'
group by m.surname, m.firstname, m.memid
order by m.memid;

-- Produce a list of member names, with each row containing the total member count
--select (select count(*) from cd.members), firstname, surname from cd.members order by joindate
select count(*) over(), firstname, surname from cd.members order by joindate;
--select count(*) over(partition by date_trunc('month',joindate)),
--	firstname, surname
--	from cd.members
--order by joindate;
-- The ORDER BY changes the window again. Instead of the window for each row being the entire partition, the window goes from the start of the partition to the current row, and not beyond. Thus, for the first member who joins in a given month, the count is 1. For the second, the count is 2, and so on.
--select count(*) over(partition by date_trunc('month',joindate) order by joindate),
--	firstname, surname
--	from cd.members
--order by joindate;
--select count(*) over(partition by date_trunc('month',joindate) order by joindate asc),
--	count(*) over(partition by date_trunc('month',joindate) order by joindate desc),
--	firstname, surname
--	from cd.members
--order by joindate;

-- Produce a numbered list of members
--select count(*) over(order by joindate), firstname, surname from cd.members order by joindate;
select row_number() over(order by joindate), firstname, surname from cd.members order by joindate;

-- Output the facility id that has the highest number of slots booked, again
select facid, sum(slots) from cd.bookings group by facid order by 2 desc limit 1; -- close but doesn't respect the tie condition

with slots as (select sum(slots) as slots from cd.bookings group by facid)
select facid, sum(slots)
from cd.bookings
group by facid
having sum(slots) = (select max(slots) from slots);

select facid, sum
from (
  select
    facid,
    rank() over (order by sum(slots) desc),
    sum(slots)
  from cd.bookings
  group by facid
) s where s.rank = 1;

-- Rank members by (rounded) hours used
--select m.firstname, m.surname,
--  (sum(b.slots)/2+5)/10*10 as hours,
--  rank() over(order by (sum(b.slots)/2+5)/10*10 desc)
--from cd.bookings b
--join cd.members m on b.memid=m.memid
--group by m.memid
--order by rank, surname, firstname;
select firstname, surname, hours, rank() over(order by hours desc)
from (
  select m.firstname, m.surname, (sum(b.slots)/2+5)/10*10 as hours
  from cd.bookings b
  join cd.members m on b.memid = m.memid
  group by m.memid
) as subq
order by rank, surname, firstname;

-- Find the top three revenue generating facilities
--with q as (select
--	b.facid,
--	sum(case
--		when b.memid=0 then b.slots*f.guestcost
--		else b.slots*f.membercost
--	end) as sum
--from cd.bookings b
--inner join cd.facilities f on f.facid = b.facid
--group by b.facid)
--
--select
--	f.name,
--	rank() over(order by sum desc)
--from q
--inner join cd.facilities f on f.facid = q.facid
--limit 3;

select name, rank
from (
  select f.name, rank() over (order by sum(case
    when memid=0 then slots*guestcost
    else slots*membercost
  end) desc) as rank
  from cd.facilities f
  inner join cd.bookings b on f.facid = b.facid
  group by f.name
) as subq
where rank <= 3
order by rank, name;

-- Classify facilities by value
select name, case
  when class=1 then 'high'
  when class=2 then 'average'
  else 'low'
end revenue
from (
  select f.name as name, ntile(3) over (order by sum(case
    when memid=0 then slots*guestcost
    else slots*membercost
  end) desc) as class
  from cd.facilities f
  inner join cd.bookings b on f.facid = b.facid
  group by f.name
) as subq
order by class, name;


