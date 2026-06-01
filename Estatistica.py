def estatistica (a,b,c): 
    soma=a+b+c
    media=(a+b+c)/3
    maior= max(a,b,c)
    return soma,media, maior

print(estatistica(10,11,13))