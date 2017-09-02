for i in range(__import__('sys').maxunicode + 1):
    try:
        print(f"\\U{i:08X}", end=' ')
        eval(f"print('\\U{i:08X}')")
    except Exception as e:
        print(e)
