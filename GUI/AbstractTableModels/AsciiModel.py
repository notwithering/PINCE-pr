"""
Copyright (C) 2016-2017 Korcan Karaokçu <korcankaraokcu@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from PyQt6.QtCore import QVariant, Qt
from GUI.AbstractTableModels.HexModel import QHexModel

from libpince import utils, debugcore


class QAsciiModel(QHexModel):
    def __init__(self, row_count, column_count, parent=None):
        super().__init__(row_count, column_count, parent)

    def data(self, QModelIndex, int_role=None):
        if self.data_array and QModelIndex.isValid():
            index = QModelIndex.row() * self.column_count + QModelIndex.column()
            if int_role == Qt.ItemDataRole.BackgroundRole:
                address = self.current_address + index
                if utils.modulo_address(address, debugcore.inferior_arch) in self.breakpoint_list:
                    return QVariant(self.breakpoint_color)
                self.cell_change_color.setAlpha(20*self.cell_animation[index])
                return QVariant(self.cell_change_color)
            elif int_role == Qt.ItemDataRole.DisplayRole:
                return QVariant(utils.aob_to_str(self.data_array[index]))
        return QVariant()
