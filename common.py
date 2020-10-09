# two string
# Given two arrays of strings, determine whether corresponding elements contain a common substring. 
# For example if array a = [ab, cd , ef] and array b = [af, ee, ef] , we make the following decision. 
# [Yes, no , yes]
X = ['aa','bq','de','ef']
Y = ['da','bt','hh','er']
n = len(X)
res = ["NO" for x in range(n)]
count = 0
for x,y in zip(X,Y):
    for xch,ych in zip(x,y):
        if (xch in y) or (ych in x):
            res[count] = "YES"
            break
    count+=1

print(res)