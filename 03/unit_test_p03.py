'''
------------------------------------------------------------------------------------
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



------------------------------------------------------------------------------------
'''

import p03

class test_case:
    desc     = ''
    a_string = ''
    len      = 3
    expected = ''
# ------------------------------------------------------------------------------------

test_cases = []

t = test_case()
t.desc     = 'example 1.'
t.a_string = 'abcabcbb'
t.bigest   = 'abc'
t.expected = 3
test_cases.append(t)

t = test_case()
t.desc     = 'example 2.'
t.a_string = 'bbbbb'
t.bigest   = 'b'
t.expected = 1
test_cases.append(t)

t = test_case()
t.desc     = 'example 3.'
t.a_string = 'pwwkew'
t.bigest   = 'wke'
t.expected = 3
test_cases.append(t)

t = test_case()
t.desc     = 'example 4.'
t.a_string = 'c'
t.bigest   = 'c'
t.expected = 1
test_cases.append(t)

t = test_case()
t.desc     = 'example 5.'
t.a_string = 'au'
t.bigest   = 'au'
t.expected = 2
test_cases.append(t)

t = test_case()
t.desc     = 'example 6.'
t.a_string = 'aa'
t.bigest   = 'aa'
t.expected = 1
test_cases.append(t)

t = test_case()
t.desc     = 'example 7.'
t.a_string = 'aab'
t.bigest   = 'a'
t.expected = 2
test_cases.append(t)

t = test_case()
t.desc     = 'example 8.'
t.a_string = 'pwwkew'
t.bigest   = 'wke'
t.expected = 3
test_cases.append(t)


# ------------------------------------------------------------------------------------

s = p03.Solution()

for i in test_cases:
    #print( '{} \t{} \t{}'.format( i.desc, i.inputList, i.output ) )
    r = 0
    print( '-' * 69 )
    print( i.desc )
    print( 'a_string = {}'.format( i.a_string     ) )
    #print( 'target   = {}'.format( i.target   ) )
    print( 'expected = {}'.format( i.expected ) )
    r =  s.lengthOfLongestSubstring( i.a_string )
    print( 'result   = {}'.format( r ))
    if i.expected == r:
        print( 'passed: \t\t\t Correct!' )
    else:
        print( 'passed: \t\t\t wrong' )
