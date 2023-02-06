

def reverse_a_list(l1):
    j = 0 
    new_list = []
    for i in range(5-1,-1,-1):
        new_list.append(l1[i])
    
    print(new_list)




l1 = [1,2,3,4,5]
reverse_a_list(l1)

# Slightly complex but simple solution.

print(l1[::-1])