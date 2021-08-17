# Enter your code here. Read input from STDIN. Print output to STDOUT
def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def cal_b(x,n,p):
    return comb(n,x) * p**x * (1-p)**(n-x)

l, r = list(map(float, input().split(" ")))
odds = 1.09/1
print(round((sum([cal_b(i,6,odds/(1+odds)) for i in range(3,7)])),3))
