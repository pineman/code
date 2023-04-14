#!/usr/bin/env ruby -pi
gsub(/from/, "\nfrom")
# Use like `./sed.rb <file>`
#
# Explanation of `ruby -pi -e 'gsub(/lol/,"lel")' file`
#
# -p: This option puts Ruby into a loop where it reads each line of the input
# file(s) and automatically prints the line after executing the provided
# script. In this case, the script is modifying the content of the line before
# printing it.
#
# -i: This option enables in-place editing of the file(s). It tells Ruby to
# modify the input file directly, rather than printing the output to the
# console or a new file.
#
# -e: This option allows you to provide an inline Ruby script to be executed.
# In this case, the script is 'gsub(/lol/,"lel")'.
#
# The reason the gsub method works without an explicit object receiver is that,
# when used with the -p option, Ruby assumes the method is being called on the
# $_ variable. The $_ variable is a special global variable that holds the
# content of the current line being processed in the loop. Thus,
# gsub(/lol/,"lel") is equivalent to $_ = $_.gsub(/lol/, "lel").

