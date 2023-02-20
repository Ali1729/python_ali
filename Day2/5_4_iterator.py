# objects of this class are iterators
class PowTwo:
    def __init__(self, max):
        self.max = max
    
    def __iter__(self):
        self.num = 0
        return self
        
    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        result = 2 ** self.num
        self.num += 1
        return result

pow_two = PowTwo(5)
pow_two_iter = iter(pow_two)

print(list(pow_two_iter))

a = str("asdf")

"""
In [7]: x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [8]: it=iter(x)

In [9]: for i in range(10):
    it.next()
   ....:     
   ....:     
Out[10]: 0
Out[10]: 1
Out[10]: 2
Out[10]: 3
Out[10]: 4
Out[10]: 5
Out[10]: 6
Out[10]: 7
Out[10]: 8
Out[10]: 9

In [12]: 'next' in dir(it)
Out[12]: True

In [13]: 'next' in dir(x)
Out[13]: False
""""