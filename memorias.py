import numpy as np
from datetime import datetime as dt
from itertools import chain, permutations
def argmin(z,key):
    if not z: return None
    min_val = min(z.values(),key=lambda x: x[key])
    return [k for k in z if z[k] == min_val][0]

class MemoriaCP(object):
    def __init__(self,largo):
        self.largo=largo
        self.mem =[]
    def tryUse(self,elem):
        #sin prob de usar taboo
        if elem in self.mem:
            return False
        else:
            if len(self.mem)==self.largo:
                self.mem=self.mem[1:]
            self.mem.append(elem)
            return True
    def __str__(self):
        return repr(self.mem)
    def __repr__(self):
        return "<MemoriaCP:"+repr(self.mem)+">"

class MemoriaMP(object):
    def __init__(self,largo):
        self.largo=largo
        self.mem ={}
        
    def cachedExcec(self,f,dato,*args):
        if self.mem.has_key(str(dato)):
            self.mem[str(dato)]['ts']=dt.now()
            return self.mem[str(dato)]["resultado"]
        else:
            if len(self.mem.keys())==self.largo:
                del self.mem[argmin(self.mem,"ts")]
            self.mem[str(dato)]={"resultado":f(dato,*args),"ts":dt.now()}
            return self.mem[str(dato)]["resultado"]
    def getElite(self):
        return eval(argmin(self.mem,"resultado"))
        
    def __str__(self):
        return repr(self.mem)
    def __repr__(self):
        return "<MemoriaCP:"+repr(self.mem)+">"
            
class MemoriaLP(object):
    def __init__(self,N):
        self.N = N
        self.mem = [[0 for _ in range(N)] for _ in range(N)] 
    
    def register(self,dato):
        for i in range(self.N):
            self.mem[i][dato[i]]+=1
        
    def choose(self):
        minFrec = float("inf")
        mfSol = None
        for a in permutations(range(self.N),self.N):
            s = sum([self.mem[i][a[i]] for i in range(self.N)])
            if s ==0:
                return a
            elif s<minFrec:
                minFrec = s
                mfSol = a
        return mfSol
    
    def __str__(self):
        return repr(self.mem)
    def __repr__(self):
        return "<MemoriaCP:"+repr(self.mem)+">"