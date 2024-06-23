-- p95 only
select
  date_trunc('hour', created_at) as "Hour",
  (sum(took_seconds) filter (where result = 'invalid')) / (count(*) filter (where result = 'invalid')) as "invalid avg time",
  percentile_cont(0.95) within group (order by took_seconds) filter (where result = 'invalid') as "invalid p95 time"
from outlook_verifier_logs
where 1=1
  and cached is false
  and {{ date }}
group by 1
order by 1;

-- distribution
select
  width_bucket(took_seconds, 0, 20, 1000) as bucket,
  round(min(took_seconds)::numeric,2) || ' - ' || round(max(took_seconds)::numeric,2) as bucket_range,
  count(*) as frequency
from outlook_verifier_logs
where 1=1
  and cached is false
  and created_at between '2024-06-01' and '2024-06-10'
group by bucket
--having width_bucket(took_seconds, 0, 20, 1000) != 501 -- take out an outlier bucket
order by bucket;
