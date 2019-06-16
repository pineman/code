# Downloaded http://www.pythonchallenge.com/pc/def/channel.zip.
# Ran 'unzip -l channel.zip | cut -d' ' -f1 | vim -' and joined all lines.
# print(set(a)) gives the unique characters in the comments.
# Ran them through an anagram solver and tried 'oxygen' (oxygen.html).
#
# It worked by coincidence. By printing the comment of each file in the zip by
# the order suggested in the readme.txt, it prints 'HOCKEY' in ASCII art,
# but that art is made of the characters O X Y G E N, as hockey.html suggests.

a = 'E Y * E Y O N * * * * * * Y * E * O G * Y G E * Y E * N * G * * G * * * * * * * O X * * E * E * * X * * G E Y * * O O G X * * * * * * * E * * X O E * E * * * * N * X G E * N N G * X E X * * Y X N * O O O * G G * O O G * Y * * * Y N Y * X * * G * * * N N * X * * Y * E * * * Y O * * * N * * * * X * E * * * X O * * * X * N * * X * * * * * G * * O Y N X N * * * Y * * * * * * X * * * E E * * E * N * G * * * Y E * * * * * * * O * * * * O G * * O O O * * * X Y * * G E * * E * * Y * * X N * Y O * O X X * G N * Y * * * X * * O * O G * * O N * * * G E * N * Y E * * O * E * * * * * * * * N * E * Y * N Y * E X * O * * * Y G * N Y G * * O * * O E * Y G Y * * X * * * * G E * * * * * O * * * * * * * * * * * * * * O * E X * E O G * * * * Y * * O O * * * * * * * * * * * * * N * * * X * X X * * E * G * * X * * E X G * * * * O * * * Y E O Y * * E Y * * * * N * * Y * * * G G * X * * * N * * E * * * * * O * X * O * * Y X * * E * * * Y O * O X * X * * X X O * * E * * * * * E * * * * * * * G Y * G *'
print(set(a))
