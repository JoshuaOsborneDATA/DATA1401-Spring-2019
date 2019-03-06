class Matrix:
    
    def __init__(self,n=1,m=1):
        self.n=n #####number of rows
        self.m=m  ##### number of columns
        self.M = [[0.0] * self.m for i in range(self.n)]
        
    def PrintM(self):
        for x in self.M:
            print x
        
    def constant(self,c):
        self.M= [[float(c)] * self.m for i in range(self.n)]
        return self.M
    
    def zeros(self):
        return [[0.0] * self.m for i in range(self.n)]
    
    def ones(self):
        return [[1.0] * self.m for i in range(self.n)]
    
    def eye(self):
        Identity=[[0.0] * self.n for i in range(self.n)]
        for k in range(0,self.n):
            for j in range(0,self.n):
                if k==j:
                    Identity[k][k]=1.0
        return Identity
    
    def Shape(self,N=list()):
        FindingRow=True
        FindingColumn=True
        shape=0
        n=0
        m=0
        ######## iterating n and m till i find number of rows and colums. I know it will go out of index so i add a try and except###
        if N ==[]:
            try:
                while FindingRow==True:
                    try:
                        while FindingColumn==True:
                            self.M[0][m]
                            m+=1
                    except IndexError:
                        FindingColumn=False
                    self.M[n][0]
                    n+=1
            except IndexError:
                FindingRow=False
            size=(n,)+(m,)  
        else:
            try:
                while FindingRow==True:
                    try:
                        while FindingColumn==True:
                            N[0][m]
                            m+=1
                    except IndexError:
                        FindingColumn=False
                    N[n][0]
                    n+=1
            except IndexError:
                FindingRow=False
            size=(n,)+(m,)
            return size
        ######### Now testing that the matrix was made correctly ########
        
        for i in range(0,n):
            if len(self.M[i]) !=m:
                return False
        return size
    
    def row(self,n):
        return self.M[n]
    
    def column(self,n):
        Size=self.Shape(self.M)
        hold=[]
        for i in range(Size[0]):
            hold.append(self.M[i][n])
        return hold
    
    def block(self,n_0,n_1,m_0,m_1):
        ####### n is columns this time *confusing* and m is rows
        hold=[[0] * (n_1-n_0+1) for z in range(m_1-m_0+1)]
        x=0
        y=0
        try:
            for i in range(m_0,m_1+1):
                for j in range(n_0,n_1+1):
                    hold[x][y]=self.M[i][j]
                    y+=1
                y=0
                x+=1
        except IndexError:
            print "Failed"
        return hold
    
    def transpose(self):
        Size=self.Shape(self.M)
        P=[[0] * Size[0] for i in range(Size[1])]
        if Size==False:
            return "cannot perform operation"
        hold=[[0] * Size[0] for i in range(Size[1])]
        for i in range(Size[0]):
            for j in range(Size[1]):
                hold[j][i]=self.M[i][j]
        P=list(hold)
        return P
    
    def __mul__(self,c):
        Size=self.Shape(self.M)
        P=[[0] * Size[0] for i in range(Size[1])]
        if Size==False:
            return "cannot perform operation"
        for i in range(Size[0]):
            for j in range(Size[1]):
                P[i][j]=self.M[i][j]*c
        return P
    
    def __add__(self,N):
        Size_M=self.Shape(self.M)
        Size_N=self.Shape(N)
        if Size_N==False or Size_M==False:
            return "cannot perform operation"
        P=[[0.0] * self.m for i in range(self.n)]
        if Size_M[0]==Size_N[0] and Size_M[1]==Size_N[1]:
            for i in range(Size_M[0]):
                for j in range(Size_M[1]):
                    P[i][j]=self.M[i][j]+N[i][j]
        else:
            return "Cannot add. Not the same dimensions"
        return P

    def __sub__(self,N):
        Size=self.Shape(N)
        for i in range(Size[0]):
            for j in range(Size[1]):
                N[i][j]=N[i][j]*-1
        P=self.__add__(N)
        for i in range(Size[0]):
            for j in range(Size[1]):
                N[i][j]=N[i][j]*-1
        return P
    
    def elementmult(self,N):
        Size_M=self.Shape(self.M)
        Size_N=self.Shape(N)
        P=[[0.0] * self.m for i in range(self.n)]
        if Size_M[0]==Size_N[0] and Size_M[1]==Size_N[1]:
            for i in range(Size_M[0]):
                for j in range(Size_M[1]):
                    P[i][j]=self.M[i][j]*N[i][j]
        else:
            return "Cannot do element-wise product"
        return P
    
    def __matmult__(self,N):
        Size_M=self.Shape(self.M)
        Size_N=self.Shape(N)
        K=[[0] * Size_N[1] for i in range(Size_M[0])]
        x=0
        Hold_Sum=0
        if Size_M[1]==Size_N[0]:
            P=list(self.transpose())
            for k in range(Size_M[0]):
                for j in range(Size_N[1]):
                    for i in range(Size_N[0]):
                        Hold_num=P[i][k]*N[i][j]
                        Hold_Sum=Hold_Sum+Hold_num 
                    K[k][j]=Hold_Sum
                    Hold_Sum=0
        else:
            return "Cannot be multiplied"
        return K
    
    def rand(self,n,m):
        import random
        K=[[0.0] * m for i in range(n)]
        for i in range (n):
            for j in range (m):
                K[i][j]=random.random()
   
        return K

class Vector(Matrix):
    def __init__(self,A=list(),B=list()):
        self.A=A
        self.B=B
        
    def dot(self):
        Size_A=len(self.A)
        Size_B=len(self.B)
        Hold_Sum=0
        if Size_A==Size_B:
            for i in range(Size_A):
                Hold_Sum=Hold_Sum+(self.A[i]*self.B[i])
        else:
            "cannot to cross product with different number of columns"
        return Hold_Sum

    def out(self):
        Size_A=len(self.A)
        Size_B=len(self.B)
        P=[[0] * len(self.A) for i in range(len(self.A))]
        if Size_A==Size_B:
            for i in range(Size_A):
                for j in range(Size_A):
                    P[i][j]=self.A[i]*self.B[j]
        else:
            "cannot to cross product with different number of columns"
        return P
    
    def norm(self,A,i):
        import math
        hold=0
        for j in range(0,len(A)):
            A[j]=abs(A[j])
        if i==0:
            for j in range(0,len(A)):
                if [j]>hold:
                    hold=A[j]
            return hold


        else:
            for j in range(0,len(A)):
                z=A[j]**i
                hold=hold+z
            hold=float(hold)**(1.0/i)
            return hold