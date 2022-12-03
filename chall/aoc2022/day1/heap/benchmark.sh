#!/bin/bash
go test -bench=. | grep -v 195292
