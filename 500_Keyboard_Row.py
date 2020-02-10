class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line_1 = 'QWERTYUIOP'
        line_2 = 'ASDFGHJKL'
        line_3 = 'ZXCVBNM'
        check_line = ''
        output_list =[]
        word_in_line = 0
        for word in words:
            if word[0].upper() in line_1:
                check_line = line_1
            if word[0].upper() in line_2:
                check_line = line_2
            if word[0].upper() in line_3:
                check_line = line_3
            for letter in word:
                if letter.upper() in check_line:
                    pass
                else:
                    word_in_line = 1
                    break
            if word_in_line:
                word_in_line = 0
            else:
                output_list.append(word)
        return output_list
        