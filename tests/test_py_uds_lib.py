from time import sleep as wait
from src.py_uds_lib import PyUdsLib
from src.py_uds_lib_utils.dummy_ecu import ClientEcu

uds_inst = PyUdsLib()
uds_services = uds_inst.diag_services

def test_importing():
    req = uds_services.diagnostic_session_control(uds_services.sfid.default_session)
    uds_inst.send_diag_request(req)

    req = uds_services.ecu_reset(uds_services.sfid.soft_reset)
    uds_inst.send_diag_request(req)

    req = uds_services.security_access(uds_services.sfid.request_seed)
    uds_inst.send_diag_request(req)
    req = uds_services.security_access(uds_services.sfid.send_key, (0x20, 0x30))
    uds_inst.send_diag_request(req)

def test_dummy_ecu():
    client = ClientEcu()
    for _ in range(5):
        client.send_diagnostic_request([0x02, 0x10, 0x01, 0, 0, 0, 0, 0])
        client.send_diagnostic_request([0x02, 0x11, 0x00, 0, 0, 0, 0, 0])
        client.send_diagnostic_request([0x02, 0x3E, 0x00, 0, 0, 0, 0, 0])
        wait(1)
    client.stop()