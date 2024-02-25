from src.py_uds_lib import PyUdsLib

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
