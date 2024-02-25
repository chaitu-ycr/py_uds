from py_uds_lib_utils.diag_services import Services


class PyUdsLib:
    def __init__(self) -> None:
        self._diag_req = str
    
    @property
    def diag_services(self):
        return Services()

    def prepare_diag_request(self, request: str):
        """
            TODO: lot to do here. incomplete implementation.
        """
        print(f"request --> {request}")
        return request
    
    def send_diag_request(self, request: str):
        """
            TODO: lot to do here. incomplete implementation.
        """
        response = self.prepare_diag_request(request)
        return response
