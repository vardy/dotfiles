# -*- coding:utf-8 -*-
#
# Copyright © 2016–2017 Liang Feng <finalion@gmail.com>
#
# Support: Report an issue at https://github.com/finalion/WordQuery/issues
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version; http://www.gnu.org/copyleft/gpl.html.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from anki.lang import currentLang

_style = u"""
<style>

* {
    font-family: 'Microsoft YaHei UI', Consolas, serif;
}

</style>

"""

trans = {
    'TOMATO COLOCK': {'zh_CN': u'番茄时钟', 'en': u'Tomato Clock'},
    'IGNORE REST': {'zh_CN': u'跳过休息', 'en': u'Continue'},
    'REST': {'zh_CN': u"休息", 'en': u'Break'},
    'IGNORE REST QUESTION': {'zh_CN': u"跳过休息吗？", 'en': u'Ignore break and continue?'},
    'ABORT TOMATO': {'zh_CN': u"中断番茄专注吗？", 'en': u'Abort Tomato Clock?'},
    'CANCEL': {'zh_CN': u"取消", 'en': u'Back'},
    'RETURN': {'zh_CN': u"返回", 'en': u'Return'},
    'MINUTES': {'zh_CN': u"分钟", 'en': u'5 Minutes'},
    'MIN': {'zh_CN': u"分钟", 'en': u'5 Minutes'},
    'MINS': {'zh_CN': u"分钟", 'en': u'5 Minutes'},
    'ENTER ONLY DIGITS': {'zh_CN': u"请只输入数字！", 'en': u'Only digits are acceptable!'},
    'SUPPORT DEVELOPMENT': {'zh_CN': u"掏出手机请框框喝咖啡吧！", 'en': u'Donate for Development'},
    'FOCUS MODE REMARK': {'zh_CN': _style + u"<center>专注模式</center>",
                          'en': _style + u'<center>Tomato Mode</center>'},
    'NORMAL MODE REMARK': {'zh_CN': _style + u"<center>普通模式</center>",
                           'en': _style + u'<center>Normal Mode</center>'},
    'QUICK MODE REMARK': {'zh_CN': _style + u"<center>训练模式</center>",
                          'en': _style + u'<center>Training Mode</center>'},
}


def _(key, lang=currentLang):
    key = key.upper().strip()
    if lang != 'zh_CN' and lang != 'en' and lang != 'fr':
        lang = 'en'  # fallback

    def disp(s):
        return s.lower().capitalize()

    if key not in trans or lang not in trans[key]:
        return disp(key)
    return trans[key][lang]


def _sl(key):
    return trans[key].values()
