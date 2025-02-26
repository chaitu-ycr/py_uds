"""Python package for creating UDS requests"""

# Import Python Libraries here
from typing import Union


class Services:
    """This class holds all UDS services. Use class methods to create diagnostic request in string format.
    """
    def __init__(self) -> None:
        pass

    @property
    def sid(self):
        return Sid()

    @property
    def sfid(self):
        return Sfid()
    
    @property
    def nrc(self):
        return Nrc()

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

    def security_access(self, security_access_type: int, security_access_data_record: list[int] = None) -> str:
        """this service provide a means to access data and/or diagnostic services, which have restricted access for security, emissions, or safety reasons.
        Check ISO 14229 doc for more information about service.

        Args:
            security_access_type (int): 1 byte parameter indicates to the server the step in progress for this service, the level of security the client wants to access.
            security_access_data_record (list[int], optional): parameter is user optional to transmit data to a server when requesting the seed information. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.SA:02X} {security_access_type & 0xFF:02X}'
        if security_access_data_record is not None:
            request = f'{request} {" ".join([f"{value & 0xFF:02X}" for value in security_access_data_record])}'
        return request

    def communication_control(self, control_type: int, communication_type: int, node_identification_number: int = None) -> str:
        """service used to switch on/off the transmission and/or the reception of certain messages.
        Check ISO 14229 doc for more information about service.

        Args:
            control_type (int): 1 byte parameter contains information on how the server shall modify the communication type.
            communication_type (int): 1 byte parameter is used to reference the kind of communication to be controlled.
            node_identification_number (int, optional): 2 byte parameter is used to identify a node on a sub-network somewhere in the vehicle. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.CC:02X} {control_type & 0xFF:02X} {communication_type & 0xFF:02X}'
        if node_identification_number is not None:
            request = f'{request} {(node_identification_number & 0xFF00) >> 8:02X} {node_identification_number & 0xFF}'
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

    def access_timing_parameter(self, timing_parameter_access_type: int, timing_parameter_request_record: list[int] = None) -> str:
        """service is used to read and change the default timing parameters of a communication link for the duration this communication link is active.
        Check ISO 14229 doc for more information about service.

        Args:
            timing_parameter_access_type (int): 1 byte parameter is used by the service to select the specific behavior of the server.
            timing_parameter_request_record (Nlist[int], optional): parameter record contains the timing parameter values to be set in the server. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.ATP:02X} {timing_parameter_access_type & 0xFF:02X}'
        if timing_parameter_request_record is not None:
            request = f'{request} {" ".join([f"{value & 0xFF:02X}" for value in timing_parameter_request_record])}'
        return request

    def secured_data_transmission(self, security_data_request_record: list[int]) -> str:
        """service to transmit data that is protected against attacks from third parties - which could endanger data security.
        Check ISO 14229 doc for more information about service.

        Args:
            security_data_request_record (list[int]): parameter contains the data as processed by the Security Sub-Layer.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.SDT:02X} {" ".join([f"{value & 0xFF:02X}" for value in security_data_request_record])}'
        return request

    def control_dtc_setting(self, dtc_setting_type: int, dtc_setting_control_option_record: list[int] = None) -> str:
        """service used by a client to stop or resume the updating of DTC status bits in the server.
        Check ISO 14229 doc for more information about service.

        Args:
            dtc_setting_type (int): 1 byte parameter used by the service to indicate to the server(s) whether diagnostic trouble code status bit updating shall stop or start again.
            dtc_setting_control_option_record (list[int], optional): parameter record is user optional to transmit data to a server when controlling the updating of DTC status bits. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.CDTCS:02X} {dtc_setting_type & 0xFF:02X}'
        if dtc_setting_control_option_record is not None:
            request = f'{request} {" ".join([f"{value & 0xFF:02X}" for value in dtc_setting_control_option_record])}'
        return request

    def response_on_event(self, event_type: int, event_window_time: int, event_type_record: list[int] = None, service_to_respond_to_record: list[int] = None) -> str:
        """service requests a server to start or stop transmission of responses on a specified event.
        Check ISO 14229 doc for more information about service.

        Args:
            event_type (int): 1 byte parameter is used by the service to specify the event to be configured in the server and to control the service set up.
            event_window_time (int): 1 byte parameter is used to specify a window for the event logic to be active in the server.
            event_type_record (list[int], optional): parameter record contains additional parameters for the specified eventType. Defaults to None.
            service_to_respond_to_record (list[int], optional): parameter record contains the service parameters of the service to be executed in the server each time the specified event defined in the eventTypeRecord occurs. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.ROE:02X} {event_type & 0xFF:02X} {event_window_time & 0xFF:02X}'
        if event_type_record is not None:
            request = f'{request} {" ".join([f"{value & 0xFF:02X}" for value in event_type_record])}'
        if service_to_respond_to_record is not None:
            request = f'{request} {" ".join([f"{value & 0xFF:02X}" for value in service_to_respond_to_record])}'
        return request

    def link_control(self, link_control_type: int, link_control_mode_identifier: int = None, link_record: int = None) -> str:
        """service is used to control the communication between the client and the server in order to gain bus bandwidth for diagnostic purposes.
        Check ISO 14229 doc for more information about service.

        Args:
            link_control_type (int): 1 byte parameter is used by the service to describe the action to be performed in the server.
            link_control_mode_identifier (int, optional): This conditional 1 byte parameter references a fixed defined mode parameter. Defaults to None.
            link_record (int, optional): This conditional 3 byte parameter record contains a specific mode parameter in case the sub-function parameter indicates that a specific parameter is used. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.LC:02X} {link_control_type & 0xFF:02X}'
        if link_control_mode_identifier is not None:
            request = f'{request} {link_control_mode_identifier}'
        if link_record is not None:
            request = f'{request} {(link_record & 0xFF0000) >> 16:02X} {(link_record & 0xFF00) >> 8:02X} {link_record & 0xFF}'
        return request

    # Data transmission
    def read_data_by_identifier(self, data_identifier: list[int]) -> str:
        """service allows the client to request data record values from the server identified by one or more dataIdentifiers.
        Check ISO 14229 doc for more information about service.

        Args:
            data_identifier (list[int]): parameter identifies the server data record(s) that are being requested by the client.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.RDBI:02X} {" ".join([f"{(value & 0xFF00) >> 8:02X} {value & 0xFF}" for value in data_identifier])}'
        return request

    def read_memory_by_address(self, address_and_length_format_identifier: int, memory_address: int, memory_size: int) -> str:
        """service allows the client to request memory data from the server via provided starting address and size of memory to be read.
        Check ISO 14229 doc for more information about service.

        Args:
            address_and_length_format_identifier (int): parameter is a one byte value with each nibble encoded separately. bit 7 - 4: Length (number of bytes) of the memorySize parameter. bit 3 - 0: Length (number of bytes) of the memoryAddress parameter.
            memory_address (int): parameter is the starting address of server memory from which data is to be retrieved.
            memory_size (int): parameter in the service specifies the number of bytes to be read starting at the address specified by memoryAddress in the server's memory.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.RMBA:02X} {address_and_length_format_identifier & 0xFF}'
        length_of_memory_address = address_and_length_format_identifier & 0xF
        length_of_memory_size = (address_and_length_format_identifier & 0xF0) >> 4
        request = f'{request} {" ".join([f"{(memory_address >> (i * 8)) & 0xFF:02X}" for i in reversed(range(length_of_memory_address))])}'
        request = f'{request} {" ".join([f"{(memory_size >> (i * 8)) & 0xFF:02X}" for i in reversed(range(length_of_memory_size))])}'
        return request

    def read_scaling_data_by_identifier(self, data_identifier: int) -> str:
        """service allows the client to request scaling data record information from the server identified by a dataIdentifier.
        Check ISO 14229 doc for more information about service.

        Args:
            data_identifier (int): 2 byte parameter identifies the server data record that is being requested by the client.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.RSDBI:02X} {(data_identifier & 0xFF00) >> 8:02X} {data_identifier & 0xFF:02X}'
        return request

    def read_data_by_periodic_identifier(self, transmission_mode: int, periodic_data_identifier: list[int]) -> str:
        """service allows the client to request the periodic transmission of data record values from the server identified by one or more periodicDataIdentifiers.
        Check ISO 14229 doc for more information about service.

        Args:
            transmission_mode (int): 1 byte parameter identifies the transmission rate of the requested periodicDataIdentifiers to be used by the server.
            periodic_data_identifier (list[int]): parameter identifies the server data record(s) that are being requested by the client.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.RDBPI:02X} {transmission_mode:02X}'
        request = f'{request} {" ".join([f"{value & 0xFF:02X}" for value in periodic_data_identifier])}'
        return request

    def dynamically_define_data_identifier(self, definition_type: int, supporting_params: Union[list[list[int]], int]) -> str:
        """service allows the client to dynamically define in a server a data identifier that can be read via the ReadDataByIdentifier service at a later time.
        Check ISO 14229 doc for more information about service.

        Args:
            definition_type (int): 1 byte parameter to mention definition type. check UDS ISO document for values.
            supporting_params (list[list[int]] | int): check UDS ISO document for different possible values.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        request = f'{self.sid.DDDI:02X} {definition_type:02X}'
        if definition_type == 0x01:
            for params in supporting_params:
                dynamically_defined_data_identifier = f'{params[0] >> 8 & 0xFF:02X} {params[0] & 0xFF:02X}'
                source_data_identifier = f'{params[1] >> 8 & 0xFF:02X} {params[1] & 0xFF:02X}'
                position_in_source_data_record = f'{params[2] & 0xFF:02X}'
                memory_size = f'{params[3] & 0xFF:02X}'
                request = f'{request} {dynamically_defined_data_identifier} {source_data_identifier} {position_in_source_data_record} {memory_size}'
        elif definition_type == 0x02:
            for params in supporting_params:
                dynamically_defined_data_identifier = f'{params[0] >> 8 & 0xFF:02X} {params[0] & 0xFF:02X}'
                address_and_length_format_identifier = f'{params[1] & 0xFF:02X}'
                length_of_memory_address = address_and_length_format_identifier & 0xF
                length_of_memory_size = (address_and_length_format_identifier & 0xF0) >> 4
                memory_address = f'{" ".join([f"{(params[2] >> (i * 8)) & 0xFF:02X}" for i in reversed(range(length_of_memory_address))])}'
                memory_size = f'{" ".join([f"{(params[3] >> (i * 8)) & 0xFF:02X}" for i in reversed(range(length_of_memory_size))])}'
                request = f'{request} {dynamically_defined_data_identifier} {address_and_length_format_identifier} {memory_address} {memory_size}'
        elif definition_type == 0x03:
                dynamically_defined_data_identifier = f'{supporting_params >> 8 & 0xFF:02X} {supporting_params & 0xFF:02X}'
                request = f'{request} {dynamically_defined_data_identifier}'
        else:
            print(f'invalid definition_type {definition_type}. possible values -> 0 to 3. request sent without supporting_params')
        return request

    def write_data_by_identifier(self, data_identifier: int, data_record: list[int]) -> str:
        """service allows the client to write information into the server at an internal location specified by the provided data identifier.
        Check ISO 14229 doc for more information about service.

        Args:
            data_identifier (int): 2 byte parameter identifies the server data record that the client is requesting to write to.
            data_record (list[int]):  parameter provides the data record associated with the dataIdentifier that the client is requesting to write to.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        data_identifier = self.convert_int_to_str_of_bytes(data_identifier)
        data_record = " ".join([f"{value & 0xFF:02X}" for value in data_record])
        request = f'{self.sid.WDBI:02X} {data_identifier} {data_record}'
        return request

    def write_memory_by_address(self, address_and_length_format_identifier: int, memory_address: int, memory_size: int, data_record: list[int]) -> str:
        """service allows the client to write information into the server at one or more contiguous memory locations.
        Check ISO 14229 doc for more information about service.

        Args:
            address_and_length_format_identifier (int): parameter is a one byte value with each nibble encoded separately. check UDS ISO for more info.
            memory_address (int): parameter is the starting address of server memory to which data is to be written.
            memory_size (int): parameter in the service specifies the number of bytes to be written starting at the address specified by memoryAddress in the server's memory.
            data_record (list[int]): parameter provides the data that the client is actually attempting to write into the server memory addresses within the interval.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        address_and_length_format_identifier = self.convert_int_to_str_of_bytes(address_and_length_format_identifier)
        memory_address = self.convert_int_to_str_of_bytes(memory_address)
        memory_size = self.convert_int_to_str_of_bytes(memory_size)
        data_record = " ".join([f"{value & 0xFF:02X}" for value in data_record])
        request = f'{self.sid.WMBA:02X} {address_and_length_format_identifier} {memory_address} {memory_size} {data_record}'
        return request

    # Stored data transmission
    def clear_diagnostic_information(self, group_of_dtc: int) -> str:
        """service is used by the client to clear diagnostic information in one or multiple servers memory.
        Check ISO 14229 doc for more information about service.

        Args:
            group_of_dtc (int): parameter contains a 3-byte value indicating the group of DTCs (e.g., Powertrain, Body, Chassis) or the particular DTC to be cleared.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        group_of_dtc = self.convert_int_to_str_of_bytes(group_of_dtc)
        request = f'{self.sid.CDTCI:02X} {group_of_dtc}'
        return request

    def read_dtc_information(self, report_type: int, remaining_arguments_list: list[int]) -> str:
        """service allows a client to read the status of server resident Diagnostic Trouble Code (DTC) information from any server, or group of servers within a vehicle.
        Check ISO 14229 doc for more information about service.

        Args:
            report_type (int): type of DTC's that we need to retrieve from ECU.
            remaining_arguments_list (list[int]): list of remaining arguments needed for type of DTC's to be fetched.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        report_type = self.convert_int_to_str_of_bytes(report_type)
        remaining_arguments_list = " ".join([f"{value & 0xFF:02X}" for value in remaining_arguments_list])
        request = f'{self.sid.RDTCI:02X} {report_type} {remaining_arguments_list}'
        return request

    # Input Output control
    def input_output_control_by_identifier(self, data_identifier: int, control_option_record: list[int], control_enable_mask_record: list[int] = None) -> str:
        """service is used by the client to substitute a value for an input signal, internal server function and/or force control to a value for an output (actuator) of an electronic system.
        Check ISO 14229 doc for more information about service.

        Args:
            data_identifier (int): parameter identifies an server local input signal(s), internal parameter(s) and/or output signal(s).
            control_option_record (list[int]): one or multiple bytes (inputOutputControlParameter and controlState 1 to controlState m).
            control_enable_mask_record (list[int], optional): one or multiple bytes (controlMask 1 to controlMask r). Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        data_identifier = self.convert_int_to_str_of_bytes(data_identifier)
        control_option_record = f'{" ".join([f"{value & 0xFF:02X}" for value in control_option_record])}'
        control_enable_mask_record = '' if control_enable_mask_record is None else f'{" ".join([f"{value & 0xFF:02X}" for value in control_enable_mask_record])}'
        request = f'{self.sid.IOCBI:02X} {data_identifier} {control_option_record} {control_enable_mask_record}'
        return request

    # Remote activation of routine
    def routine_control(self, routine_control_type: int, routine_identifier: int, routine_control_option_record: list[int] = None) -> str:
        """service is used by the client to execute a defined sequence of steps and obtain any relevant results.
        Check ISO 14229 doc for more information about service.

        Args:
            routine_control_type (int): 1 byte parameter used by this service to select the control of the routine.
            routine_identifier (int): parameter identifies a server local routine and is out of the range of defined dataIdentifiers.
            routine_control_option_record (list[int], optional): Routine entry/exit option parameters. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        routine_control_type = self.convert_int_to_str_of_bytes(routine_control_type)
        routine_identifier = self.convert_int_to_str_of_bytes(routine_identifier)
        routine_control_option_record = '' if routine_control_option_record is None else f'{" ".join([f"{value & 0xFF:02X}" for value in routine_control_option_record])}'
        request = f'{self.sid.RC:02X} {routine_control_type} {routine_identifier} {routine_control_option_record}'
        return request

    # Upload download
    def request_download(self, data_format_identifier: int, address_and_length_format_identifier: int, memory_address: int, memory_size: int) -> str:
        """service is used by the client to initiate a data transfer from the client to the server.
        Check ISO 14229 doc for more information about service.

        Args:
            data_format_identifier (int): one byte value with each nibble encoded separately. The high nibble specifies the "compressionMethod", and the low nibble specifies the "encryptingMethod".
            address_and_length_format_identifier (int): parameter is a one byte value with each nibble encoded separately. bit 7 - 4: Length of the memorySize parameter. bit 3 - 0: Length of the memoryAddress parameter.
            memory_address (int): starting address of the server memory where the data is to be written to.
            memory_size (int): parameter shall be used by the server to compare the memory size with the total amount of data transferred during the TransferData service.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        data_format_identifier = f'{data_format_identifier & 0xFF:02X}'
        address_and_length_format_identifier = f'{address_and_length_format_identifier & 0xFF:02X}'
        memory_address = self.convert_int_to_str_of_bytes(memory_address)
        memory_size = self.convert_int_to_str_of_bytes(memory_size)
        request = f'{self.sid.RD:02X} {data_format_identifier} {address_and_length_format_identifier} {memory_address} {memory_size}'
        return request

    def request_upload(self, data_format_identifier: int, address_and_length_format_identifier: int, memory_address: int, memory_size: int) -> str:
        """service is used by the client to initiate a data transfer from the server to the client.
        Check ISO 14229 doc for more information about service.

        Args:
            data_format_identifier (int): one byte value with each nibble encoded separately. The high nibble specifies the "compressionMethod", and the low nibble specifies the "encryptingMethod".
            address_and_length_format_identifier (int): parameter is a one byte value with each nibble encoded separately. bit 7 - 4: Length of the memorySize parameter. bit 3 - 0: Length of the memoryAddress parameter.
            memory_address (int): starting address of server memory from which data is to be retrieved.
            memory_size (int): parameter shall be used by the server to compare the memory size with the total amount of data transferred during the TransferData service.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        data_format_identifier = self.convert_int_to_str_of_bytes(data_format_identifier)
        address_and_length_format_identifier = self.convert_int_to_str_of_bytes(address_and_length_format_identifier)
        memory_address = self.convert_int_to_str_of_bytes(memory_address)
        memory_size = self.convert_int_to_str_of_bytes(memory_size)
        request = f'{self.sid.RU:02X} {data_format_identifier} {address_and_length_format_identifier} {memory_address} {memory_size}'
        return request

    def transfer_data(self, block_sequence_counter: int, transfer_request_parameter_record: list[int]) -> str:
        """service is used by the client to transfer data either from the client to the server (download) or from the server to the client (upload).
        Check ISO 14229 doc for more information about service.

        Args:
            block_sequence_counter (int): parameter value starts at 0x01 with the first TransferData request that follows the RequestDownload (0x34) or RequestUpload (0x35) service.
            transfer_request_parameter_record (list[int], optional): parameter record contains parameter(s) which are required by the server to support the transfer of data. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        block_sequence_counter = self.convert_int_to_str_of_bytes(block_sequence_counter)
        transfer_request_parameter_record = f'{" ".join([f"{value & 0xFF:02X}" for value in transfer_request_parameter_record])}'
        request = f'{self.sid.TD:02X} {block_sequence_counter} {transfer_request_parameter_record}'
        return request

    def request_transfer_exit(self, transfer_request_parameter_record: list[int] = None) -> str:
        """service is used by the client to terminate a data transfer between client and server (upload or download).
        Check ISO 14229 doc for more information about service.

        Args:
            transfer_request_parameter_record (list[int], optional): parameter record contains parameter(s), which are required by the server to support the transfer of data. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        if transfer_request_parameter_record is None:
            request = f'{self.sid.RTE:02X}'
        else:
            transfer_request_parameter_record = f'{" ".join([f"{value & 0xFF:02X}" for value in transfer_request_parameter_record])}'
            request = f'{self.sid.TD:02X} {transfer_request_parameter_record}'
        return request

    def request_file_transfer(self, mode_of_operation: int, file_path_and_name_length: int, file_path_and_name: list[int], data_format_identifier:  int = None, file_size_parameter_length: int = None,
                              file_size_uncompressed: list[int] = None, file_size_compressed: list[int] = None) -> str:
        """service is used by the client to initiate a file data transfer from either the client to the server or from the server to the client (download or upload).
        Check ISO 14229 doc for more information about service.

        Args:
            mode_of_operation (int): This data-parameter defines the type of operation to be applied to the file or directory indicated in the filePathAndName parameter.
            file_path_and_name_length (int): length in byte for the parameter filePath.
            file_path_and_name (list[int]): Defines the file system location of the server where the file which shall be added, deleted, replaced or read from depending on the parameter modeOfOperation parameter.
            data_format_identifier (int, optional): This data-parameter is a one byte value with each nibble encoded separately.. Defaults to None.
            file_size_parameter_length (int, optional): Defines the length in bytes for both parameters fileSizeUncompressed and fileSizeCompressed. Defaults to None.
            file_size_uncompressed (list[int], optional): Defines the size of the uncompressed file in bytes. Defaults to None.
            file_size_compressed (list[int], optional): Defines the size of the compressed file in bytes. Defaults to None.

        Returns:
            str: complete request in string of bytes with space between each byte.
        """
        mode_of_operation = self.convert_int_to_str_of_bytes(mode_of_operation)
        file_path_and_name_length = self.convert_int_to_str_of_bytes(file_path_and_name_length)
        file_path_and_name = f'{" ".join([f"{value & 0xFF:02X}" for value in file_path_and_name])}'
        data_format_identifier = f'{data_format_identifier & 0xFF:02X}'
        file_size_parameter_length = f'{file_size_parameter_length & 0xFF:02X}'
        file_size_uncompressed = f'{" ".join([f"{value & 0xFF:02X}" for value in file_size_uncompressed])}'
        file_size_compressed = f'{" ".join([f"{value & 0xFF:02X}" for value in file_size_compressed])}'
        request = f'{self.sid.RFT:02X} {mode_of_operation} {file_path_and_name_length} {file_path_and_name} {data_format_identifier} {file_size_parameter_length} {file_size_uncompressed} {file_size_compressed}'
        return request

    def convert_int_to_str_of_bytes(self, integer_value: int) -> str:
        number_of_bytes = round(integer_value.bit_length() / 8)
        hex_str = ' '.join([f'{val:02X}' for val in integer_value.to_bytes(number_of_bytes)])
        return hex_str


class Sid:
    """This class holds all service identifiers name and its value respectively.
    Check ISO 14229 doc for more information.
    """
    def __init__(self) -> None:
        # Diagnostic and communication management
        self.diagnostic_session_control = self.DSC = 0x10

        self.ecu_reset = self.ER = 0x11
        self.security_access = self.SA = 0x27
        self.communication_control = self.CC = 0X28
        self.tester_present = self.TP = 0x3E
        self.access_timing_parameter = self.ATP = 0x83
        self.secured_data_transmission = self.SDT = 0x84
        self.control_dtc_setting = self.CDTCS = 0x85
        self.response_on_event = self.ROE = 0x86
        self.link_control = self.LC = 0x87
        # Data transmission
        self.read_data_by_identifier = self.RDBI = 0x22
        self.read_memory_by_address = self.RMBA = 0x23
        self.read_scaling_data_by_identifier = self.RSDBI = 0x24
        self.read_data_by_periodic_identifier = self.RDBPI = 0x2A
        self.dynamically_define_data_identifier = self.DDDI = 0x2C
        self.write_data_by_identifier = self.WDBI = 0x2E
        self.write_memory_by_address = self.WMBA = 0x3D
        # Stored data transmission
        self.clear_diagnostic_information = self.CDTCI = 0x14
        self.read_dtc_information = self.RDTCI = 0x19
        # Input Output control
        self.input_output_control_by_identifier = self.IOCBI = 0x2F
        # Remote activation of routine
        self.routine_control = self.RC = 0x31
        # Upload download
        self.request_download = self.RD = 0x34
        self.request_upload = self.RU = 0x35
        self.transfer_data = self.TD = 0x36
        self.request_transfer_exit = self.RTE = 0x37
        self.request_file_transfer = self.RFT = 0x38
        # Negative Response
        self.negative_response = self.NR = 0x7F


class Sfid:
    """This class holds all service identifier sub-functions name and its value respectively.
    Check ISO 14229 doc for more information.
    """
    def __init__(self) -> None:
        # diagnostic_session_control
        self.default_session = self.DS = 0x01
        self.programming_session = self.PRGS = 0x02
        self.extended_session = self.EXTDS = 0x03
        self.safety_system_diagnostic_session = self.SSDS = 0x04
        # ecu_reset
        self.hard_reset = self.HR = 0x01
        self.key_on_off_reset = self.KOFFONR = 0x02
        self.soft_reset = self.SR = 0x03
        self.enable_rapid_power_shutdown = self.ERPSD = 0x04
        self.disable_rapid_power_shutdown = self.DRPSD = 0x05
        # security_access
        self.request_seed = self.RSD = 0x01
        self.send_key = self.SK = 0x02
        # communication_control
        self.enable_rx_and_tx = self.ERXTX = 0x00
        self.enable_rx_and_disable_tx = self.ERXDTX = 0x01
        self.disable_rx_and_enable_tx = self.DRXETX = 0x02
        self.disable_rx_and_tx = self.DRXTX = 0x03
        self.enable_rx_and_disable_tx_with_enhanced_address_information = self.ERXDTXWEAI = 0x04
        self.enable_rx_and_tx_with_enhanced_address_information = self.ERXTXWEAI = 0x05
        # tester_present
        self.zero_sub_function = self.ZSUBF = 0x00
        # access_timing_parameter
        self.read_extended_timing_parameter_set = self.RETPS = 0x01
        self.set_timing_parameters_to_default_value = self.STPTDV = 0x02
        self.read_currently_active_timing_parameters = self.RCATP = 0x03
        self.set_timing_parameters_to_given_values = self.STPTGV = 0x04
        # control_dtc_setting
        self.on = self.ON = 0x01
        self.off = self.OFF = 0x02
        # response_on_event
        self.do_not_store_event = self.DNSE = 0x00
        self.store_event = self.SE = 0x01
        self.stop_response_on_event = self.STPROE = 0x00
        self.on_dtc_status_change = self.ONDTCS = 0x01
        self.on_timer_interrupt = self.OTI = 0x02
        self.on_change_of_data_identifier = self.OCODID = 0x03
        self.report_activated_events = self.RAE = 0x04
        self.start_response_on_event = self.STRTROE = 0x05
        self.clear_response_on_event = self.CLRROE = 0x06
        self.on_comparison_of_value = self.OCOV = 0x07
        # link_control
        self.verify_mode_transition_with_fixed_parameter = self.VMTWFP = 0x01
        self.verify_mode_transition_with_specific_parameter = self.VMTWSP = 0x02
        self.transition_mode = self.TM = 0x03
        # dynamically_define_data_identifier
        self.define_by_identifier = self.DBID = 0x01
        self.define_by_memory_address = self.DBMA = 0x02
        self.clear_dynamically_defined_data_identifier = self.CDDDID = 0x03
        # read_dtc_information
        self.report_number_of_dtc_by_status_mask = self.RNODTCBSM = 0x01
        self.report_dtc_by_status_mask = self.RDTCBSM = 0x02
        self.report_dtc_snapshot_identification = self.RDTCSSI = 0x03
        self.report_dtc_snapshot_record_by_dtc_number = self.RDTCSSBDTC = 0x04
        self.read_dtc_stored_data_by_record_number = self.RDTCSDBRN = 0x05
        self.report_dtc_ext_data_record_by_dtc_number = self.RDTCEDRBDN = 0x06
        self.report_number_of_dtc_by_severity_mask_record = self.RNODTCBSMR = 0x07
        self.report_dtc_by_severity_mask_record = self.RDTCBSMR = 0x08
        self.report_severity_information_of_dtc = self.RSIODTC = 0x09
        self.report_mirror_memory_dtc_ext_data_record_by_dtc_number = self.RMDEDRBDN = 0x10
        self.report_supported_dtc = self.RSUPDTC = 0x0A
        self.report_first_test_failed_dtc = self.RFTFDTC = 0x0B
        self.report_first_confirmed_dtc = self.RFCDTC = 0x0C
        self.report_most_recent_test_failed_dtc = self.RMRTFDTC = 0x0D
        self.report_most_recent_confirmed_dtc = self.RMRCDTC = 0x0E
        self.report_mirror_memory_dtc_by_status_mask = self.RMMDTCBSM = 0x0F
        self.report_number_of_mirror_memory_dtc_by_status_mask = self.RNOMMDTCBSM = 0x11
        self.report_number_of_emission_obd_dtc_by_status_mask = self.RNOOEBDDTCBSM = 0x12
        self.report_emission_obd_dtc_by_status_mask = self.ROBDDTCBSM = 0x13
        self.report_dtc_fault_detection_counter = self.RDTCFDC = 0x14
        self.report_dtc_with_permanent_status = self.RDTCWPS = 0x15
        self.report_dtc_ext_data_record_by_record_number = self.RDTCEDRBR = 0x16
        self.report_user_def_memory_dtc_by_status_mask = self.RUDMDTCBSM = 0x17
        self.report_user_def_memory_dtc_snapshot_record_by_dtc_number = self.RUDMDTCSSBDTC = 0x18
        self.report_user_def_memory_dtc_ext_data_record_by_dtc_number = self.RUDMDTCEDRBDN = 0x19
        self.report_wwh_obd_dtc_by_mask_record = self.ROBDDTCBMR = 0x42
        self.report_wwh_obd_dtc_with_permanent_status = self.RWWHOBDDTCWPS = 0x55
        self.start_routine = self.STR = 0x01
        self.stop_routine = self.STPR = 0x02
        self.request_routine_result = self.RRR = 0x03


class Nrc:
    """This class holds all negative response codes name and its values respectively.
    Check ISO 14229 doc for more information.
    """
    def __init__(self) -> None:
        self.general_reject = self.GR = 0x10
        self.service_not_supported = self.SNS = 0x11
        self.sub_function_not_supported = self.SFNS = 0x12
        self.incorrect_message_length_or_invalid_format = self.IMLOIF = 0x13
        self.response_too_long = self.RTL = 0x14
        self.busy_repeat_request = self.BRR = 0x21
        self.conditions_not_correct = self.CNC = 0x22
        self.request_sequence_error = self.RSE = 0x24
        self.no_response_from_subnet_component = self.NRFSC = 0x25
        self.failure_prevents_execution_of_requested_action = self.FPEORA = 0x26
        self.request_out_of_range = self.ROOR = 0x31
        self.security_access_denied = self.SAD = 0x33
        self.invalid_key = self.IK = 0x35
        self.exceeded_number_of_attempts = self.ENOA = 0x36
        self.required_time_delay_not_expired = self.RTDNE = 0x37
        self.upload_download_not_accepted = self.UDNA = 0x70
        self.transfer_data_suspended = self.TDS = 0x71
        self.general_programming_failure = self.GPF = 0x72
        self.wrong_block_sequence_counter = self.WBSC = 0x73
        self.request_correctly_received_response_pending = self.RCRRP = 0x78
        self.sub_function_not_supported_in_active_session = self.SFNSIAS = 0x7E
        self.service_not_supported_in_active_session = self.SNSIAS = 0x7F
        self.rpm_too_high = self.RPMTH = 0x81
        self.rpm_too_low = self.RPMTL = 0x82
        self.engine_is_running = self.EIR = 0x83
        self.engine_is_not_running = self.EINR = 0x84
        self.engine_run_time_too_low = self.ERTTL = 0x85
        self.temperature_too_high = self.TEMPTH = 0x86
        self.temperature_too_low = self.TEMPTL = 0x87
        self.vehicle_speed_too_high = self.VSTH = 0x88
        self.vehicle_speed_too_low = self.VSTL = 0x89
        self.throttle_or_pedal_too_high = self.TPTH = 0x8A
        self.throttle_or_pedal_too_low = self.TPTL = 0x8B
        self.transmission_range_not_in_neutral = self.TRNIN = 0x8C
        self.transmission_range_not_in_gear = self.TRNIG = 0x8D
        self.brake_switch_not_closed = self.BSNC = 0x8F
        self.shifter_lever_not_in_park = self.SLNIP = 0x90
        self.torque_converter_clutch_locked = self.TCCL = 0x91
        self.voltage_too_high = self.VTH = 0x92
        self.voltage_too_low = self.VTL = 0x93
