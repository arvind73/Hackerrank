One line of input: an integer N.

Constraints
0<=N<=15

Output Format

A list on a single line containing the cubes of the first N fibonacci numbers.

Sample Input

5
Sample Output

[0, 1, 1, 8, 27]
Explanation
The first 5 fibonacci numbers are [0,1,1,2,3], and their cubes are [0,1,1,8,27].

Solution #1:
cube = lambda x: pow(x,3)# complete the lambda function 
 def fibonacci(n):
     # return a list of fibonacci numbers
     lis = [0,1]
     for i in range(2,n):
         lis.append(lis[i-2] + lis[i-1])
     return(lis[0:n])
  

Solution #2:
inp = int(input())

cube = lambda x: x**3 # complete the lambda function

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

print(list(map(cube, list(fibonacci(inp)))))


Solution #3:
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
print(list(map(lambda x: x**3, fib[:int(input())])))
