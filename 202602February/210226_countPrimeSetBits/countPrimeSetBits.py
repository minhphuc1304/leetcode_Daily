class Solution:
  def countPrimeSetBits(self, left: int, right: int) -> int:

    def prime(num):
      if num <= 1:
        return False
      if num <= 3:
        return True
      if num % 2 == 0 or num % 3 == 0:
        return False
      
      i = 5
      while i*i <= num:
        if num%i == 0 or num%(1+2) == 0:
          return False
      
      return True
    
    cnt = 0
    for i in range(left, right + 1):
      val = bin(i)[2:]
      res = val.count('1')
      if prime(res) == True:
        cnt += 1
    
    return cnt
