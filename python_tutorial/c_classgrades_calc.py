grades= [100,102,50,45]

def max(grades):
    largest=0
    
    for k in grades:
        if k>100:
            largest = 100
        elif k>largest:
            largest = k 
    return largest

def grades_highestlow(grades):
    return (min(grades),max(grades))

