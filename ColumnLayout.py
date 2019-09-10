#!/usr/env/python python3
# -*- coding: utf8 -*-
"""
@作者: 马聚川
@文件: ColumnLayout.py
@时间: 2019/8/31 16:15

This file is part of V3 project.
It is subject to the license terms in the LICENSE file found in the top-level directory
(c)2019 by GFD AUTOMATION TECHNOLOGY CO., LTD
"""
import logging

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QLayout, QToolButton, QToolBar, QWidgetItem

_INFO = logging.getLogger(__name__).info


class ColumnLayout(QLayout):
    def __init__(self, parent=None, toolBar=None, buttonSize=None):
        super(ColumnLayout, self).__init__(parent)
        self.setContentsMargins(2, 2, 2, 2)
        self.setProperty('toolBar', toolBar)
        self.setProperty('sHint', QSize())
        self.itemList = []
        self.setProperty("itemList", self.itemList)

    def removeAction(self, a):
        if self.itemList and isinstance(a, QToolButton):
            for i, item in enumerate(self.itemList):
                if a == item:
                    del self.itemList[i]
                    return

    def addItem(self, item_new):
        # itemList = self.property("ItemList")
        # if itemList is None or len(itemList) == 0:
        #     self.setProperty("ItemList", [item_new])
        #     return

        # so = ColumnLayout.getAccumulatedSortOrder(item_new, self.parent().objectName())
        # if so != 0:
        #     for i, item in enumerate(self.itemList):
        #         if not isinstance(item.property("SortOrder"), int) or not isinstance(item.property("SortOrder"), float):
        #             continue
        #         so2 = ColumnLayout.getAccumulatedSortOrder(item, self.parent().objectName())
        #         if so2 is None:
        #             continue
        #
        #         if so2 > so:
        #             # self.itemList.insert(so2, item_new)
        #             self.itemList.insert(i, item_new)
        #             return
        print("ColumnLayout.addItem : ", item_new.objectName())
        self.itemList.append(item_new)
        self.setProperty("ItemList", self.itemList)
        # print("ColumnLayout().addItem:", self.itemList)

    @staticmethod
    def getAccumulatedSortOrder(item, objectName):
        return ColumnLayout.getSortOrder(item, objectName) + ColumnLayout.getGroupSortOrder(item, objectName) * 100000

    @staticmethod
    def getSortOrder(item, objectName):
        n = "SortOrderOverride" + objectName
        if isinstance(item.property(n), int) or isinstance(item.property(n), float):
            return item.property(n)
        if isinstance(item.property("SortOrder"), int) or isinstance(item.property("SortOrder"), float):
            return item.property("SortOrder")
        return 0

    @staticmethod
    def getGroupSortOrder(item, objectName):
        n = "GroupSortOrderOverride" + objectName
        if isinstance(item.property(n), int) or isinstance(item.property(n), float):
            return item.property(n)
        if isinstance(item.property("GroupSortOrder"), int) or isinstance(item.property("GroupSortOrder"), float):
            return item.property("GroupSortOrder")
        return 0

    def minimumSize(self):
        return self.sizeHint()

    def sizeHint(self):
        # if not self.property("sHint"):
        #     print("=================== sizeHint ===================")
        #     return QSize(0, 0)
        # print("************** sizeHint **************")
        # self.setGeometry()
        return self.property("sHint")

    def setGeometry(self, rect=None):
        """
        s设置ToolBar的布局
        :rtype: object
        """
        dbg = False
        if self.parent().objectName() == "MainToolsPanel":
            dbg = True

        if not self.itemList:
            return

        columns = 2

        width = self.parentWidget().width()
        height = self.parentWidget().height()

        verticalWhenFloating = True
        # print('self.property("toolBar"): ', type(self.property("toolBar")))
        horizontal = self.property("toolBar").orientation() == Qt.Horizontal
        if self.property("toolBar").isFloating() and verticalWhenFloating:
            horizontal = False

        iconSize = 32

        if (self.property("sHintColumns") == columns and
                self.property("sHintWidth") == width and
                self.property("sHintHeight") == height and
                self.property("sHintVerticalWhenFloating") == verticalWhenFloating and
                self.property("sHintHorizontal") == horizontal and
                self.property("sHintIconSize") == iconSize):
            return self.property('sHint')

        w = 2 if horizontal else 0
        # w = 2
        h = 2 if not horizontal else 0
        # h = 2
        buttonSize = iconSize * 1.25
        c = 0
        groupOrder = -1

        for item in self.itemList:
            print("************** setGeometry **************", item.objectName())
            print("对象实例判断是否为QToolButton对象之前：", item.objectName())
            if isinstance(item, QToolButton):
                print("对象可以实例为QToolButton对象：", item.objectName())
                item.setIconSize(QSize(iconSize, iconSize))
            if item.defaultAction().isVisible() is False:
                item.setVisible(False)
                continue

            if item.objectName() == "BackButton":
                if horizontal:
                    item.setGeometry(0, 0, buttonSize * 0.75, height)
                    w += buttonSize * 0.75 + 8
                    h = 0

                else:
                    item.setGeometry(0, 0, width, buttonSize * 0.75)
                    h += buttonSize * 0.75 + 8
                    w = 0
                continue

            if horizontal:
                if h == 0:
                    w += 8
                else:
                    w += buttonSize + 8
                    h = 0
                    c = 0
            else:
                if w == 0:
                    h += 8
                else:
                    h += buttonSize + 8
                    w = 0
                    c = 0

            item.setGeometry(w, h, buttonSize, buttonSize)

            if horizontal:
                h += buttonSize
                c += 1
                if c >= columns:
                    h = 0
                    c = 0
                    w += buttonSize
            else:
                w += buttonSize
                c += 1
                if c >= columns:
                    w = 0
                    c = 0
                    h += buttonSize

        if horizontal:
            h += buttonSize
        else:
            w += buttonSize
        if horizontal:
            self.setProperty("sHint", QSize(w, buttonSize * columns))
        else:
            self.setProperty("sHint", QSize(buttonSize * columns, h))

        self.setProperty("sHintColumns", columns)
        self.setProperty("sHintWidth", width)
        self.setProperty("sHintHeight", height)
        self.setProperty("sHintVerticalWhenFloating", verticalWhenFloating)
        self.setProperty("sHintHorizontal", horizontal)
        self.setProperty("sHintIconSize", iconSize)

    def itemAt(self, index):
        if self.property("ItemList") is None or index >= len(self.itemList):
            return None
        return self.itemList[index]

    def count(self):
        return len(self.itemList)




