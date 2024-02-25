class Sid:
    def __init__(self) -> None:
        # Diagnostic and communication management
        self.diagnostic_session_control = 0x10
        self.DSC = 0x10
        self.ecu_reset = 0x11
        self.ER = 0x11
        self.security_access = 0x27
        self.SA = 0x27
        self.communication_control = 0X28
        self.CC = 0X28
        self.tester_present = 0x3E
        self.TP = 0x3E
        self.access_timing_parameter = 0x83
        self.ATP = 0x83
        self.secured_data_transmission = 0x84
        self.SDT = 0x84
        self.control_dtc_setting = 0x85
        self.CDTCS = 0x85
        self.response_on_event = 0x86
        self.ROE = 0x86
        self.link_control = 0x87
        self.LC = 0x87
        # Data transmission
        self.read_data_by_identifier = 0x22
        self.RDBI = 0x22
        self.read_memory_by_address = 0x23
        self.RMBA = 0x23
        self.read_scaling_data_by_identifier = 0x24
        self.RSDBI = 0x24
        self.read_data_by_periodic_identifier = 0x2A
        self.RDBPI = 0x2A
        self.dynamically_define_data_identifier = 0x2C
        self.DDDI = 0x2C
        self.write_data_by_identifier = 0x2E
        self.WDBI = 0x2E
        self.write_memory_by_address = 0x3D
        self.WMBA = 0x3D
        # Stored data transmission
        self.clear_diagnostic_information = 0x14
        self.CDTCI = 0x14
        self.read_dtc_information = 0x19
        self.RDTCI = 0x19
        # Input Output control
        self.input_output_control_by_identifier = 0x2F
        self.IOCBI = 0x2F
        # Remote activation of routine
        self.routine_control = 0x31
        self.RC = 0x31
        # Upload download
        self.request_download = 0x34
        self.RD = 0x34
        self.request_upload = 0x35
        self.RU = 0x35
        self.transfer_data = 0x36
        self.TD = 0x36
        self.request_transfer_exit = 0x37
        self.RTE = 0x37
        self.request_file_transfer = 0x38
        self.RFT = 0x38


class Sfid:
    def __init__(self) -> None:
        # diagnostic_session_control
        self.default_session = 0x01
        self.DS = 0x01
        self.programming_session = 0x02
        self.PRGS = 0x02
        self.extended_session = 0x03
        self.EXTDS = 0x03
        self.safety_system_diagnostic_session = 0x04
        self.SSDS = 0x04
        # ecu_reset
        self.hard_reset = 0x01
        self.HR = 0x01
        self.key_on_off_reset = 0x02
        self.KOFFONR = 0x02
        self.soft_reset = 0x03
        self.SR = 0x03
        self.enable_rapid_power_shutdown = 0x04
        self.ERPSD = 0x04
        self.disable_rapid_power_shutdown = 0x05
        self.DRPSD = 0x05
        # security_access
        self.request_seed = 0x01
        self.RSD = 0x01
        self.send_key = 0x02
        self.SK = 0x02
        # communication_control
        self.enable_rx_and_tx = 0x00
        self.ERXTX = 0x00
        self.enable_rx_and_disable_tx = 0x01
        self.ERXDTX = 0x01
        self.disable_rx_and_enable_tx = 0x02
        self.DRXETX = 0x02
        self.disable_rx_and_tx = 0x03
        self.DRXTX = 0x03
        self.enable_rx_and_disable_tx_with_enhanced_address_information = 0x04
        self.ERXDTXWEAI = 0x04
        self.enable_rx_and_tx_with_enhanced_address_information = 0x05
        self.ERXTXWEAI = 0x05
        # tester_present
        self.zero_sub_function = 0x00
        self.ZSUBF = 0x00
        # access_timing_parameter
        self.read_extended_timing_parameter_set = 0x01
        self.RETPS = 0x01
        self.set_timing_parameters_to_default_value = 0x02
        self.STPTDV = 0x02
        self.read_currently_active_timing_parameters = 0x03
        self.RCATP = 0x03
        self.set_timing_parameters_to_given_values = 0x04
        self.STPTGV = 0x04
        # control_dtc_setting
        self.on = 0x01
        self.ON = 0x01
        self.off = 0x02
        self.OFF = 0x02
        # response_on_event
        self.do_not_store_event = 0x00
        self.DNSE = 0x00
        self.store_event = 0x01
        self.SE = 0x01
        self.stop_response_on_event = 0x00
        self.STPROE = 0x00
        self.on_dtc_status_change = 0x01
        self.ONDTCS = 0x01
        self.on_timer_interrupt = 0x02
        self.OTI = 0x02
        self.on_change_of_data_identifier = 0x03
        self.OCODID = 0x03
        self.report_activated_events = 0x04
        self.RAE = 0x04
        self.start_response_on_event = 0x05
        self.STRTROE = 0x05
        self.clear_response_on_event = 0x06
        self.CLRROE = 0x06
        self.on_comparison_of_value = 0x07
        self.OCOV = 0x07
        # link_control
        self.verify_mode_transition_with_fixed_parameter = 0x01
        self.VMTWFP = 0x01
        self.verify_mode_transition_with_specific_parameter = 0x02
        self.VMTWSP = 0x02
        self.transition_mode = 0x03
        self.TM = 0x03
        # dynamically_define_data_identifier
        self.define_by_identifier = 0x01
        self.DBID = 0x01
        self.define_by_memory_address = 0x02
        self.DBMA = 0x02
        self.clear_dynamically_defined_data_identifier = 0x03
        self.CDDDID = 0x03
        # read_dtc_information
        self.report_number_of_dtc_by_status_mask = 0x01
        self.RNODTCBSM = 0x01
        self.report_dtc_by_status_mask = 0x02
        self.RDTCBSM = 0x02
        self.report_dtc_snapshot_identification = 0x03
        self.RDTCSSI = 0x03
        self.report_dtc_snapshot_record_by_dtc_number = 0x04
        self.RDTCSSBDTC = 0x04
        self.read_dtc_stored_data_by_record_number = 0x05
        self.RDTCSDBRN = 0x05
        self.report_dtc_ext_data_record_by_dtc_number = 0x06
        self.RDTCEDRBDN = 0x06
        self.report_number_of_dtc_by_severity_mask_record = 0x07
        self.RNODTCBSMR = 0x07
        self.report_dtc_by_severity_mask_record = 0x08
        self.RDTCBSMR = 0x08
        self.report_severity_information_of_dtc = 0x09
        self.RSIODTC = 0x09
        self.report_mirror_memory_dtc_ext_data_record_by_dtc_number = 0x10
        self.RMDEDRBDN = 0x10
        self.report_supported_dtc = 0x0A
        self.RSUPDTC = 0x0A
        self.report_first_test_failed_dtc = 0x0B
        self.RFTFDTC = 0x0B
        self.report_first_confirmed_dtc = 0x0C
        self.RFCDTC = 0x0C
        self.report_most_recent_test_failed_dtc = 0x0D
        self.RMRTFDTC = 0x0D
        self.report_most_recent_confirmed_dtc = 0x0E
        self.RMRCDTC = 0x0E
        self.report_mirror_memory_dtc_by_status_mask = 0x0F
        self.RMMDTCBSM = 0x0F
        self.report_number_of_mirror_memory_dtc_by_status_mask = 0x11
        self.RNOMMDTCBSM = 0x11
        self.report_number_of_emission_obd_dtc_by_status_mask = 0x12
        self.RNOOEBDDTCBSM = 0x12
        self.report_emission_obd_dtc_by_status_mask = 0x13
        self.ROBDDTCBSM = 0x13
        self.report_dtc_fault_detection_counter = 0x14
        self.RDTCFDC = 0x14
        self.report_dtc_with_permanent_status = 0x15
        self.RDTCWPS = 0x15
        self.report_dtc_ext_data_record_by_record_number = 0x16
        self.RDTCEDRBR = 0x16
        self.report_user_def_memory_dtc_by_status_mask = 0x17
        self.RUDMDTCBSM = 0x17
        self.report_user_def_memory_dtc_snapshot_record_by_dtc_number = 0x18
        self.RUDMDTCSSBDTC = 0x18
        self.report_user_def_memory_dtc_ext_data_record_by_dtc_number = 0x19
        self.RUDMDTCEDRBDN = 0x19
        self.report_wwh_obd_dtc_by_mask_record = 0x42
        self.ROBDDTCBMR = 0x42
        self.report_wwh_obd_dtc_with_permanent_status = 0x55
        self.RWWHOBDDTCWPS = 0x55
        self.start_routine = 0x01
        self.STR = 0x01
        self.stop_routine = 0x02
        self.STPR = 0x02
        self.request_routine_result = 0x03
        self.RRR = 0x03


class Services:
    def __init__(self) -> None:
        pass

    @property
    def sid(self):
        return Sid()

    @property
    def sfid(self):
        return Sfid()

    # Diagnostic and communication management
    def diagnostic_session_control(self, diagnostic_session_type: int) -> str:
        """service is used to enable different diagnostic sessions in the server(s).
        Check ISO 14229 doc for more information about service.

        Args:
            diagnostic_session_type (int): 1 byte parameter is used by the service to select the specific behavior of the server

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.DSC:02X} {diagnostic_session_type:02X}'
        return request

    def ecu_reset(self, reset_type: int) -> str:
        """The ECUReset service is used by the client to request a server reset.
        Check ISO 14229 doc for more information about service.

        Args:
            reset_type (int): 1 byte parameter is used by the service to describe how the server has to perform the reset.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.ER:02X} {reset_type:02X}'
        return request

    def security_access(self, security_access_type: int, security_access_data_record: None | list[int] = None) -> str:
        """this service provide a means to access data and/or diagnostic services, which have restricted access for security, emissions, or safety reasons.
        Check ISO 14229 doc for more information about service.

        Args:
            security_access_type (int): 1 byte parameter indicates to the server the step in progress for this service, the level of security the client wants to access.
            security_access_data_record (None | list[int], optional): parameter is user optional to transmit data to a server when requesting the seed information. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.SA:02X} {security_access_type & 0xFF:02X}'
        if security_access_data_record is not None:
            request = f'{request} {" ".join([f"{value & 0xFF:02x}" for value in security_access_data_record])}'
        return request

    def communication_control(self, control_type: int, communication_type: int, node_identification_number: None | int = None) -> str:
        """service used to switch on/off the transmission and/or the reception of certain messages.
        Check ISO 14229 doc for more information about service.

        Args:
            control_type (int): 1 byte parameter contains information on how the server shall modify the communication type.
            communication_type (int): 1 byte parameter is used to reference the kind of communication to be controlled.
            node_identification_number (None | int, optional): 2 byte parameter is used to identify a node on a sub-network somewhere in the vehicle. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.CC:02X} {control_type & 0xFF:02X} {communication_type & 0xFF:02X}'
        if node_identification_number is not None:
            request = f'{request} {(node_identification_number & 0xFF00) > 8:02X} {node_identification_number & 0xFF}'
        return request

    def tester_present(self, zero_sub_functions: int) -> str:
        """This service is used to indicate to a server (or servers) that a client is still connected to the vehicle and that
        certain diagnostic services and/or communication that have been previously activated are to remain active.
        Check ISO 14229 doc for more information about service.

        Args:
            zero_sub_functions (int): 1 byte parameter is used to indicate that no sub-function beside the suppressPosRspMsgIndicationBit is supported by this service.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.TP:02X} {zero_sub_functions & 0xFF:02X}'
        return request

    def access_timing_parameter(self, timing_parameter_access_type: int, timing_parameter_request_record: None | list[int] = None) -> str:
        """service is used to read and change the default timing parameters of a communication link for the duration this communication link is active.
        Check ISO 14229 doc for more information about service.

        Args:
            timing_parameter_access_type (int): 1 byte parameter is used by the service to select the specific behavior of the server.
            timing_parameter_request_record (None | list[int], optional): parameter record contains the timing parameter values to be set in the server. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.ATP:02X} {timing_parameter_access_type & 0xFF:02X}'
        if timing_parameter_request_record is not None:
            request = f'{request} {" ".join([f"{value & 0xFF:02x}" for value in timing_parameter_request_record])}'
        return request

    def secured_data_transmission(self, security_data_request_record: list[int]) -> str:
        """service to transmit data that is protected against attacks from third parties - which could endanger data security.
        Check ISO 14229 doc for more information about service.

        Args:
            security_data_request_record (list[int]): parameter contains the data as processed by the Security Sub-Layer.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.SDT:02X} {" ".join([f"{value & 0xFF:02x}" for value in security_data_request_record])}'
        return request

    def control_dtc_setting(self, dtc_setting_type: int, dtc_setting_control_option_record: None | list[int] = None) -> str:
        """service used by a client to stop or resume the updating of DTC status bits in the server.
        Check ISO 14229 doc for more information about service.

        Args:
            dtc_setting_type (int): 1 byte parameter used by the service to indicate to the server(s) whether diagnostic trouble code status bit updating shall stop or start again.
            dtc_setting_control_option_record (None | list[int], optional): parameter record is user optional to transmit data to a server when controlling the updating of DTC status bits. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.CDTCS:02X} {dtc_setting_type & 0xFF:02X}'
        if dtc_setting_control_option_record is not None:
            request = f'{request} {" ".join([f"{value & 0xFF:02x}" for value in dtc_setting_control_option_record])}'
        return request

    def response_on_event(self, event_type: int, event_window_time: int, event_type_record: None | list[int] = None, service_to_respond_to_record: None | list[int] = None) -> str:
        """service requests a server to start or stop transmission of responses on a specified event.
        Check ISO 14229 doc for more information about service.

        Args:
            event_type (int): 1 byte parameter is used by the service to specify the event to be configured in the server and to control the service set up.
            event_window_time (int): 1 byte parameter is used to specify a window for the event logic to be active in the server.
            event_type_record (None | list[int], optional): parameter record contains additional parameters for the specified eventType. Defaults to None.
            service_to_respond_to_record (None | list[int], optional): parameter record contains the service parameters of the service to be executed in the server each time the specified event defined in the eventTypeRecord occurs. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.ROE:02X} {event_type & 0xFF:02X} {event_window_time & 0xFF:02X}'
        if event_type_record is not None:
            request = f'{request} {" ".join([f"{value & 0xFF:02x}" for value in event_type_record])}'
        if service_to_respond_to_record is not None:
            request = f'{request} {" ".join([f"{value & 0xFF:02x}" for value in service_to_respond_to_record])}'
        return request

    def link_control(self, link_control_type: int, link_control_mode_identifier: int | None = None, link_record: int | None = None) -> str:
        """service is used to control the communication between the client and the server in order to gain bus bandwidth for diagnostic purposes.
        Check ISO 14229 doc for more information about service.

        Args:
            link_control_type (int): 1 byte parameter is used by the service to describe the action to be performed in the server.
            link_control_mode_identifier (int | None, optional): This conditional 1 byte parameter references a fixed defined mode parameter. Defaults to None.
            link_record (int | None, optional): This conditional 3 byte parameter record contains a specific mode parameter in case the sub-function parameter indicates that a specific parameter is used. Defaults to None.

        Returns:
            str: _description_
        """
        request = f'{self.sid.LC:02X} {link_control_type & 0xFF:02X}'
        if link_control_mode_identifier is not None:
            request = f'{request} {link_control_mode_identifier}'
        if link_record is not None:
            request = f'{request} {(link_record & 0xFF0000) > 16:02X} {(link_record & 0xFF0000) > 8:02X} {link_record & 0xFF}'
        return request

    # Data transmission
    # Stored data transmission
    # Input Output control
    # Remote activation of routine
    # Upload download
