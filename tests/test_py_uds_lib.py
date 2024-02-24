from src.py_uds_lib import PyUdsLib


def test_importing():
    cls_instance = PyUdsLib()
    assert cls_instance.say_hello()
