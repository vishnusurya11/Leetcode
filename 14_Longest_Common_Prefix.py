class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ''
        longest_common_prefix = strs[0]
        common_prefix = ''
        for word_in_list in strs[1:]:
            if len(longest_common_prefix) >= len(word_in_list):
                small_word = word_in_list
                big_word = longest_common_prefix
            else:
                small_word = longest_common_prefix
                big_word = word_in_list
            for i in range(len(small_word)):
                if small_word[i] == big_word[i]:
                    common_prefix = common_prefix + small_word[i]
                else:
                    break
            if len(longest_common_prefix):
                longest_common_prefix = common_prefix
                common_prefix = ''
            else:
                break
        return longest_common_prefix