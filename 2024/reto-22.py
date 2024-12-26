
# Reto: https://adventjs.dev/es/challenges/2024/22

def generate_gift_sets(gifts):

    result = [];n = len(gifts)
    
    def backtrack(start, current_combination):
        
        if len(current_combination) > 0:result.append(current_combination[:])
        
        for i in range(start, n):
            current_combination.append(gifts[i])
            backtrack(i + 1, current_combination)
            current_combination.pop()
    
    backtrack(0, []);result.sort(key=len)

    return result
