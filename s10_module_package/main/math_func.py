

def add(a, b):
    return a + b


if __name__ == '__main__':
# 在這個 if __name__ == '__main__':的package裡面，只有這裡執行才會顯示出來，從其他package裡面不會出現，可用來做測試代碼放置處
    x = 1
    y = 2
    print(x, '+', y, '=', add(x, y))
