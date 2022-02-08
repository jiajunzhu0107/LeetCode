def split_primes(input_str: str) -> int:
    # boundary -> num of ways
    dp = [-1 for _ in range(len(input_str) + 1)]
    dp[0] = 1
    for i in range(1, len(input_str) + 1):
        dp[i] = sum(
            dp[i - n]
            # length of last number
            # at most 3 digits,
            # and cannot be more than the num of characters we have scanned
            for n in range(1, min(3, i) + 1)
            # not contain leading 0, and is prime
            if input_str[i - n] != '0' and int(input_str[i - n:i]) in primes
        )
    return dp[-1]
a = dp[i - n]  for n in range(1, min(3, i) + 1) if input_str[i - n] != '0' and int(input_str[i - n:i]) in primes

temp = []
for n in range(1, min(3, i) + 1):
    if input_str[i - n] != '0' and int(input_str[i - n:i]) in primes:
        temp.append(dp[i-n])

dp[i] = sum(
            a
        )