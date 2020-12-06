#!/bin/sh
set -eux
test -z "$(go fmt ./...)"
