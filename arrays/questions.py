def anagram_checker(s1: str, s2: str) -> bool:
    # Anagram Check:
    # (Given two strings, check to see if they are anagrams.
    # An anagram is when two strings can be written using
    # the exact same letters)
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False
    for ch in s1:
        if ch not in s2:
            return False
    return True


if __name__ == "__main__":

    print(anagram_checker('Dormitory', 'Dirty room'))
    print(anagram_checker('Conversation', 'Voices rant on'))
    print(anagram_checker('dog', 'god'))
