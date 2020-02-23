#!/bin/sh
./gradlew jibDockerBuild -Pbuild=native
docker build -t builder-native .
docker run --rm -v $(pwd):/app/mount builder-native
