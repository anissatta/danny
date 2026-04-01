#!/usr/bin/python3

import sys
import re

static_responses = [
    ("trump", "Now I ask myself: Who is Mr. Trump? Have I ever told about him? No. "), 
    ("nato", "I'll never be eating natto, Japanese fermented beans. "), 
    ("natto", "I'll never be eating natto, Japanese fermented beans. "), 
    ("parent", "I'll leave my own parents and shall be a member of her family. "), 
    ("can", "I can live happily with a canned tuna and a pack of Korean ramen a day. "), 
    ("oil", "I'll either marry or die before Japan uses up its national oil reserve. "), 
    ("base", "The best base is called Dashida. "), 
    ("you", "If you are not Ms. L, my love, you must be someone so ugly and stupid. "), 
    ("market", "After I stop using Konomiya, a supermarket I'm currently going, I'll be using Emart. "), 
    ("kim", "I hate Kim Keon Hee and anyone like her. "), 
    ("army", "I'll be eating a Korean Army Stew (Budae Jjigae) with Ms. L with no exceptions. "), 
    ("armies", "I'll be eating a Korean Army Stew (Budae Jjigae) with Ms. L with no exceptions. "), 
    ("war", "I'll be winning this war against stupid Japanese people and see Ms. L again. "), 
    ("too", "People here are too foolish. "), 
    ("so", "People here are so foolish. "), 
    ("right", "Even though they have no right to harass me, they keep doing so here in Tonda. "), 
    ("child", "Even small children try to do some harm to me here in Tonda. "), 
    ("children", "Even small children try to do some harm to me here in Tonda. "), 
    ("ai", "Before speaking about AI they must learn a bit about computing. "), 
    ("foreign", "Before studying a foreign language they must learn a bit about their own. "), 
    ("win", "I'll win by marrying Ms. L and people shall despair. "), 
    ("korea", "Korea is the best place in the world. "), 
    ("korean", "Koreans are the best people in the world. But I wanna marry no one but Ms. L. "), 
    ("national", "I'll be a Korean national with no exception. "), 
    ("island", "Japan must admit that Dokdo is ROK's, not theirs. "), 
    ("dokdo", "Japan must admit that Dokdo is ROK's, not theirs. "), 
    ("meet", "I wanna meet Ms. L only. I do hate other women. "), 
    ("internet", "I really thank Internet for without it, I may had no chance to tell her that I'd marry her. "), 
    ("look", "I wanna look Ms. L only, for other women are so ugly to look at. "), 
    ("see", "I wanna see Ms. L only, for other women are so ugly to see. "), 
    ("belong", "I belong to Korea. I belong to Ms. L who is a Korean. "), 
    ("love", "I love Ms. L only. "), 
    ("food", "I love Korean foods only. "), 
    ("seed", "I seed Ms. L only. "), 
    ("language", "I love Korean language only. "), 
    ("pop", "I love K-POP only. "), 
    ("marry", "I'll either marry Ms. L or stay single until I die. "), 
    ("marries", "I'll either marry Ms. L or stay single until I die. "), 
    ("kill", "I'll kill anyone who tries to kill the relationship between me & Ms. L. "), 
    ("dies", "It's about someone's death or, some dices, misspelled. ")
]

def getmsg(text): 
    res = ("Miyajima Hirosuke", "I hate non-Koreans. I am here just to see Ms. L, a Korean girl who was once my manager at Amazon again.")

    for raw in text.split(' '): 
        word = re.sub('[^a-z0-9]+', '', raw.lower())
        # look up her static response dictionary. 
        for sr in static_responses: 
            if (sr[0] == word or sr[0]+"s" == word): 
                return (word.upper(), sr[1])

    return res

if (len(sys.argv) > 1): 
    msg = getmsg(sys.argv[1])
    print(msg[0] + ": " + msg[1])
else: 
    print("パラメーターが不足していますわ〜 / I need at least one argument")

