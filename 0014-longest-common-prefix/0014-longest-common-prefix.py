class Solution:
    def longestCommonPrefix(self, string: List[str]) -> str:
        if "" in string:
            return ""

        shortest_string = ""
        for i in string:
            if len(i) < len(shortest_string) or shortest_string == "":
                shortest_string = i

        j = 0
        while j < len(string):
            if string[j][0] == shortest_string[0]:
                if j == shortest_string:
                    j=j+1
                elif shortest_string in string[j][:len(shortest_string)]:
                    j += 1
                elif shortest_string not in string[j][:len(shortest_string)]:
                    shortest_string = shortest_string[:-1]
                    j -= 1
            else:
                return ""
        return shortest_string
    