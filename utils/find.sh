#!/bin/sh
find ~/Documents/ -type d -exec chmod 755 {} \;
find ~/Documents/ -type f -exec chmod 644 {} \;
find ~/Music/ -type d -exec chmod 755 {} \;
find ~/Music/ -type f -exec chmod 644 {} \;
find ~/Pictures/ -type d -exec chmod 755 {} \;
find ~/Pictures/ -type f -exec chmod 644 {} \;
