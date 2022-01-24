# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more
# than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
#
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

def duplicate_count(text):
    my_list = []
    count = 0
    for sym in text.lower():
        my_list.append(sym)
    my_set = set(my_list)
    for char in my_set:
        if my_list.count(char) > 1:
            count += 1
    return count

print(duplicate_count(""))

    # for char in chars:
    #     count = check_string.count(char)
    #     if count > 1:
    #         print
    #         char, count






    # import codewars_test as test
    # from solution import duplicate_count
    #
    # @test.describe("Fixed Tests")
    # def fixed_tests():
    #     @test.it("Basic Tests")
    #     def basic_tests():
    #         test.assert_equals(duplicate_count(""), 0)
    #         test.assert_equals(duplicate_count("abcde"), 0)
    #         test.assert_equals(duplicate_count("abcdeaa"), 1)
    #         test.assert_equals(duplicate_count("abcdeaB"), 2)
    #         test.assert_equals(duplicate_count("Indivisibilities"), 2)