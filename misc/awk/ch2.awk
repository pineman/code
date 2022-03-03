# print countries with column headers and totals
#BEGIN { FS = "\t" # make tab the field separator
#		printf("%10s %6s %5s %s\n\n",
#			   "COUNTRY", "AREA", "POP", "CONTINENT")
#	  }
#	  {
#		printf("%10s %6d %5d %s\n", $1, $2, $3, $4)
#		area += $2
#		pop *= $3
#	  }
#END	  { printf("\n%10s %6d %5d\n", "TOTAL", area, pop) }

# The following program uses a conditional expression to print the reciprocal of $1, or a warning if $1 is zero:
# { print ($1 != 0 ? 1/$1 : "$1 is zero, line " NR) }

# index() is 1 indexed, 0 if not found

# Thus, to force a string comparison between two fields, coerce one field to string:
# $1 "" == $2
# To force a numeric comparison, coerce both fields to numeric:
# $1 + 0 = $2 + 0
# This works regardless of what the fields contain.

# The numeric value of a string is the value of the longest prefix of the string that looks numeric.
# BEGIN { print "1E2"+0, "12E"+0, "E12"+0, "1X2Y3"+0 }
# yields
# 100 12 0 1

# `next` keyword is like continue in C
# `exit <value>` is like break and jumps to END returning int(value)

#/Asia/ { pop["Asia"] += $3 }
#/Europe/ { pop["Europe"] += $3 }
#END { print "Asian population is", pop["Asia"], "million"
#print "European population is", pop["Europe"], "million" }

#BEGIN { FS = "\t" }
#	  { pop[$4] += $3 }
#END { for (name in pop)
#		print name, pop[name]
#	}

# Strings are versatile array subscripts, but the behavior of numeric subscripts as strings may sometimes appear counterintuitive. Since the string values of 1 and "1" are the same, arr[1] is the same as arr["1"]. But notice that 01 is not the same string as 1 and the string 10 comes before the string 2.
# AWK has simulated support for multi dimensional arrays but array elements themselves cannot be arrays (pp. 52-53)

BEGIN {
	while ( "ls" | getline f )
		print f
}

# All variables are global except arguments to functions. To simulate function
# local vars, define extra arguments in the function (no need to pass them
# when calling it)
#To repeat, within a function definition, the parameters are local variables -
#they last only as long as the function is executing, and they are unrelated to
#variables of the same name elsewhere in the program. But all other variables
#are global; if a variable is not named in the parameter list, it is visible and
#accessible throughout the program.
#This means that the way to provide local variables for the private use of a
#function is to include them at the end of the parameter list in the function
#definition. Any variable in the parameter list for which no actual parameter is
#supplied in a call is a local variable, with null initial value. This is not a very
#elegant language design but it at least provides the necessary facility. We put
#several blanks between the arguments and the local variables so they can be dis-
#tinguished.
