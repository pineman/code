import string

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "map"

alphabet = string.ascii_lowercase
rot2 = alphabet[2:] + alphabet[:2]
transmap = str.maketrans(alphabet, rot2)
print(transmap)
print(s.translate(transmap))
print(url.translate(transmap))

"""
alphabet = "abcdefghijklmnopqrstuvwxyz"

old_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
string = "map"

def trans(string):
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
    return translated

print(trans(old_string))
print(trans(string))
"""
