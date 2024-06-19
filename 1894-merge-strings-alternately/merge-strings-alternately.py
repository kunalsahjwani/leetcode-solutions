class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        char_list = list(word1)
        char_list2 = list(word2)
        sentence =[]
        for i, j in zip(char_list, char_list2):
            sentence.append(i)
            sentence.append(j)
        
        # If word1 is longer, add the remaining characters
        if len(char_list) > len(char_list2):
            sentence.extend(char_list[len(char_list2):])
        
        # If word2 is longer, add the remaining characters
        if len(char_list2) > len(char_list):
            sentence.extend(char_list2[len(char_list):])
        
        # Join the list into a single string
        string = ''.join(sentence)
        return string

        