#!/bin/bash
set -euo pipefail

# 9 april 2014
base=1397072123
seconds_per_day=$((60*60*24))
day=0
for day in {0..5844}; do
    date=$((base + day * seconds_per_day))
    export GIT_AUTHOR_DATE=$date
    export GIT_COMMITTER_DATE=$date
	for pass in {0..10}; do
		git commit --allow-empty --allow-empty-message -m '' &>/dev/null
	done
done
