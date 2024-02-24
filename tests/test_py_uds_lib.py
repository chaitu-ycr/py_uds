from src.py_uds_lib import PyUdsLib


def test_importing():
    default_session_req = '10 01'
    cls_instance = PyUdsLib()
    assert cls_instance.create_diag_request(default_session_req) == default_session_req
