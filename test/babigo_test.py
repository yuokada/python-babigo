# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from future.utils import string_types
from builtins import str
from nose.tools import *
from mock import patch, Mock
import httplib2
import os.path

import babigo

TESTDIR = os.path.dirname(__file__)
APPID = 'yuokada'
CACHE = '/tmp/'

RES = {
    'status': '200'
}
RES_F = {
    'status': '400'
}
CONTENT_1 = open(TESTDIR + '/data/result_01.xml').read()
CONTENT_3 = open(TESTDIR + '/data/result_03.xml').read()


class TestBabigo(object):
    """ test class babigo
    """

    def test_init_01(self):
        """ babbigo concate test

        Arguments:
        - `self`:
        """
        babi = babigo.Babigo()

    def test_init_02(self):
        """ babbigo concate test

        Arguments:
        - `self`:
        """
        babi = babigo.Babigo(APPID, CACHE)

    @patch.object(httplib2.Http, 'request')
    def test_translate_01(self, mk):
        """docstring for test_translate"""
        mk.return_value = (RES, CONTENT_1)
        babi = babigo.Babigo(APPID, CACHE)
        res = babi.translate('hoge')
        pass

    @patch.object(httplib2.Http, 'request')
    def test_get_kana_sentence_01(self, mk):
        """ test_get_kana_sentence_01 """
        mk.return_value = (RES, CONTENT_3)
        babi = babigo.Babigo()
        TEST_STRING = u'頑張ってくださいw'
        EXPECT = u'がんばってくださいw'
        res = babi.get_kana_sentence(TEST_STRING)
        ok_(isinstance(res, string_types))
        eq_(res, EXPECT)

    @patch.object(httplib2.Http, 'request')
    def test_get_kana_sentence_02(self, mk):
        """ test_get_kana_sentence_02 """
        mk.return_value = (RES_F, CONTENT_3)
        babi = babigo.Babigo()
        TEST_STRING = u'頑張ってくださいw'
        EXPECT = False
        res = babi.get_kana_sentence(TEST_STRING)
        eq_(res, EXPECT)

    @patch.object(babigo.Babigo, 'get_kana_sentence')
    def test_translate_sentence2babigo_01(self, mk):
        TEST_SENTENCE = u'頑張ってくださいw'
        MOCK_VALUE = u'がんばってくださいw'
        EXPECT = u'がばんばばってべくぶだばさばいびw'
        mk.return_value = MOCK_VALUE
        babi = babigo.Babigo()
        res = babi.translate_sentence2babigo(TEST_SENTENCE)
        eq_(res, EXPECT)

    @patch.object(babigo.Babigo, 'get_kana_sentence')
    def test_translate_sentence2babigo_01(self, mk):
        TEST_SENTENCE = u'頑張ってくださいw'
        MOCK_VALUE = False
        EXPECT = False
        mk.return_value = MOCK_VALUE
        babi = babigo.Babigo()
        res = babi.translate_sentence2babigo(TEST_SENTENCE)
        eq_(res, EXPECT)

    def test__insert_babi_01(self):
        """test__insert_babi_01: 長いので分割 (1/2)"""
        babi = babigo.Babigo()
        TEST_STRING = u'おはようございます。'
        EXPECT = u'おぼはばよぼうぶごぼざばいびまばすぶ。'
        res = babi._insert_babi(TEST_STRING)
        ok_(isinstance(res, string_types))
        eq_(res, EXPECT)

    def test__insert_babi_02(self):
        """test__insert_babi_02: 長いので分割 (2/2)"""
        babi = babigo.Babigo()
        TEST_STRING = u'いいてんきですね。'
        EXPECT = u'いびいびてべんきびでべすぶねべ。'
        res = babi._insert_babi(TEST_STRING)
        ok_(isinstance(res, string_types))
        eq_(res, EXPECT)
