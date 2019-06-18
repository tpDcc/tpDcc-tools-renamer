#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Widget that manages replace functionality for tpRenamer
"""

from __future__ import print_function, division, absolute_import


from tpQtLib.Qt.QtCore import *
from tpQtLib.Qt.QtWidgets import *
from tpQtLib.Qt.QtGui import *

from tpQtLib.core import base
from tpQtLib.widgets import splitters, expandables


class ReplacerWidget(base.BaseWidget, object):

    replaceUpdate = Signal()

    def __init__(self, parent=None):
        super(ReplacerWidget, self).__init__(parent=parent)

    def ui(self):
        super(ReplacerWidget, self).ui()

        self.main_layout.addWidget(splitters.Splitter('REPLACE'))

        replace_layout = QHBoxLayout()
        replace_layout.setAlignment(Qt.AlignLeft)
        replace_layout.setContentsMargins(0, 0, 0, 0)
        replace_layout.setSpacing(2)
        self.main_layout.addLayout(replace_layout)

        self._find_replace_cbx = QCheckBox()
        replace_layout.addWidget(self._find_replace_cbx)
        replace_layout.addWidget(splitters.get_horizontal_separator_widget())

        self._replace_lbl = QLabel('Find: ')
        self._replace_line = QLineEdit()
        self._with_lbl = QLabel('Replace: ')
        self._with_line = QLineEdit()
        # replace_lbl.setFixedWidth(55)
        # with_lbl.setFixedWidth(55)
        reg_ex = QRegExp("[a-zA-Z_0-9]+")
        text_validator = QRegExpValidator(reg_ex, self._replace_line)
        self._replace_line.setValidator(text_validator)
        self._with_line.setValidator(text_validator)

        replace_layout.addWidget(self._replace_lbl)
        replace_layout.addWidget(self._replace_line)
        replace_layout.addItem(QSpacerItem(10, 0, QSizePolicy.Fixed, QSizePolicy.Preferred))
        replace_layout.addWidget(self._with_lbl)
        replace_layout.addWidget(self._with_line)

        self._replace_lbl.setEnabled(False)
        self._replace_line.setEnabled(False)
        self._with_lbl.setEnabled(False)
        self._with_line.setEnabled(False)

    def setup_signals(self):
        self._find_replace_cbx.toggled.connect(self._on_find_replace_toggled)
        self._replace_line.textChanged.connect(self._on_replace_line_text_changed)
        self._with_line.textChanged.connect(self._on_with_line_text_changed)

    def get_replace_settings(self):
        """
        Internal function that returns current rename settings
        :return: str, str
        """

        if self._find_replace_cbx.isChecked():
            find_str = self._replace_line.text()
            replace_str = self._with_line.text()
        else:
            find_str = ''
            replace_str = ''

        return find_str, replace_str

    def _on_find_replace_toggled(self, flag):

        self._replace_lbl.setEnabled(flag)
        self._replace_line.setEnabled(flag)
        self._with_lbl.setEnabled(flag)
        self._with_line.setEnabled(flag)
        self.replaceUpdate.emit()

    def _on_replace_line_text_changed(self, new_text):
        self.replaceUpdate.emit()

    def _on_with_line_text_changed(self, new_text):
        self.replaceUpdate.emit()