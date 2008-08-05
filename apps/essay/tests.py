import unittest
from utils import split_text_to_words, count_words_in_list_to_dict, split_text_to_words_dict_with_counts


class UtilsSplitTextToWordsTestCase(unittest.TestCase):
    def testEmptyStr(self):
        text = ''
        
        self.assertEqual(
            split_text_to_words(text),
            []
        )
    
    def testNoWord(self):
        text = '  . - + 123'
        
        self.assertEqual(
            split_text_to_words(text),
            []
        )
    
    def testSingleWord(self):
        text = 'word'
        
        self.assertEqual(
            split_text_to_words(text),
            ['word']
        )
        
    def testSimpleText(self):
        text = 'Simple text.'
        
        self.assertEqual(
            split_text_to_words(text),
            ['Simple', 'text']
        )
        
    def testTwoSentences(self):
        text = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.\nDuis tortor eros. Duis tortor eros, adipiscing sed, scelerisque a, faucibus in, purus.'
        
        self.assertEqual(
            split_text_to_words(text),
            ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetuer', 'adipiscing', 'elit',
             'Duis', 'tortor', 'eros', 'Duis', 'tortor', 'eros', 'adipiscing', 'sed', 'scelerisque',
             'a', 'faucibus', 'in', 'purus']
        )


class UtilsCountWordsInListToDictTestCase(unittest.TestCase):
    def testSimpleText(self):
        words_list = ['Simple', 'text']
        
        self.assertEqual(
            count_words_in_list_to_dict(words_list),
            { 'simple': 1, 'text': 1 }
        )
        
        
    def testTwoSentences(self):
        words_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetuer', 'adipiscing', 'elit',
         'Duis', 'tortor', 'eros', 'Duis', 'tortor', 'eros', 'adipiscing', 'sed', 'scelerisque',
         'a', 'faucibus', 'in', 'purus']
        
        self.assertEqual(
            count_words_in_list_to_dict(words_list),
            { 'a': 1, 'ipsum': 1, 'sed': 1, 'tortor': 2, 'sit': 1, 'scelerisque': 1, 'in': 1, 'purus': 1,
              'elit': 1, 'duis': 2, 'adipiscing': 2, 'dolor': 1, 'consectetuer': 1, 'lorem': 1, 'amet': 1,
              'faucibus': 1, 'eros': 2 }
        )

class UtilsSplitTextToWordsDictWithCountsTestCase(unittest.TestCase):
    def testSimpleText(self):
        text = 'Simple text.'
        
        self.assertEqual(
            split_text_to_words_dict_with_counts(text),
            { 'simple': 1, 'text': 1 }
        )
    
    def testTwoSentences(self):
        text = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.\nDuis tortor eros. Duis tortor eros, adipiscing sed, scelerisque a, faucibus in, purus.'
        
        self.assertEqual(
            split_text_to_words_dict_with_counts(text),
            { 'a': 1, 'ipsum': 1, 'sed': 1, 'tortor': 2, 'sit': 1, 'scelerisque': 1, 'in': 1, 'purus': 1,
              'elit': 1, 'duis': 2, 'adipiscing': 2, 'dolor': 1, 'consectetuer': 1, 'lorem': 1, 'amet': 1,
              'faucibus': 1, 'eros': 2 }
        )
