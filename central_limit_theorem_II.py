# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

numTicket = float(input())
numStd = float(input())
mu_sum = numStd * float(input())
sig_sum = math.sqrt(numStd) * float(input())

print(round(0.5*(1+math.erf((numTicket - mu_sum)/(sig_sum * math.sqrt(2)))),4))