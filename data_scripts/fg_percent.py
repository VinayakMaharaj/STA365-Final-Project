

if __name__ == '__main__':
    # expressed as decimal, not percent despite the name
    names = ["stephen curry", "klay thompson", "al horford", "tyreke evans", "anthony davis", "monta ellis", "nikola vucevic", "kyrie irving", "lebron james", "markieff morris", "james harden", "rudy gay", "chris paul", "blake griffin", "lamarcus aldridge"]
    fg = [0.487, 0.463, 0.538, 0.447, 0.535, 0.445, 0.523, 0.468, 0.488, 0.465, 0.44, 0.455, 0.485, 0.502, 0.466]
    fg_percent = {}
    for i in range(len(fg)):
        fg_percent[names[i]] = fg[i]
    
    
    
    