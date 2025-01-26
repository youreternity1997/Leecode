# Edited on 2025-01-26 23:39:24 edit
# Edited on 2025-01-26 23:38:30 edit
        return 0;
    elif n == 1:
        return 1;
    return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(7))