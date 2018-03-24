from nose.tools import *
from ex48 import parser


def test_parse_subject():
    assert_equal(parser.parse_subject([('noun', 'bear')]), ('noun', 'bear'))
    assert_equal(parser.parse_subject([('verb', 'eat')]), ('noun', 'player'))
    assert_equal(parser.parse_subject([('stop', 'of'), ('noun', 'bear')]), ('noun', 'bear'))


def test_parse_sentence():
    sentence = parser.parse_sentence([('verb', 'go'),
                                      ('stop', 'to'),
                                      ('direction', 'north')])
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'go')
    assert_equal(sentence.object, 'north')
