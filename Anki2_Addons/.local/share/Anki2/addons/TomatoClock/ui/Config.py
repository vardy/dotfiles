import re
from functools import partial

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QDialog, QTableWidgetItem

from ._Config import Ui_dlg_config
from ..lib.config import UserConfig


class ConfigDialog(QDialog, Ui_dlg_config):
    def __init__(self, parent):
        super(ConfigDialog, self).__init__(parent)
        self.setupUi(self)

        self.load_config_value()
        self.bind_slots()
        self.adjust_ui()

    def adjust_ui(self):

        break_min_dicts = UserConfig.BREAK_MINUTES
        sorted_keys = sorted(break_min_dicts.keys())[:7]
        minites_ints = [int(re.findall("\d+", s)[0]) for s in sorted_keys]

        rc = self.tableWidget.rowCount()
        cc = self.tableWidget.columnCount()
        for c in range(cc):
            for r in range(rc):
                item = self.tableWidget.itemAt(r, c)
                assert isinstance(item, QTableWidgetItem)

    def table_cell_changed(self, r, c):
        item = self.tableWidget.item(r, c)
        assert isinstance(item, QTableWidgetItem)

        text = item.text()
        if text.strip() and not re.match("^\d+$", text):
            from aqt.utils import showWarning
            from ..lib.lang import _ as trans
            showWarning(trans("ENTER ONLY DIGITS"))
            return

        rc = self.tableWidget.rowCount()
        cc = self.tableWidget.columnCount()
        _dict = {}

        for r in range(rc):
            min_item = self.tableWidget.item(r, 0)
            break_item = self.tableWidget.item(r, 1)
            assert isinstance(item, QTableWidgetItem)
            assert isinstance(item, QTableWidgetItem)

            min_txt = min_item.text()
            break_min_txt = break_item.text()
            if not all([min_txt, break_min_txt]):
                continue

            _dict["{}MIN".format(min_item.text())] = int(min_item.text())
        else:
            UserConfig.BREAK_MINUTES = _dict

    def load_config_value(self):
        # checks
        self.check_answer_timeout.setChecked(UserConfig.SHOW_ANSWER_ON_CARD_TIMEOUT)
        self.check_overall.setChecked(UserConfig.SHOW_OVERALL_STATISTICS)
        self.check_deck.setChecked(UserConfig.SHOW_DECK_STATISTICS)

        self.check_start.setChecked(UserConfig.PLAY_SOUNDS['start'])
        self.check_break.setChecked(UserConfig.PLAY_SOUNDS['break'])
        self.check_almost_timeout.setChecked(UserConfig.PLAY_SOUNDS['half_way_limit'])
        self.check_timeout.setChecked(UserConfig.PLAY_SOUNDS['timeout'])
        self.check_abort.setChecked(UserConfig.PLAY_SOUNDS['abort'])

        # value
        self.spin_card_secs.setValue(UserConfig.ANSWER_TIMEOUT_SECONDS)

        # minutes
        break_min_dicts = UserConfig.BREAK_MINUTES
        sorted_keys = sorted(break_min_dicts.keys())[:7]
        minites_ints = [int(re.findall("\d+", s)[0]) for s in sorted_keys]

        for c in range(UserConfig.BREAK_MINUTES.items()[0].__len__()):
            for r in range(sorted_keys.__len__()):
                if c:
                    item = QTableWidgetItem(str(break_min_dicts[sorted_keys[r]]))
                else:
                    item = QTableWidgetItem(str(minites_ints[r]))
                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(r, c, item)

    def _set_playsounds_property(self, sound_name, val):
        _play_sounds_dict = UserConfig.PLAY_SOUNDS
        _play_sounds_dict[sound_name] = val
        UserConfig.PLAY_SOUNDS = _play_sounds_dict

    def bind_slots(self):
        checks = [self.check_answer_timeout, self.check_overall, self.check_deck,
                  self.check_start, self.check_break, self.check_almost_timeout,
                  self.check_timeout, self.check_abort,
                  ]

        toggle_func = [
            lambda val: setattr(UserConfig, "SHOW_ANSWER_ON_CARD_TIMEOUT", val),
            lambda val: setattr(UserConfig, "SHOW_OVERALL_STATISTICS", val),
            lambda val: setattr(UserConfig, "SHOW_DECK_STATISTICS", val),

            lambda val: self._set_playsounds_property("start", val),
            lambda val: self._set_playsounds_property("break", val),
            lambda val: self._set_playsounds_property("half_way_limit", val),
            lambda val: self._set_playsounds_property("timeout", val),
            lambda val: self._set_playsounds_property("abort", val),
        ]

        for ctrl, func in zip(checks, toggle_func):
            ctrl.toggled.connect(func)

        self.tableWidget.cellChanged.connect(self.table_cell_changed)
