#!/bin/sh
go test -bench=. -run='^skipTests'
