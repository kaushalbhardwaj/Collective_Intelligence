from math import sqrt

#Unsupervised Learning Algorithm

 #Pearson distance method to find similarity between two vector sets which are actully word count
 def pearson(v1,v2):
     s1=sum(v1)
     s2=sum(v2)

     sq1=sum([pow(v,2) for v in v1])
     sq2=sum([pow(v,2) for v in v2])

     psum=sum([v1[i]*v2[i] for i in range(len(v1))])

     num=psum-(sum1*sum2/len(v1))
     den=sqrt((sq1-pow(s1,2)/len(v1))*(sq2-pow(s2,2)/len(v2)))
     if den==0: return 0
     return 1.0-num/den

#Defination of Cluster containg data and methods

class bicluster:
    def _init__(self,v,l=None,r=None,d=0.0,id=None):
        self.v=v
        self.l=l
        self.r=r
        self.d=d
        self.id=id

#hierarchical Algorithm for blog word count
    def hcluster(rows,distance=pearson):
        dis={}
        clustId=-1
        clust=[bicluster(rows[i],id=1) for i in range(len(rows))]

        while len(clust)>1:
            lowestpair=(0,1)
            c=distance(clust[0].v,clust[1].v)

        for i in range(len(clust)):
            for j in range(i+1,len(clust)):
                if(clust[i].id,clust[j].id) not in dis:
                    dis[(clust[i].id,clust[j].id)]=distance(clus[i].v,clust[j].v)

                d=dis[(clust[i].id,clust[j].id)]
                if d<c:
                    c=d
                    lowestpair=(i,j)
            mer=[(clust[lowestpair[0]].v[i]+clust[lowestpair[1].v[i]]/2.0 for i in range(len(clust[0].v)))]

            newCluster=bicluster(mer,l=clust[lowestpair[0],r=clust[lowestpair[1],d=c,id=clustId]])

            clustId=-1
            del clust[lowestpair[1]]
            del clust[lowestpair[0]]
            clust.append(newCluster)

            return clust[0]

#We can use this final return cluster to make Dendrogram which is a tree to represent cluster graphically

#We can also interchange/transpose this two dimensional matrix to find many more relevant clusters in the dataset
