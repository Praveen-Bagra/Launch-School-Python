memo = {}

def fibonacci(nth):
    if nth in [1, 2]:
        return 1
    elif nth in memo:
        return memo[nth]
    else:
        memo[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
        return memo[nth]

print(fibonacci(5))
print(memo)

memo [5] = fibonacci[4] + fibonacci[3]

fibonacci[3] = fibonacci[2] + fibonacci[2]

fibonacci[4] = fibonacci[3] + fibonacci[2]
                    
{3: 2, 4: 3, 5: 5}
