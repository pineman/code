import sys

for i in range(255):
    try:
        print(f"\\U{i:08X}", end=' ')
        eval(f"print('\\U{i:08X}')")
    except Exception as e:
        print(e)
