class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                               "-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
                               "-","..-","...-",".--","-..-","-.--","--.."]
        unique_morse_codes = set()
        for word in words:
            morse_code_word = ""
            for c in word:
                morse_code_word += morse_code_alphabet[ord(c) - 97]
            unique_morse_codes.add(morse_code_word)
        return len(unique_morse_codes)
