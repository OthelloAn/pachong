import pytest
import demo

class Test_demo():
    def test_add(self):
        # Add = demo.Add()
        res=demo.Add().add_num(3,4)
        assert res == 7
