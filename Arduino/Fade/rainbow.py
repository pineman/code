# `p` is the variable color channel, all the other are fixed,
# in order to make a 'rainbow' effect. The order of the
# fixed and variable color channels are easily verified
# in a color wheel. In RGB order.
rainbow = [['0 : 255    : {p}' , '{p}  : 255    : 0' ]
			,['255   : {p}  : 0' , '255    : 0  : {p}' ]
			,['{p} : 0  : 255'   , '0  : {p}  : 255'   ]]

d1 = [75, 25, 25]
d2 = [25, 25, 75]

for d, seg in enumerate(rainbow):
    # First part of the color segment, `p` increases.
    for p in range(255, 0, -3):
        # format the variable color channel `p` into the string
        # and turn it into an array of int [R, G, B]
        color = [int(x) for x in seg[0].format(p=p).split(':')]
        print("analogWrite(9, {});".format(color[0]))
        print("analogWrite(11, {});".format(color[1]))
        print("analogWrite(10, {});".format(color[2]))
        print("delay({});".format(d1[d]))

    # In the second part of the color segment,
    # p goes from 0xff to 0 instead.
    for p in reversed(range(255, 0, -3)):
        color = [int(x) for x in seg[1].format(p=p).split(':')]
        print("analogWrite(9, {});".format(color[0]))
        print("analogWrite(11, {});".format(color[1]))
        print("analogWrite(10, {});".format(color[2]))
        print("delay({});".format(d2[d]))
