class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count ={}
        # freq = [[] for i in range (len(nums)+1)]

        # for n in nums:
        #     count[n] = 1 +count.get(n,0)
        # for n , c in count.item():
        #     freq[c].append(n)

        # res =[]
        # for i in range(len(freq)-1,0,-1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             retrn res

        # Create a frequency map
        frequency_map = defaultdict(int)
        for n in nums:
            frequency_map[n] += 1

        # Create buckets where index represents frequency
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequency_map.items():
            bucket[freq].append(num)

        # Collect the top k frequent elements
        top_k = []
        for pos in range(len(bucket) - 1, 0, -1):
            if bucket[pos]:
                top_k.extend(bucket[pos])
                if len(top_k) >= k:
                    return top_k[:k]
        
        return top_k

        