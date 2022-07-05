class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        output = ''
        indices_dict = {index:seq for seq, index in enumerate(indices)}
        i = 0
        while i < len(s):
            if i in indices_dict:
                length_source = len(sources[indices_dict[i]])
                if s[i:i+length_source] == sources[indices_dict[i]]:
                    output += targets[indices_dict[i]]
                    i += length_source
                else:
                    output += s[i]
                    i += 1
            else:
                output += s[i]
                i += 1
        return output