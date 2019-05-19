function initnum() {
	split("one two three four five six seven eight nine "\
		"ten eleven twelve thirteen fourteen fifteen "\
		"sixteen seventeen eighteen nineteen", nums, " ")
	split("ten twenty thirty forty fifty sixty "\
		"seventy eighty ninety", tens, " ")
}

function intowords(n) {
	n = int(n)
	if (n >= 1000)
		return intowords(n/1000) " thousand " intowords(n%1000)
	if (n >= 100)
		return intowords(n/100) " hundred " intowords(n%100)
	if (n >= 20)
		return tens[int(n/10)] " " intowords(n%10)
	return nums[n]
}
