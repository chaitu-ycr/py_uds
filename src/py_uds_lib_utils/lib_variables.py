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
        