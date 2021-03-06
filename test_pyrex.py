import unittest
import pyrex

class TestPyrex(unittest.TestCase):
    def test_single_literal(self):
        self.assertEqual((0, 1), pyrex.rex('a').match('a'))

    def test_malformed_expression(self):
        self.assertRaises(Exception, pyrex.rex, '*')

    def test_malformed_expression_starting_with_parethensis(self):
        self.assertRaises(Exception, pyrex.rex, ')a')

    def test_single_literal_in_the_middle(self):
        self.assertEqual((1, 2), pyrex.rex('a').match('ba'))

    def test_single_literal_matching_multiple_times(self):
        self.assertEqual((0, 1), pyrex.rex('a').match('aa'))

    def test_double_literal(self):
        self.assertEqual((0, 2), pyrex.rex('aa').match('aa'))

    def test_double_literal_matching_multiple_times(self):
        self.assertEqual((0, 2), pyrex.rex('aa').match('aaaa'))

    def test_simple_repetition(self):
        self.assertEqual((0, 2), pyrex.rex('a+').match('aa'))

    def test_simple_repetition_with_optional(self):
        self.assertEqual((0, 2), pyrex.rex('a+?').match('aa'))

    def test_simple_repetition_zero_or_more(self):
        self.assertEqual((0, 2), pyrex.rex('a*').match('aa'))

    def test_will_match_zero_width_string(self):
        self.assertEqual(None, pyrex.rex('a*').match(''))
        self.assertEqual(None, pyrex.rex('a*').match('b'))

    def test_simple_repetition_zero_or_one(self):
        self.assertEqual((0, 2), pyrex.rex('aa?').match('aa'))

    def test_options_simple(self):
        self.assertEqual((0, 2), pyrex.rex('ab|aa').match('aab'))

    def test_grouping_simple(self):
        self.assertEqual((0, 5), pyrex.rex('a(ab)+').match('aabab'))

    def test_would_never_end(self):
        self.assertEqual(None, pyrex.rex('(.+.+)+y').match('a'*29))

    def test_will_match_greedly(self):
        self.assertEqual((0, 30), pyrex.rex('(.+.+)+y').match('a'*29+'y'))

    def test_will_match_greedly_in_the_middle(self):
        self.assertEqual((1, 31), pyrex.rex('a(.+.+)+y').match('b' + 'a'*29+ 'yb'))

    def test_article_specially_crafted_regex(self, n=100):
        self.assertEqual((0, n), pyrex.rex('a?'*n+'a'*n).match('a'*n))

    def test_regex_source(self):
        self.assertEqual('0000: CONSUME a\n0001: JUMP (1, 2)\n0002: CONSUME b\n0003: MATCH!', str(pyrex.rex('ab?')))


        
if __name__ == "__main__":
    unittest.main()
