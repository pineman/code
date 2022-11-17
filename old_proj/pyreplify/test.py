"""doc


string"""

x = "   asdasdasd \
    asdasd       \
aa"

def l():
    print("asd",
end='')


# comment
    # comment
def gen(a):
    for i in range(a):
        yield i

        for x in range(2):
            print(x)

for x in range(2):
    for i in range(2):
        print(x)

next(gen(3))
gen(3).__next__()


