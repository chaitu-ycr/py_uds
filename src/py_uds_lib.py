from py_uds_lib_utils.diag_services import Services


class PyUdsLib:
    def __init__(self) -> None:
        self._diag_req = str

    @property
    def diag_services(self):
        return Services()

    def __prepare_diag_request(self, request: str):
        """prepares diagnostic request to suite interface.
        diagnostic request received is string of bytes.

        TODO: lot to do here. incomplete implementation.
        """
        print(f"request --> {request}")
        return request

    def send_diag_request(self, request: str):
        """send diagnostic request and wait for response.

        TODO: lot to do here. incomplete implementation.
        """
        response = self.__prepare_diag_request(request)
        return response
