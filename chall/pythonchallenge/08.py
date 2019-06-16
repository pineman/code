import magic

u = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
p = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

"""with open('u', 'wb') as f:
    f.write(u)

with open('p', 'wb') as f:
    f.write(p)
"""
print(magic.detect_from_content(u))
print(magic.detect_from_content(p))

import bz2
print(bz2.decompress(u))
print(bz2.decompress(p))

# Solution is http://www.pythonchallenge.com/pc/return/good.html
