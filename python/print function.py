# Output Format

# Print the list of integers from  through  as a string, without spaces.

# Sample Input 0

# 3
# Sample Output 0

# 123

if __name__ == '__main__':
    print(*range(1, int(input())+1), sep='')