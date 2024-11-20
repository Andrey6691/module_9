def is_prime(func):
  def wrapper(a, b, c):
      x = func(a, b, c)
      if x > 1:
          for i in range(2, (x // 2) + 1):
              if (x % i) == 0:
                  print('Составное')
                  break
              else:
                  print('Простое')
                  break
      else:
          print('Составное')
      return func(a, b, c)

  return wrapper


@is_prime
def sum_three(a, b, c):
  return a + b + c


result = sum_three(2, 3, 2)
print(result)