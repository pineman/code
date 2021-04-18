-- Test inner join

drop table if exists test;
drop table if exists test2;

create table test (
	id integer,
	name text not null
);

insert into test(id, name) values (1, 'Aone');
insert into test(id, name) values (2, 'Atwo');
insert into test(id, name) values (3, 'Athree');
insert into test(id, name) values (3, 'Athree2');

create table test2 (
	id integer,
	name text not null
);

insert into test2(id, name) values (1, 'Bone');
insert into test2(id, name) values (1, 'Bone2');
insert into test2(id, name) values (3, 'Bthree');

--select * from test inner join test2 where test.id==test2.id;
--select * from test inner join test2 using (id);
--select * from test join test2 using (id);
select * from test, test2 using (id);
