# -*- coding=utf-8 -*-
import pytest


class TestDemo:

    # 1 单个属性参数化
    # 2 多个属性参数化
    def test_f1(self):
        print("1成功")
        assert True

    def test_f2(self):
        print("2成功")
        assert True

    def test_f3(self):
        print("3失败")
        assert False

    def test_f4(self):
        print("4成功")
        assert True
