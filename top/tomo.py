#!/usr/bin/python3

import sys
import re

static_responses = [
    ("iran", "Japan and its allies excluding ROK must send a ship to the Strait of Hormuz so that we can buy their oil again."), 
    ("iranian", "Japan and its allies excluding ROK must send a ship to the Strait of Hormuz so that we can buy their oil again."), 
    ("trump", "Japan and other countries excluding ROK must pay more money to Trump so that we can save ours. "), 
    ("takaichi", "Takaichi must create a nation which can deter China so that we can stay nice both to China and Taiwan. "), 
    ("island", "Japan must admit that Dokdo is ROK's, not theirs. "), 
    ("islands", "Japan must admit that Dokdo is ROK's, not theirs. "), 
    ("dokdo", "Japan must admit that Dokdo is ROK's, not theirs. "), 
    ("win", "I'll win by marrying Ms. L and people shall despair. "), 
    ("wins", "I'll win by marrying Ms. L and people shall despair. "), 
    ("national", "I'll be a Korean national with no exception. "), 
    ("korea", "Korea is the best place in the world. "), 
    ("korean", "Koreans are the best people in the world. But I wanna marry no one but Ms. L. "), 
    ("koreans", "Koreans are the best people in the world. But I wanna marry no one but Ms. L. "), 
    ("japan", "Japan must deter China. That's the reason why it is still permitted to exist. "), 
    ("philippines", "Philippines must keep playing with fire with Japan. "), 
    ("drug", "I think Americans must use TrumpRx but I won't use myself because I'm not an American. "), 
    ("melania", "I think Americans must watch Melania, a film but I won't watch myself because I'm not an American. "),  
    ("war", "Japan must have at least two warheads to deter China and North Korea. "), 
    ("meet", "I wanna meet Ms. L only. I do hate other women. "), 
    ("meets", "I wanna meet Ms. L only. I do hate other women. "), 
    ("internet", "I really thank Internet for without it, I may had no chance to tell her that I'd marry her. "), 
    ("look", "I wanna look Ms. L only, for other women are so ugly to look at. "), 
    ("looks", "I wanna look Ms. L only, for other women are so ugly to look at. "), 
    ("see", "I wanna see Ms. L only, for other women are so ugly to see. "), 
    ("sees", "I wanna see Ms. L only, for other women are so ugly to see. "), 
    ("belong", "I belong to Korea. I belong to Ms. L who is a Korean. "), 
    ("belongs", "I belong to Korea. I belong to Ms. L who is a Korean. "), 
    ("love", "I love Ms. L only. "), 
    ("loves", "I love Ms. L only. "), 
    ("food", "I love Korean foods only. "), 
    ("foods", "I love Korean foods only. "), 
    ("language", "I love Korean language only. "), 
    ("languages", "I love Korean language only. "), 
    ("pop", "I love K-POP only. "), 
    ("pops", "I love K-POP only. "), 
    ("marry", "I'll either marry Ms. L or stay single until I die. "), 
    ("marries", "I'll either marry Ms. L or stay single until I die. "), 
    ("kill", "I'll kill anyone who tries to kill the relationship between me & Ms. L. "), 
    ("kills", "I'll kill anyone who tries to kill the relationship between me & Ms. L. "), 
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

