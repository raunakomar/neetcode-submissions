class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.timer = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.timer,tweetId))
        self.timer+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = []
        tweets = []
        if userId  in self.followers:
            followers = self.followers[userId]
        if(userId in self.tweets):
            tweets.extend(self.tweets[userId])
        for followeeId in followers:
            if followeeId in self.tweets:
                tweets.extend(self.tweets[followeeId])
       
        ans =[]
        tweets.sort(key=lambda x: x[0], reverse=True)
        #for i in range(len(tweets)):
        #    print(userId,"->",tweets[i][1])
        #print("len",len(tweets))
        for i in range(len(tweets)):
            if(i<10):
                ans.append(tweets[i][1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followerId not in self.followers:
            self.followers[followerId] = []
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            return
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)