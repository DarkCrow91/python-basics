name1=input("whats boys name")
name2=input("whats girls name")
def love_calculator(name1, name2):
    
    true_word = ["t", "r", "u", "e"]
    love_word = ["l", "o", "v", "e"]
    
    
    combine_name = (name1 + name2).lower()
    
    
    true_count = 0
    for letter in combine_name:
        if letter in true_word:
            true_count += 1
    
    
    love_count = 0
    for letter in combine_name:
        if letter in love_word:
            love_count += 1
    
    
    love_score = int(str(true_count) + str(love_count))
    
    
    if love_score > 100:
        love_score = 100
    
    return f"Love Score: {love_score}%"


print(love_calculator(name1, name2))