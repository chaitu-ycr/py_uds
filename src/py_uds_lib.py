from py_uds_lib_utils.lib_variables import Sid, Sfid

class PyUdsLib:
    def __init__(self) -> None:
        self._diag_req = str
    
    @property
    def sid(self):
        return Sid()
    
    @property
    def sfid(self):
        return Sfid()

    def create_diag_request(self, request: str):
        print(f"request --> {request}")
        return request
