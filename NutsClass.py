class Nuts:
    def __init__(self, *args):
        self.Nuts = 'Nuts'
    
    def __getitem__(self, idx):
        return idx
    
    def __setitem__(self, idx, val):
        pass
    
    def __delitem__(self, idx):
        pass
    
    def __getattribute__(self, attr):
        return attr
    
    def __setattr__(self, attr, val):
        pass
    
    def __delattr__(self, attr):
        pass
    
    def __str__(self):
        
        return self.Nuts
    
    def __iter__(self):
        return iter("Nuts")
    
    def __next__(self):
        raise StopIteration

c = Nuts(1)
print(c)

# M, N = Nuts(), Nuts(1,2,3,4)
# print(M, N)
# M[100] = N.qwerty = 42
# print(M[100], N.qwerty)
# print(Nuts("QWERQWERQWER"))
# print(*list(Nuts("QWERQWERQWER")))
# del M["QQ"], N[6:10], M[...], N._, N.qwerty
# print(M.asdfg, N[-2])