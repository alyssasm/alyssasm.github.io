def fibboncaci(n):
  if n in [1, 2]:
    return 1
 
  seq = [1, 1]
  while len(seq) < n:
    print seq
    print str(seq[0]) + ' ' + str(seq[1])
    seq.append(seq[-1] + seq[-2])
  return seq[len(seq) - 1]
 
print fibboncaci(10)
 

def is_palindrome(word):
 first_half = None
 second_half = None
 
 if len(word) % 2 == 0:
    first_half = len(word) / 2
    second_half = len(word) / 2
 else:
    first_half = (len(word) / 2) + 1
    second_half = len(word) / 2

 first_half= word[:first_half]
 second_half= word[second_half:]
 second_half= second_half[::-1]

 print first_half
 print second_half
 
 if first_half == second_half:
    return word + ' is a palindrome!'
 else:
    return word + ' is not a palindrome...'
 
print is_palindrome('kayak')
print is_palindrome('racecar')
print is_palindrome('katniss everdeen')

