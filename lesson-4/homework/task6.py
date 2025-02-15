prime_numbers = []

for num in range(2,101):
    is_prime = True
    
    for divisor in range(2, int(num**0.5)+1):
        if num % divisor == 0:
            is_prime = False
            break
        
    if is_prime:
        prime_numbers.append(num)

print(prime_numbers)
            
            