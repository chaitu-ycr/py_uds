from src.py_uds import PyUds


def test_importing():
    cls_instance = PyUds()
    assert cls_instance.say_hello()
