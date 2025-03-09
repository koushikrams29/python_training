class poly:
    def __init__(self,*x):
        self.x=list(x)
    def __add__(self,other):
        max_len=max(len(self.x),len(other.x))
        result=[0]*max_len

        for i in range(len(self.x)):
            result[max_len-len(self.x)+i]+=self.x[i]
        for i in range(len(other.x)):
            result[max_len-len(other.x)+i]+=other.x[i]
        
        return poly(*result)
    def __repr__(self):
        return f"poly{tuple(self.x)}"
