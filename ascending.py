s=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(s)):
    for j in range(i+1,len(s)): 
        if s[i][1]>s[j][1]:
            s[i],s[j]=s[j],s[i]  
print(s)