from unittest import TestCase

import RFXtrx

class Lighting5TestCase(TestCase):

    def setUp(self):

        self.data = bytearray(b'\x0A\x14\x00\xAD\xF3\x94\xAB'
                              b'\x01\x01\x00\x60')
        self.parser = RFXtrx.lowlevel.Lighting5()

    def test_parse_bytes(self):

        light = RFXtrx.lowlevel.parse(self.data)
        self.assertEquals(RFXtrx.lowlevel.Lighting5, type(light))
        self.assertEquals(light.type_string,"LightwaveRF, Siemens")
        self.assertEquals(light.seqnbr,173)
        self.assertEquals(light.id_string,"f394ab:1")
        self.assertEquals(light.cmnd_string,"On")
        self.assertEquals(light.cmnd,1)
        self.assertEquals(light.level,0)
