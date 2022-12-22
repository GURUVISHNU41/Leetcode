class Solution:
    def groupAnagrams(self, strs):
        sd = collections.defaultdict(list)
        for s in strs:
            s_ = ''.join(sorted(s))
            sd[s_].append(s)
            
        return [l for k,l in sd.items()]
