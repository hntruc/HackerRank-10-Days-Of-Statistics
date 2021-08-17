# Enter your code here. Read input from STDIN. Print output to STDOUT
averageA, averageB = [float(num) for num in input().split(" ")]
print(round(160 + 40 * (averageA + averageA**2),3))
print(round(128 + 40 * (averageB + averageB**2),3))
