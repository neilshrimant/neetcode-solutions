class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        match_map = defaultdict(set)

        for w1, w2 in similarPairs:
            match_map[w1].add(w2)
            match_map[w2].add(w1)

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or sentence1[i] in match_map[sentence2[i]]:
                    continue
            return False    
              
        return True
                    
