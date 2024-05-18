from py_uds_lib import Services

uds_services = Services()

def test_uds_services():
    return_value = uds_services.diagnostic_session_control(diagnostic_session_type=uds_services.sfid.extended_session)
    assert return_value == '10 03'
