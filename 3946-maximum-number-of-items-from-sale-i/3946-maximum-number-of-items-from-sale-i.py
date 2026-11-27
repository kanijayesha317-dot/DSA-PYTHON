from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # bonus[i] = kitne free copies milenge agar item i ki kam se kam 1 copy kharidi jaye
        bonus = [0] * n
        for i in range(n):
            fi = items[i][0]
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            bonus[i] = cnt

        # dp[b] = budget 'b' spend karke maximum total items (purchased + free)
        dp = [0] * (budget + 1)

        for idx, (_, price) in enumerate(items):
            if price > budget:
                continue

            # 1. First copy (0/1 step): 1 purchased item + bonus[idx] free items
            first_gain = 1 + bonus[idx]
            for b in range(budget, price - 1, -1):
                candidate = dp[b - price] + first_gain
                if candidate > dp[b]:
                    dp[b] = candidate

            # 2. Extra copies (unbounded step): har extra copy par +1 item (no extra bonus)
            for b in range(price, budget + 1):
                candidate = dp[b - price] + 1
                if candidate > dp[b]:
                    dp[b] = candidate

        return max(dp)