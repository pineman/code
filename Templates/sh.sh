#!/bin/sh
exec 1<&-
exec 2<&-
exec 1<>$LOGFILE
exec 2>&1
