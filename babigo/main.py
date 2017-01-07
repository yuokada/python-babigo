# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from future.utils import string_types
from builtins import str
import os
import os.path
import sys
import httplib2
from bs4 import BeautifulSoup

from future.standard_library import install_aliases
install_aliases()
from urllib.parse import urlencode

if sys.version_info.major == 3:
    import configparser as configparser
else:
    import ConfigParser as configparser


class BabigoException(Exception):
    """ Babigo Exception Class
    """
    pass


class Babigo(object):
    """ Babigo: Babigo Translate Class
    """
    appid = None
    cache = None

    def __init__(self, appid=None, cache=None):
        super(Babigo, self).__init__()
        self.cache = None
        self._read_rcfile()
        if not appid is None:
            self.appid = appid
        if not cache is None:
            self.cache = cache
        return

    def _read_rcfile(self):
        """ read $HOME/.babigorc
        """
        homedir = os.getenv('HOME')
        rcfile = homedir + os.path.sep + '.babigorc'  # don't work on windows
        con = configparser.SafeConfigParser(allow_no_value=True)
        if os.path.exists(rcfile):
            con.read(rcfile)
            self.appid = con.get('SETTINGS', 'appid')
            self.cache = con.get('SETTINGS', 'cache')
        return

    ### dead function
    def translate(self, sentence):
        """ translate your sentence to babigo sentence

        Arguments:
        - `self`:
        - `sentence`:
        """
        h = httplib2.Http(self.cache)
        params = {
            'results': 'ma,uniq',
            'uniq_filter': '9|10',
            'sentence': sentence.encode('utf-8'),
        }
        query = urlencode(params)
        headers = {
            'Host': 'jlp.yahooapis.jp',
            'User-Agent': 'Yahoo AppID: %s' % self.appid,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '%d' % len(query),
        }

        entry_point = 'http://jlp.yahooapis.jp/MAService/V1/parse'
        res, content = h.request(entry_point, 'POST', query, headers=headers)
        if res["status"] == '200':
            pass

    def translate_sentence2babigo(self, sentence):
        try:
            assert (isinstance(sentence, string_types))
            kana_sentence = self.get_kana_sentence(sentence)
            if kana_sentence:
                babi_sentence = self._insert_babi(kana_sentence)
                return babi_sentence
            else:
                return False
        except Exception as e:
            raise BabigoException(e)

    def get_kana_sentence(self, sentence):
        """ translate your sentence to babigo sentence
            optional feature
        Arguments:
        - `self`:
        - `sentence`: traslate target sentence
        """
        h = httplib2.Http(self.cache)
        sentence = dict(
            sentence=sentence.encode('utf-8'),
        )
        query = urlencode(sentence)
        headers = {
            'Host': 'jlp.yahooapis.jp',
            'User-Agent': 'Yahoo AppID: %s' % self.appid,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '%d' % len(query),
        }

        entry_point = 'http://jlp.yahooapis.jp/FuriganaService/V1/furigana'
        res, content = h.request(entry_point, 'POST', query, headers=headers)
        if res["status"] == '200':
            return self._concat_sentence(content)
        else:
            return False

    def _concat_sentence(self, content):
        """ concat sentence from web api

        Arguments:
        - `content`: Web API Response , format:XML
        """
        soup = BeautifulSoup(content, "xml")
        wlist = soup.find('WordList')  # WordList
        sentence = ''
        for word in wlist.findAll('Word'):
            if word.find('Furigana'):
                sentence += word.find('Furigana').getText()
            elif word.find('Surface'):
                sentence += word.find('Surface').getText()
        return sentence

    def _insert_babi(self, sentence):
        """ insert into  babigo into sentence

        Arguments:
        - `self`:
        - `sentence`:
        """
        assert (isinstance(sentence, string_types))
        kana = [
            u'あかさたなはまやらわがざだばぱ',
            u'いきしちにひみりぎじぢびぴ',
            u'うくすつぬふむゆるぐずづぶぷ',
            u'えけせてねへめれげげぜでべぺ',
            u'おこそとのほもよろをごぞどぼぽ',
            # んの扱いと濁音破裂音の扱いってどうなるの？
            # あと小文字の扱いは?
        ]
        mother_a = [x for x in kana[0]]
        mother_i = [x for x in kana[1]]
        mother_u = [x for x in kana[2]]
        mother_e = [x for x in kana[3]]
        mother_o = [x for x in kana[4]]
        result = u''
        for c in sentence:
            if c in mother_a:
                result += c + u'ば'
            elif c in mother_i:
                result += c + u'び'
            elif c in mother_u:
                result += c + u'ぶ'
            elif c in mother_e:
                result += c + u'べ'
            elif c in mother_o:
                result += c + u'ぼ'
            else:
                result += c
        return result
