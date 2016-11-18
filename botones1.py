#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json


TOKEN = "299056405:AAFv7EfClfn1M0VBe-xfD1YwXf9G2pLTfr4"
chat_id = 212880702


msg = "some string"
BASE_URL = "https://api.telegram.org/bot{}/".format(TOKEN)

reply_markup = {'keyboard': [['1'],['2']], 'resize_keyboard': True, 'one_time_keyboard': True}
reply_markup = json.dumps(reply_markup)
params = urllib.urlencode({
      'chat_id': str(chat_id),
      'text': msg.encode('utf-8'),
      'reply_markup': reply_markup,
      'disable_web_page_preview': 'true',
      # 'reply_to_message_id': str(message_id),
})
resp = urllib2.urlopen(BASE_URL + 'sendMessage', params).read()
