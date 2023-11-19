def enhanced_multi_table(a, end_mult):
    for i in range(1, int(end_mult) + 1):
        print('{0} x {1} = {2}'.format(a, i, a * i))


if __name__ == '__main__':
    a = input('Enter a number: ')
    b = input('Enter the last multiple: ')
    enhanced_multi_table(float(a), b)
