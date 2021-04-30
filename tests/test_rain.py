from unittest import TestCase

import RFXtrx


class RainTestCase(TestCase):


    def test_rain2(self):
        data = [0x0B, 0x55, 0x02, 0x17, 0xB6, 0x00, 0x00, 0x00, 0x00, 0x4D, 0x3C, 0x69]
        packet = RFXtrx.lowlevel.parse(data)
        self.assertEqual(RFXtrx.lowlevel.Rain, type(packet))
        self.assertEqual(packet.type_string,'PCR800')
        self.assertEqual(packet.id_string,'b6:00')
        self.assertAlmostEqual(packet.rainrate, 0)
        self.assertAlmostEqual(packet.raintotal, 1977.2)
        self.assertEqual(packet.battery, 9)
        self.assertEqual(packet.rssi, 6)

    def test_rain6(self):
        data = [0x0B, 0x55, 0x06, 0x03, 0x3E, 0xBB, 0x00, 0x00, 0x00, 0x00, 0x7F, 0x69]
        packet = RFXtrx.lowlevel.parse(data)
        self.assertEqual(RFXtrx.lowlevel.Rain, type(packet))
        self.assertEqual(packet.type_string,'La Crosse TX5')
        self.assertEqual(packet.id_string,'3e:bb')
        self.assertAlmostEqual(packet.rainrate, None)
        self.assertAlmostEqual(packet.raintotal, 33.782)
        self.assertEqual(packet.battery, 9)
        self.assertEqual(packet.rssi, 6)

    def test_rain8(self):
        data = [0x0B, 0x55, 0x08, 0x03, 0x3E, 0xBB, 0x00, 0x00, 0x00, 0x00, 0x7F, 0x69]
        packet = RFXtrx.lowlevel.parse(data)
        self.assertEqual(RFXtrx.lowlevel.Rain, type(packet))
        self.assertEqual(packet.type_string,'Davis')
        self.assertEqual(packet.id_string,'3e:bb')
        self.assertAlmostEqual(packet.rainrate, None)
        self.assertAlmostEqual(packet.raintotal, 25.400)
        self.assertEqual(packet.battery, 9)
        self.assertEqual(packet.rssi, 6)

    def test_rain9(self):
        data = [0x0B, 0x55, 0x09, 0x03, 0x3E, 0xBB, 0x00, 0x00, 0x00, 0x00, 0x7F, 0x69]
        packet = RFXtrx.lowlevel.parse(data)
        self.assertEqual(RFXtrx.lowlevel.Rain, type(packet))
        self.assertEqual(packet.type_string,'TFA 30.3233.01')
        self.assertEqual(packet.id_string,'3e:bb')
        self.assertAlmostEqual(packet.rainrate, None)
        self.assertAlmostEqual(packet.raintotal, 32.258)
        self.assertEqual(packet.battery, 9)
        self.assertEqual(packet.rssi, 6)
