class Solution:
    def justifyFull(self, line_words, line_width, target_width):
        # print(line_width)
        remain_width = target_width - line_width
        num_space_slots = len(line_words) - 1
        if len(line_words) == 1:
            return line_words[0] + (' ' * remain_width)
        num_space = remain_width // num_space_slots
        if remain_width % num_space_slots != 0:
            for i in range(remain_width % num_space_slots):
                line_words[i] += ' ' 
        return (' ' * (num_space + 1)).join(line_words)
    
    def justifyLeft(self, line_words, line_width, target_width):
        return ' '.join(line_words) + (' ' * (target_width - line_width))
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        current_line_words = []
        current_line_width = -1
        
        i = 0
        while i < len(words):
            word = words[i]
            length_word = len(word)
            if current_line_width + length_word + 1 <= maxWidth:
                current_line_words.append(word)
                current_line_width += 1 + length_word
                # print(current_line_words, current_line_width)
                i += 1
            else:
                
                output.append(self.justifyFull(current_line_words, current_line_width, maxWidth))
                current_line_words = []
                current_line_width = -1
        output.append(self.justifyLeft(current_line_words, current_line_width, maxWidth))
        return output
                
            
            