"""DNA"""
def find_longest_common_substring(dna1, dna2):
    """i'll find you"""
    def valid_dna(dna):
        """check dna"""
        return all(c in 'ACGT' for c in dna)

    if not valid_dna(dna1) or not valid_dna(dna2):
        return "Error"

    def common_longest(s1, s2):
        """very long"""
        len1, len2 = len(s1), len(s2)
        longest = ""

        ding = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    ding[i][j] = ding[i - 1][j - 1] + 1
                    if ding[i][j] > len(longest):
                        longest = s1[i - ding[i][j]:i]
                else:
                    ding[i][j] = 0

        return longest if longest else "None"

    return common_longest(dna1, dna2)

print(find_longest_common_substring(input().strip(), input().strip()))
