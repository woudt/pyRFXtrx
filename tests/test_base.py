from unittest import TestCase
from mock import Mock

import RFXtrx


def _callback(*args, **kwargs):
    pass


def _callback2(*args, **kwargs):
    pass


class CoreTestCase(TestCase):

    def setup_class(self):

        self.elec_packet = (b'\x11\x5A\x01\x00\x2E\xB2\x03\x00\x00'
                            b'\x02\xB4\x00\x00\x0C\x46\xA8\x11\x69')

        device = '/dev/serial/...'
        self.core =  RFXtrx.Connect(device, event_callback=_callback, debug=False, transport_protocol=RFXtrx.DummyTransport)
        self.bytes_array = bytearray(b'\x11\x5A\x01\x00\x2E\xB2\x03\x00\x00')


    def test_constructor(self):

        mock = Mock()
        device = '/dev/serial/...'
        RFXtrx.Core(device, event_callback=_callback, debug=False, transport_protocol=mock)
        mock.assert_called_once_with(device, False)

    def test_format_packet(self):
        bytes_array = bytearray([0x07, 0x10, 0x00, 0x2a, 0x45, 0x05, 0x01, 0x70])
        event = self.core.transport.parse(bytes_array)
        self.assertEquals(RFXtrx.ControlEvent, type(event))
        self.assertEquals(event.device.type_string,'X10 lighting')
        self.assertEquals(event.device.id_string,'E5')
        self.assertEquals(event.values['Command'],'On')
        self.assertEquals(event.values['Rssi numeric'],7)

        event.device.send_on(self.core.transport)



