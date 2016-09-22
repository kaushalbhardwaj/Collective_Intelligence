import random

#In this clustering algorithm we predecide finite number of centroids or no of groups in which we cluster our data
#Better than hierarchial method as cluster are less

#Tanimoto coefficient can be used to find similarity between dataset in which data is represented
#as 1 or 0 present or not.For this pearson method cannot be used as it does not contain count of anything

#We can use various python libraries to represent data in 2-D and can get jpeg for it





def kcluster(rows,distance=pearson,k=4):
ranges=[(min([row[i] for row in rows]),max([row[i] for row in rows]))
for i in range(len(rows[0]))]
clusters=[[random.random( )*(ranges[i][1]-ranges[i][0])+ranges[i][0]
for i in range(len(rows[0]))] for j in range(k)]
lastmatches=None
for t in range(100):
print 'Iteration %d' % t
bestmatches=[[] for i in range(k)]
for j in range(len(rows)):
row=rows[j]
bestmatch=0
for i in range(k):
d=distance(clusters[i],row)
if d<distance(clusters[bestmatch],row): bestmatch=i
bestmatches[bestmatch].append(j)
if bestmatches==lastmatches: break
lastmatches=bestmatches
for i in range(k):
avgs=[0.0]*len(rows[0])
if len(bestmatches[i])>0:
for rowid in bestmatches[i]:
for m in range(len(rows[rowid])):
avgs[m]+=rows[rowid][m]
for j in range(len(avgs)):
avgs[j]/=len(bestmatches[i])
clusters[i]=avgs
return bestmatches
