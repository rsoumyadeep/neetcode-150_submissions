class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        count=[[] for i in range(len(nums)+1)]

        for n in nums:
            freq[n]+=1
        for n,c in freq.items():
            count[c].append(n)
        result=[]
        for i in range(len(count)-1,0,-1):
            for n in count[i]:
                result.append(n)
                if(len(result)==k):
                    return result


        