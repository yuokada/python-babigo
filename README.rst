Overview
========
与えられた任意の文字列をバビ語に変換するパッケージです。
バビ語については以下を参照

::

    ア行→ば イ行→び ウ行→ぶ エ行→べ オ行→ボ をつければいいです
    例)おはようございます => おぼはばよぼうぶごぼざばいびまばすぶ

`バビ語の使い方-Yahoo!知恵袋 <http://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1455806259>`_

動作は、Python2.7 で確認しています。

Installation
============

::

    easy_install babigo

または

::

    pip install babigo

Usage
=====

事前にYahoo　デベロッパーネットワークでアプリケーションIDを取得します。

`Yahoo!デベロッパーネットワーク <http://developer.yahoo.co.jp/>`_

::

    import babigo
    babi = babigo.Babigo(appid='your-appid')
    sentence = u'庭には二羽ニワトリがいる。'
    print babi.translate_sentence2babigo(sentence) # にびわばにびはばにびわばにびわばとぼりびがばいびるぶ。

Changelog
=========

0.2.0 (2016-01-07)
------------------
- Require BeautifulSoup4

0.1.3 (2012-07-28)
------------------
- add unittest
- add Travis-CI setting

0.1.1 (2012-06-16)
------------------
- fix bug

0.1.0 (2012-06-16)
------------------
- First release


Travis
======

`Travis CI - Distributed build platform for the open source community <http://travis-ci.org/#!/yuokada/python-babigo>`_

.. image :: https://secure.travis-ci.org/yuokada/python-babigo.png?branch=master
