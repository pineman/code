# run with python -m pdb pm.py
from pdb import set_trace as bp

def func(a):
    bp()
    if a:
        print("true")
    else:
        raise Exception

a = [1,2,False]
for b in a:
    func(b)
    print("called func")
print("finished")
