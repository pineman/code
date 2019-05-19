# First chapter of The AWK Programming Language
# Section 1.8, page 17 contains useful one-liners

# pattern { action }
# Match every pattern with every line and if true run action.
# Essentially the program is inside a for loop for each line.
# NF (updated each line): number of fields in line
# NR (updated each line): line number

#NF != 3		{ print $0, "number of fields is not equal to 3" }
#$2 < 3.35	{ print $0, "rate is below minimum wage" }
#$2 > 10		{ print $0, "rate exceeds $10 per hour" }
#$3 < 0		{ print $0, "negative hours worked" }
#$3 > 60		{ print $0, "too many hours worked" }

#BEGIN	{ print "NAME\tRATE\tHOURS"; print "" }
#		{ print }
#$3 > 15 { emp = emp + 1 } # No need to initialize emp
#		{ pay = pay + $2 * $3 }
#
#END		{ print ""
#		  print NR, "employees"
#		  print emp, "employees worked more than 15 hours"
#		  print "total pay is", pay
#		  print "average pay is", pay/NR
#		}

#$2 > maxrate	{ maxrate = $2; maxemp = $1 } # Variables can hold numbers or strings
#END				{ print "highest hourly rate:", maxrate, "for", maxemp }

#{ names = names $1 " " } # Simple string concatenation
#END { print names}

# Print last line
#{ last = $0 }
#END { print last }

#{ print $1, length($1) }
#{ nc = nc + length($0) + 1 # +1 for \n
#  nf = nf + NF }
#END { print NR, "lines,", nf, "fields,", nc, "characters" }

#$2 > 6 { n = n + 1; pay = pay + $2 * $3 }
#END {
#	if (n > 0) {
#		print n, "employees are paid more than $6/hour"
#		print "total pay is", pay
#		print "average pay is", pay/n
#	}
#	else {
#		print "no employees are paid more than $6/hour"
#		#print 1/0
#	}
#}

# reverse
{ line[NR] = $0 }
END {
	for (i = NR; i > 0; i = i - 1)
		print line[i]
}
