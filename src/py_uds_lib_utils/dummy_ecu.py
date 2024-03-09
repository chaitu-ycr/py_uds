import can
from time import sleep as wait
from py_uds_lib_utils.diag_services import Nrc, Sid, Sfid


class UdsServerExec:
    def __init__(self) -> None:
        self.__nrc = Nrc()
        self.__sid = Sid()
        self.__sfid = Sfid()
        self.__pos_res_adder = 0x40
        self.rx_req = list[int]
        self.tx_res = list[int]
        self.on = True
        self.off = False
        self.active_diagnostic_session = self.__sfid.DS
        self.ignition_key_status = self.off
        self.vehicle_running_status = self.off
        self.engine_running_status = self.off
        self.p2_server_max = [0x00, 0x32]
        self.p2start_server_max = [0x00, 0xC8]
        self.supported_diagnostic_sessions = [self.__sfid.DS, self.__sfid.PRGS, self.__sfid.EXTDS, self.__sfid.SSDS]

    def diagnostic_session_control(self):
        self.tx_res = [0, 0, 0, 0, 0, 0, 0, 0]
        if self.rx_req[2] in self.supported_diagnostic_sessions:
            if self.rx_req[0] == 0x02:
                if not self.ignition_key_status and not self.vehicle_running_status and not self.engine_running_status:
                    response = [self.rx_req[1] + self.__pos_res_adder, self.rx_req[2]] + self.p2_server_max + self.p2start_server_max
                    self.tx_res = [len(response)] + response
                else:
                    self.tx_res = [0x03, self.__sid.NR, self.__sid.DSC, self.__nrc.CNC]
            else:
                self.tx_res = [0x03, self.__sid.NR, self.__sid.DSC, self.__nrc.IMLOIF]
        else:
            self.tx_res = [0x03, self.__sid.NR, self.__sid.DSC, self.__nrc.SFNS]


class UdsServer:
    def __init__(self, bus_interface='kvaser', channel_name='0', bitrate=500000) -> None:
        self.tx_id = 0xFA
        self.rx_id = 0xFB
        self._tx_msg_data = [0, 0, 0, 0, 0, 0, 0, 0]
        self._rx_msg_data = list
        self._bus = can.interface.Bus(interface=bus_interface, channel=channel_name, bitrate=bitrate)
        self._tx_msg = can.Message(arbitration_id=self.tx_id, dlc=8, is_extended_id=False, data=self._tx_msg_data)
        self._rx_msg = can.Message
        self._return_from__receive_message_loop = False
        self.__server_exec = UdsServerExec()
        self.stop_receiving_message = False
        self._exec_service = {
            0x10: self.__server_exec.diagnostic_session_control
        }

    def _receive(self, timeout=0.1):
        while True:
            self._rx_msg = self._bus.recv(timeout)
            if self._rx_msg and self._rx_msg.arbitration_id == self.rx_id:
                break
            if self.stop_receiving_message:
                break

    def _send(self, timeout=0.1):
        try:
            self._bus.send(self._tx_msg, timeout)
            print(f"Message sent on {self._bus.channel_info}")
        except can.CanError:
            print("Message NOT sent")

    def _req_res(self):
        while not self.stop_receiving_message:
            self._receive()
            self._tx_msg_data = [0, 0, 0, 0, 0, 0, 0, 0]
            self._tx_msg_data = self._rx_msg.data
            self._tx_msg_data[1] = self._tx_msg_data[1] + 0x40
            self._tx_msg.data = self._tx_msg_data
            self._send()

    def _shutdown_bus(self):
        self._bus.shutdown()

    def start(self):
        self._req_res()

    def stop(self):
        self.stop_receiving_message = True
        wait(0.2)
        self._shutdown_bus()


class UdsClient:
    def __init__(self, bus_interface='kvaser', channel_name='1', bitrate=500000) -> None:
        self.tx_id = 0xFB
        self.rx_id = 0xFA
        self._tx_msg_data = [0, 0, 0, 0, 0, 0, 0, 0]
        self._rx_msg_data = list
        self._bus = can.interface.Bus(interface=bus_interface, channel=channel_name, bitrate=bitrate)
        self._tx_msg = can.Message(arbitration_id=self.tx_id, dlc=8, is_extended_id=False, data=self._tx_msg_data)

    def _send(self, msg: can.Message, timeout=5.0):
        try:
            self._bus.send(msg, timeout)
            print(f"Message sent on {self._bus.channel_info}")
        except can.CanError:
            print("Message NOT sent")

    def _shutdown_bus(self):
        self._bus.shutdown()

    def send_request(self, request_data: list, response_timeout = 3.0) -> list:
        final_req_data = [0 for _ in range(8)]
        for i in range(len(request_data)):
            final_req_data[i] = request_data[i]
        self._tx_msg.data = final_req_data
        self._send(self._tx_msg)

    def stop(self):
        self._shutdown_bus()


if __name__ == '__main__':
    # server = UdsServer()
    # server.start()
    exec = UdsServerExec()
    for i in range(10):
        exec.rx_req = [0x02, 0x10, i]
        exec.diagnostic_session_control()
        print(f'{[f"0x{i:02X}" for i in exec.tx_res]}')
    exec.ignition_key_status = True
    exec.rx_req = [0x02, 0x10, 0x01]
    exec.diagnostic_session_control()
    print(f'{[f"0x{i:02X}" for i in exec.tx_res]}')
