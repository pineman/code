#!/bin/sh

hostname=$(hostname | tr [:lower:] [:upper:])
date=$(date +%d.%m.%Y)
file="$hostname-$date"

workdir="/backup"
logfile="$workdir/logs/backup-$date.log"
exclude="$workdir/exclude/normal"

mailfrom="root@oceanic.pineman.me"
mailto="joao.castropinheiro@gmail.com"
subject="[$hostname] Backup completed at `date`"

if [ "$(id -u)" == "0" ]; then
	exec 2>&1
	exec 1>$logfile
	cd $workdir

	echo [`date`] Started tar
	tar --exclude-from=$exclude -cpf $file.tar /
	echo [`date`] Finished tar

	echo [`date`] Started pixz
	pixz $file.tar
	echo [`date`] Finished pixz

	echo [`date`] Started megaput
	megaput --no-progress --config /root/.megarc $file.tpxz
	echo [`date`] Finished megaput

	#echo [`date`] Uploading logfile
	#gzip -kf $logfile
	#megaput --no-progress --config /root/.megarc $logfile.gz

	echo [`date`] Sending email
	gzip -kf $logfile
	echo | mail -a "$logfile.gz" -r "$mailfrom" -s "$subject" "$mailto"

	echo [`date`] Done.
	gzip -f $logfile
else
	echo 'This script needs to run as root.'
fi
