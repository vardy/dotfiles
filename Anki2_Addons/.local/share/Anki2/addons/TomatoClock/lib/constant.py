# -*- coding: utf-8 -*-
# Created: 3/9/2018
# Project : TomatoClock
from anki.lang import currentLang

ADDON_CD = 1608644302
HAS_SET_UP = False
DEBUG = False
MIN_SECS = 1 if DEBUG else 60
__version__ = "0.3.02"
STATISTICS_PY = "https://raw.githubusercontent.com/upday7/TomatoClock/master/TomatoClock/lib/tomatostats.py"
REST_MINS = 5

UPDATE_LOGS = (
    (
        "0.1.5", u"""
        <ol>
            <li>新增： 静音选项，详细见设置 > PlaySounds</li>
            <li>新增： 插件投票选项（窗口右上角） </li>
            <li>修复： 若干BUG</li>
            </ol>
        """ if currentLang == 'zh_CN' else """
        <ol>
            <li>Added: Mute for sounds, see in settings > PlaySounds </li>
            <li>Added: "Vote for Addon" button, at the top right corner of window </li>
            <li>Fixed: several bugs</li>
            </ol>"""
    ),
    (
        "0.1.6", u"""
        <ol>
            <li>新增： 番茄图表! (在设置中可以关闭)</li>
            </ol>
        """ if currentLang == 'zh_CN' else """
        <ol>
            <li>Added: Statics! (Switch off in settings) </li>
            </ol>"""
    ),
    (
        "0.1.7", u"""
        <ol>
            <li>修复： 番茄图表若干BUG</li>
            <li>新增： 动态加载代码（设置里关闭）</li>
            </ol>
        """ if currentLang == 'zh_CN' else """
        <ol>
            <li>Fixed: Reports bugs </li>
            <li>Added: Dynamically loading codes from github(Switch off in settings) </li>
            </ol>"""
    ),
    (
        "0.2.0", u"""
        <ol>
            <li>新增： 图表时间范围（设置里调节： report_recent_days）</li>
            </ol>
        """ if currentLang == 'zh_CN' else """
        <ol>
            <li>Added: Days range for statistics (Switch off in settings: report_recent_days) </li>
            </ol>"""
    ),

    (
        "0.2.1", u"""
        <ol>
            <li>新增：番茄数据总揽</li>
            <li>修复：一些BUG</li>
            </ol>
        """ if currentLang == 'zh_CN' else """
        <ol>
            <li>Added: Summary statistics </li>
            <li>Fixed: Some bugs </li>
            </ol>"""
    ),
    (
        "0.2.2", u"""
        <ol>
            <li>新增：番茄数据总揽（全部牌组, 关闭数据显示在设置里。）</li>
            </ol>
        """ if currentLang == 'zh_CN' else """
        <ol>
            <li>Added: Summary statistics for all decks, switch off statistic in settings </li>
        </ol>"""
    ), (
        "0.2.3", u"""
        <ol>
            <li>新增：全新番茄时钟图表。</li>
            </ol>
        """ if currentLang == 'zh_CN' else """
        <ol>
            <li>Added: Nwe Charts.</li>
        </ol>"""
    ),
    (
        "0.2.31", u"""
        <ol>
            <li>修复：修复与WebQuery冲突的问题。</li>
            </ol>
        """ if currentLang == 'zh_CN' else """
        <ol>
            <li>Fixed: Crashing Anki when WebQuery is installed.</li>
        </ol>"""
    ), (
        "0.2.34", u"""
        <ol>
            <li>修复：BUG FIXES。</li>
            </ol>
        """ if currentLang == 'zh_CN' else """
        <ol>
            <li>Fixed: Some Bugs</li>
        </ol>"""
    ), (
        "0.2.35", u"""
        <ol>
            <li>修复：BUG FIXES。</li>
            </ol>
        """ if currentLang == 'zh_CN' else """
        <ol>
            <li>Fixed: Some Bugs</li>
        </ol>"""
    ),
    (
        "0.3.01", u"""
        <ol>
            <li>新增：现在可以同时使用正常的Anki模式了，番茄模式请选择“番茄时钟”按钮。</li>
            <li>新增：全新的设置界面，现在您可以配置自己的番茄时间了。</li>
            </ol>
        """ if currentLang == 'zh_CN' else """
        <ol>
            <li>Added: You can now use the normal Anki mode for study, trigger "Tomato Clock" only when you want it.</li>
            <li>Added: Configuration interface, you can now add your preferred tomato minutes and break minutes.</li>
        </ol>"""
    )

)
