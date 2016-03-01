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
        self.assertEquals(energy.totalwatts,920825.1947099693)
    