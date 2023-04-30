class C2dVector:
    def __init__(self,i,j):
        self.icap =i
        self.jcap=j

    def __str__(self):
        return f"{self.icap}i and {self.jcap}j"

class C3dVector(C2dVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
    def __str__(self):
        return f"{self.icap}i and {self.jcap}j and {self.kcap}k"

v2d= C2dVector(1,3)
v3d= C3dVector(2,9,7)
print(v2d)
print(v3d)