from math import sqrt


#Collaborative filtering
#Dictionary of movies and critics score showing rating by critics for any movie

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
'The Night Listener': 4.5, 'Superman Returns': 4.0,
'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


#Euclidean distance score method to find similarity between two movies
def sim_distance(prefs,person1,person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si=[item]=1

    if len(si)==0:
        return 0

    sum_square=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sum_square)

#Pearson correlation score method which corrects grade inflation problem and is more precise

def sim_pearson(prefs,p1,p2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    if len(si)==0:
        return 0
    sum1=sum(prefs[p1][item] for item in si)
    sum2=sum(prefs[p2][item] for item in si)
    sum1sq=sum([pow(prefs[p1][item],2) for item in si])
    sum2sq=sum([pow(prefs[p2][item],2) for item in si])
    p_sum=sum([prefs[p1][item]*prefs[p2][item] for item in si])
    n=len(si)

    num=p_sum-(sum1*sum2/n)
    den=sqrt((sum1sq-pow(sum1,2)/n)*(sum2sq-pow(sum2,2)/n))
    if den==0: return 0

    r=num/den
    return r

#Ranking the critics according to similarity with the person p1

def topMatches(prefs,p1,n=5,sim=sim_pearson):
    scores=[(similarity(prefs,p1,other),other) for other in prefs if other!=p1]
    scores.sort()
    scores.reverse()
    return scores[0:n]

#Recommending items for the person by comparing each person with all users one by one

def getRecommendation(prefs,p,similarity=sim_pearson):
    total={}
    simSum={}

    for other in prefs:
        if other==p: continue
        sim=similarity(prefs,p,other)

        if sim<=0: continue
        for item in prefs[other]:
            if item not in prefs[p] or prefs[p][item]==0:
                total.setdefault(item,0)
                total[item] +=prefs[other][item]*sim
                simSum.setdefault(item,0)
                simSum[item] +=sim

    ranking=[(t/simSum[item],item) for item,t in total.item() ]
    ranking.sort()
    ranking.reverse()
    return ranking

#Transform dictionary to find similar movies instead of users on the basis of users rating for that movie
def transformPrefs(prefs):
    result={}
    for p in prefs:
        for item in prefs[p]:
            result.setdefault(item,{})
            result[item][p]=prefs[p][item]

    return result

#Item-Based filtering

def calculateSimilarItems(prefs,n=10):
    result={}
    itemPref=transformPrefs(prefs)
    for item in itemPref:
        score=topMatches(itemPref,item,n=n,similarity=sim_distance)
        result[item]=score

    return result

def getRecommendationItem(pref,itemMatch,user):
    userRatings=pref[user]
    scores={}
    total={}

    for (similarity,item2) in itemMatch[item]:
        if item2 in userRatings: continue
        scores.setdefault(item2,0)
        scores[item2]+=similarity*rating
        totalSim.setdefault(item2,0)
        totalSim[item2]+=similarity
        rankings=[(score/totalSim[item],item) for item,score in scores.items( )]
        rankings.sort( )
        rankings.reverse( )

    return rankings
