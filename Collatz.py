def collatz(num):
    num_of_steps=0
    while num!=1:
        if num%2==0:
            num/=2
            num_of_steps+=1
        else:
            num=(num*3)+1
            num_of_steps+=1
    return(f'{num_of_steps} steps')

print(collatz(2992929292))

        