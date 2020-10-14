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


def rev_word(string: str) -> str:
    # Given a string of words, reverse all the words
    # 1st way
    lst = string.split()
    rev = ' '.join(lst[::-1]).strip()

    # 2nd way
    result = ''
    for i in reversed(lst):
        result += i + " "
    return result.strip()


def compress(s: str):
    if len(s) == 0:
        return 'String is empty'
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        count.setdefault(i, 1)
    result = ''.join(f'{k}{v}' for (k, v) in count.items())
    return result


if __name__ == "__main__":
    a = compress('aABBcC')
    print(a)
    # print(rev_word('What do we have here ? '))
    # print(anagram_checker('Dormitory', 'Dirty room'))
    # print(anagram_checker('Conversation', 'Voices rant on'))
    # print(anagram_checker('dog', 'god'))
