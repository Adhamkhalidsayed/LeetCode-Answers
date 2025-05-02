# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        guesses_used = 0
        guessed_letters = 0

        def match(word, random_word):
            letters_matched = 0
            for i in range(6):
                if word[i] == random_word[i]:
                    letters_matched += 1
            return letters_matched

        while words:
            if guessed_letters == 6:
                return
            random_word = random.choice(words)
            guessed_letters = master.guess(random_word)
            candidates = []
            for word in words:
                matched_letters = match(word, random_word)
                if matched_letters == guessed_letters:
                    candidates.append(word)
            
            guesses_used +=1
            words = candidates
        

                

            