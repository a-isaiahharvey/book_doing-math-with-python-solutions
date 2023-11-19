def even_odd(num):
      if num % 2 == 0:
          print("even")
      else:
          print("odd")
      for i in range(0, 20, 2):
          print(num + i)

if __name__ == '__main__':

    while True:
        even_odd(2)
        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break
