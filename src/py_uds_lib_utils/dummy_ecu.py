import can
from time import sleep as wait

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
        self.stop_receiving_message = False

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
    server = UdsServer()
    server.start()