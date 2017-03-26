#!/usr/bin/env python3

alphabet = "abcdefghijklmnopqrstuvwxyz"

old_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
string = "map"

translated = ""
for s in string:
	try:
		index = 2 + alphabet.index(s)
	except ValueError:
		translated += s
		continue

	if index >= len(alphabet):
		index = index - len(alphabet)
	translated += alphabet[index]

print(translated)
