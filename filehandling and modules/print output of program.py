try:
    print(100)
    print(5/0)
    print(200)
except ZeroDivisionError:
    print(300)
finally:
    print(400)
