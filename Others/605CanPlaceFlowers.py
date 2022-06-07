class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        flowers = 0
        i = 0
        while(i < len(flowerbed)):
            if prev == 1:
                prev = flowerbed[i]
                i += 1
                # continue
            else:
                if flowerbed[i] == 1:
                    i += 1
                    prev = 1
                    # continue
                else:
                    if i+1 == len(flowerbed):
                        flowers += 1
                        break
                    if flowerbed[i+1] == 1:
                        i += 2
                        prev = 1
                        # continue
                    else:
                        flowers += 1
                        prev = 1
                        i += 1
                        # continue
            # print(flowers)
        return flowers >= n