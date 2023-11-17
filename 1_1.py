def even_odd(num: Int):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
    for i in range(0, 20, 2):
        print(num + i)

if __name__ == '__main__':
    even_odd(2)
