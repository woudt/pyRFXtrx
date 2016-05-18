from unittest import TestCase

import RFXtrx
        
class Elec2TestCase(TestCase):

    def setUp(self):

        self.data = bytearray(b'\x11\x5A\x01\x00\x2E\xB2\x03\x00\x00'
                              b'\x02\xB4\x00\x00\x0C\x46\xA8\x11\x69')
        self.parser = RFXtrx.lowlevel.Energy()

    def test_parse_bytes(self):

        energy = RFXtrx.lowlevel.parse(self.data)
        self.assertEquals(energy.type_string,"CM119/160")
        self.assertEquals(energy.seqnbr,0)
        self.assertEquals(energy.id_string,"2e:b2")
        self.assertEquals(energy.count,3)
        self.assertEquals(energy.currentwatt,692)
        self.assertEquals(energy.totalwatts,920824.5195961836)

class Elec4TestCase(TestCase):

    def setUp(self):

        self.data = bytearray(b'\x13\x5b\x01\x04'
                              b'\x2e\xB2'
                              b'\x01'
                              b'\x11\x12'
                              b'\x14\x15'
                              b'\x17\x18'
                              b'\x17\x18\x19\x20\x21\x22'
                              b'\x69')
        self.parser = RFXtrx.lowlevel.Energy4()

    def test_parse_bytes(self):

        energy = RFXtrx.lowlevel.parse(self.data)
        self.assertEquals(energy.type_string,"CM180i")
        self.assertEquals(energy.seqnbr,4)
        self.assertEquals(energy.id_string,"2e:b2")
        self.assertEquals(energy.count,1)
        self.assertEquals(energy.currentamps1,437)
        self.assertEquals(energy.currentamps2,514.1)
        self.assertEquals(energy.currentamps3,591.2)
        self.assertEquals(energy.totalwatthours,113527617921.3023)
