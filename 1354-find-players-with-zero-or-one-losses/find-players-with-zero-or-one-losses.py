class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans1=[]
        ans2=[]
        players=set()
        loser=[j for i,j in matches]
        l=set(loser)
        freq=Counter(loser)
        for key,val in freq.items():
            if val==1:
                ans2.append(key)
        for i in range(len(matches)):
            players.add(matches[i][0])
            players.add(matches[i][1])
        players=list(players)
        for j in players:
            if j not in l:
                ans1.append(j)
        ans1.sort()
        ans2.sort()
        return [ans1,ans2]


