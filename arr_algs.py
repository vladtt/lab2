mass = [1, 3, 5, 7];
def min (mass):
    m = mass [0];
    for x in mass:
        if x < m:
            m=x;
    return m;

def av (mass):
    return sum(mass)/len(mass)

print (min (mass));
print (av (mass))




