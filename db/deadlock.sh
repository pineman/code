#!/bin/bash
set -euxo pipefail

export PGPASSWORD=p
docker run --name pg-deadlock --rm -e POSTGRES_PASSWORD=$PGPASSWORD -p 5432:5432 postgres &
sleep 2
psql -h localhost -U postgres <<EOF
create table test (
	a int,
	b int
);
insert into test values(1, 1);
insert into test values(2, 2);
EOF
psql -h localhost -U postgres -c 'begin; update test set b=3 where a=1; select pg_sleep(1); update test set b=4 where a=2; commit;' &
psql -h localhost -U postgres -c 'begin; update test set b=4 where a=2; select pg_sleep(1); update test set b=3 where a=1; commit;' &
# 2022-12-28 23:55:04.536 UTC [68] ERROR:  deadlock detected
# 2022-12-28 23:55:04.536 UTC [68] DETAIL:  Process 68 waits for ShareLock on transaction 729; blocked by process 67.
# 	Process 67 waits for ShareLock on transaction 728; blocked by process 68.
# 	Process 68: begin; update test set b=4 where a=2; select pg_sleep(1); update test set b=3 where a=1; commit;
# 	Process 67: begin; update test set b=3 where a=1; select pg_sleep(1); update test set b=4 where a=2; commit;
# 2022-12-28 23:55:04.536 UTC [68] HINT:  See server log for query details.
# 2022-12-28 23:55:04.536 UTC [68] CONTEXT:  while updating tuple (0,1) in relation "test"
# 2022-12-28 23:55:04.536 UTC [68] STATEMENT:  begin; update test set b=4 where a=2; select pg_sleep(1); update test set b=3 where a=1; commit;
sleep 2
kill $(jobs -p)
wait
