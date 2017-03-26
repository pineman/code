#CFLAGS=-Wall -Wextra -Werror -std=c99 -pedantic-errors -ggdb
CFLAGS=-Wall -Wextra -Werror -std=c99 -ggdb

all:
	find -name "*.c" | sed -e "s/\.c//g" | xargs make

clean:
	find -regextype posix-extended -regex "./[0-9]-[0-9a-z]+" -exec rm -rf {} \;
