Overview
========
与えられた任意の文字列をバビ語に変換するパッケージです。
バビ語については以下を参照

    ア行→ば イ行→び ウ行→ぶ エ行→べ オ行→ボ をつければいいです
    例)おはようございます→おぼはばよぼうぶごぼざばいびまばすぶ

`バビ語の使い方-Yahoo!知恵袋 <http://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1455806259>`_

動作は、Python2.7 で確認しています。

Installation
============

下のどちらのほうほうでもインストールできます

    easy_install babigo

または

    pip install babigo

Usage
=====

事前にYahooJapan　デベロッパーネットワークでアプリケーションIDを取得します。
`Yahoo!デベロッパーネットワーク <http://developer.yahoo.co.jp/>`_

    import babigo
    babigo = babigo.Babigo(appid='your-appid')
    sentence = u'庭には二羽ニワトリがいる。'
    print babigo.translate_sentence2babigo(sentence) # にびわばにびはばにびわばにびわばとぼりびがばいびるぶ。

Changelog
=========

0.1.0 (2012-06-16)
----------------
- First release
