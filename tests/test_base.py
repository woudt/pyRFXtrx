from unittest import TestCase
import time

import RFXtrx

num_calbacks = 0
def _callback(*args, **kwargs):
    global num_calbacks
    num_calbacks = num_calbacks + 1


class CoreTestCase(TestCase):

    def setup_class(self):
        device = '/dev/serial/...'
        global num_calbacks
        num_calbacks = 0

        self.core =  RFXtrx.Connect(device, event_callback=_callback, debug=False, transport_protocol=RFXtrx.DummyTransport)

    def test_constructor(self):
        device = '/dev/serial/...'
        core = RFXtrx.Core(device, event_callback=_callback, debug=False,transport_protocol=RFXtrx.DummyTransport2)
        global num_calbacks
        while num_calbacks < 5:
            time.sleep(0.1)

        self.assertEquals(len(core.sensors()),2)

    def test_format_packet(self):
        # Lighting1
        bytes_array = bytearray([0x07, 0x10, 0x00, 0x2a, 0x45, 0x05, 0x01, 0x70])
        event = self.core.transport.parse(bytes_array)
        self.assertEquals(RFXtrx.ControlEvent, type(event))
        self.assertEquals(event.device.type_string,'X10 lighting')
        self.assertEquals(event.device.id_string,'E5')
        self.assertEquals(event.values['Command'],'On')
        self.assertEquals(event.values['Rssi numeric'],7)
        event.device.send_on(self.core.transport)
        event.device.send_off(self.core.transport)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,50)

        # Lighting2
        bytes_array =[0x0b, 0x11, 0x00, 0x2a, 0x01, 0x23, 0x45, 0x67, 0x05, 0x02, 0x07, 0x70]
        event = self.core.transport.parse(bytes_array)
        event.device.send_on(self.core.transport)
        event.device.send_off(self.core.transport)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,150)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,-1)
        event.device.send_dim(self.core.transport,50)
        event.device.send_dim(self.core.transport,0)

        # Lighting3
        bytes_array = [0x08, 0x12, 0x00, 0x2a, 0x01, 0x34, 0x02, 0x15, 0x79]
        event = self.core.transport.parse(bytes_array)
        event.device.send_on(self.core.transport)
        event.device.send_off(self.core.transport)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,50)

        # Lighting4, not supported yet
        bytes_array = [0x09, 0x13, 0x00, 0x2a, 0x12, 0x34, 0x56, 0x01, 0x5e, 0x70]
        event = self.core.transport.parse(bytes_array)
        self.assertEquals(RFXtrx.ControlEvent, type(event))
        self.assertEquals(RFXtrx.RFXtrxDevice, type(event.device))
       # event.device.send_on(self.core.transport)
       # event.device.send_off(self.core.transport)
       # self.assertRaises(ValueError,event.device.send_dim,self.core.transport,50)

        # Lighting5, subtype0
        bytes_array = bytearray(b'\x0A\x14\x00\xAD\xF3\x94\xAB\x01\x10\x00\x60')
        event = self.core.transport.parse(bytes_array)
        event.device.send_on(self.core.transport)
        event.device.send_off(self.core.transport)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,150)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,-1)
        event.device.send_dim(self.core.transport,50)
        event.device.send_dim(self.core.transport,0)

        # Lighting5, subtype1
        bytes_array = bytearray(b'\x0A\x14\x01\xAD\xF3\x94\xAB\x01\x10\x00\x60')
        event = self.core.transport.parse(bytes_array)
        event.device.send_on(self.core.transport)
        event.device.send_off(self.core.transport)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,150)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,-1)
        event.device.send_dim(self.core.transport,50)
        event.device.send_dim(self.core.transport,0)


        # Lighting5, subtype2
        bytes_array = bytearray(b'\x0A\x14\x02\xAD\xF3\x94\xAB\x01\x10\x00\x60')
        event = self.core.transport.parse(bytes_array)
        event.device.send_on(self.core.transport)
        event.device.send_off(self.core.transport)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,150)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,-1)
        event.device.send_dim(self.core.transport,50)
        event.device.send_dim(self.core.transport,0)


        # Lighting5, subtype3
        bytes_array = bytearray(b'\x0A\x14\x03\xAD\xF3\x94\xAB\x01\x10\x00\x60')
        event = self.core.transport.parse(bytes_array)
        event.device.send_on(self.core.transport)
        event.device.send_off(self.core.transport)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,150)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,-1)
        event.device.send_dim(self.core.transport,50)
        event.device.send_dim(self.core.transport,0)


        # Lighting5, subtype4
        bytes_array = bytearray(b'\x0A\x14\x04\xAD\xF3\x94\xAB\x01\x10\x00\x60')
        event = self.core.transport.parse(bytes_array)
        event.device.send_on(self.core.transport)
        event.device.send_off(self.core.transport)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,150)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,-1)
        event.device.send_dim(self.core.transport,50)
        event.device.send_dim(self.core.transport,0)

        # Lighting5, subtype5
        bytes_array = bytearray(b'\x0A\x14\x05\xAD\xF3\x94\xAB\x01\x10\x00\x60')
        event = self.core.transport.parse(bytes_array)
        event.device.send_on(self.core.transport)
        event.device.send_off(self.core.transport)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,150)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,-1)
        event.device.send_dim(self.core.transport,50)
        event.device.send_dim(self.core.transport,0)

        # Lighting5, subtype6 . unknown
        bytes_array = bytearray(b'\x0A\x14\x06\xAD\xF3\x94\xAB\x01\x10\x00\x60')
        event = self.core.transport.parse(bytes_array)
        event.device.send_on(self.core.transport)
        event.device.send_off(self.core.transport)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,150)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,-1)
        event.device.send_dim(self.core.transport,50)
        event.device.send_dim(self.core.transport,0)

        #Lighting 6
        bytes_array = [0x0b, 0x15, 0x00, 0x2a, 0x12, 0x34, 0x41, 0x05, 0x03, 0x01, 0x00, 0x70]
        event = self.core.transport.parse(bytes_array)
        event.device.send_on(self.core.transport)
        event.device.send_off(self.core.transport)
        self.assertRaises(ValueError,event.device.send_dim,self.core.transport,50)

        #rain
        bytes_array = [0x0b, 0x55, 0x02, 0x03, 0x12, 0x34, 0x02, 0x50, 0x01, 0x23, 0x45, 0x57]
        event = self.core.transport.parse(bytes_array)
        self.assertEquals(RFXtrx.SensorEvent, type(event))
        self.assertEquals(event.__str__(),"<class 'RFXtrx.SensorEvent'> device=[<class 'RFXtrx.RFXtrxDevice'> type='PCR800' id='12:34'] values=[('Battery numeric', 7), ('Rain rate', 5.92), ('Rain total', 7456.5), ('Rssi numeric', 5)]")

        #baro
        bytes_array = [0x09, 0x53, 0x01, 0x2a, 0x96, 0x03, 0x04, 0x06, 0x00, 0x79]
        event = self.core.transport.parse(bytes_array)
        self.assertEquals(RFXtrx.SensorEvent, type(event))
        self.assertEquals(event.__str__(),"<class 'RFXtrx.SensorEvent'> device=[<class 'RFXtrx.RFXtrxDevice'> type='Unknown type (0x53/0x01)' id='96:03'] values=[('Barometer', 1030), ('Battery numeric', 9), ('Forecast', 'no forecast available'), ('Forecast numeric', 0), ('Rssi numeric', 7)]")

        #wind
        bytes_array = [0x10, 0x56, 0x01, 0x03, 0x2F, 0x00, 0x00, 0xF7, 0x00, 0x20, 0x00, 0x24, 0x81, 0x60, 0x82, 0x50, 0x59]
        event = self.core.transport.parse(bytes_array)
        self.assertEquals(RFXtrx.SensorEvent, type(event))
        self.assertEquals(event.__str__(),"<class 'RFXtrx.SensorEvent'> device=[<class 'RFXtrx.RFXtrxDevice'> type='WTGR800' id='2f:00'] values=[('Battery numeric', 9), ('Chill', -59.2), ('Rssi numeric', 5), ('Temperature', -35.2), ('Wind average speed', 3.2), ('Wind direction', 247), ('Wind gust', 3.6)]")

        #Lighting5
        bytes_array = bytearray(b'\x0A\x14\x00\xAD\xF3\x94\xAB'
                                b'\x01\x01\x00\x60')
        event= self.core.transport.receive(bytes_array)
        self.assertEquals(RFXtrx.ControlEvent, type(event))
        self.assertEquals(event.__str__(),"<class 'RFXtrx.ControlEvent'> device=[<class 'RFXtrx.LightingDevice'> type='LightwaveRF, Siemens' id='f394ab:1'] values=[('Command', 'On'), ('Rssi numeric', 6)]")

        #temphumid
        bytes_array = [0x0a, 0x52, 0x01, 0x2a, 0x96, 0x03, 0x81, 0x41, 0x60, 0x03, 0x79]
        event = self.core.transport.parse(bytes_array)
        self.assertEquals(RFXtrx.SensorEvent, type(event))
        self.assertEquals(event.__str__(),"<class 'RFXtrx.SensorEvent'> device=[<class 'RFXtrx.RFXtrxDevice'> type='THGN122/123, THGN132, THGR122/228/238/268' id='96:03'] values=[('Battery numeric', 9), ('Humidity', 96), ('Humidity status', 'wet'), ('Humidity status numeric', 3), ('Rssi numeric', 7), ('Temperature', -32.1)]")

        #Chime
        bytes_array = [0x0a, 0x16, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        event = self.core.transport.parse(bytes_array)
        self.assertEquals(RFXtrx.SensorEvent, type(event))
        self.assertEquals(event.__str__(),"<class 'RFXtrx.SensorEvent'> device=[<class 'RFXtrx.RFXtrxDevice'> type='Byron SX' id='00:00'] values=[('Battery numeric', 0), ('Rssi numeric', 0), ('Sound', 0)]")

        #security1
        bytes_array = [0x0a, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        event = self.core.transport.parse(bytes_array)
        self.assertEquals(RFXtrx.SensorEvent, type(event))
        self.assertEquals(event.__str__(),"<class 'RFXtrx.SensorEvent'> device=[<class 'RFXtrx.RFXtrxDevice'> type='X10 Security' id='000000:32'] values=[('Battery numeric', 0), ('Rssi numeric', 0), ('Sensor Status', 'Normal')]")

        #temp
        bytes_array = [0x0a, 0x50, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        event = self.core.transport.parse(bytes_array)
        self.assertEquals(RFXtrx.SensorEvent, type(event))
        self.assertEquals(event.__str__(),"<class 'RFXtrx.SensorEvent'> device=[<class 'RFXtrx.RFXtrxDevice'> type='THR128/138, THC138' id='00:00'] values=[('Battery numeric', 0), ('Rssi numeric', 0), ('Temperature', 0.0)]")

        #humid
        bytes_array = [0x0a, 0x51, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        event = self.core.transport.parse(bytes_array)
        self.assertEquals(RFXtrx.SensorEvent, type(event))
        self.assertEquals(event.__str__(),"<class 'RFXtrx.SensorEvent'> device=[<class 'RFXtrx.RFXtrxDevice'> type='LaCrosse TX3' id='00:00'] values=[('Battery numeric', 0), ('Humidity', 0), ('Humidity status', 'dry'), ('Humidity status numeric', 0), ('Rssi numeric', 0)]")

        #temphumidBaro
        bytes_array = [0x10, 0x54, 0x01, 0x03, 0x2F, 0x00, 0x00, 0xF7, 0x00, 0x20, 0x00, 0x24, 0x81, 0x60, 0x82, 0x50, 0x59]
        event = self.core.transport.parse(bytes_array)
        self.assertEquals(RFXtrx.SensorEvent, type(event))
        self.assertEquals(event.__str__(),"<class 'RFXtrx.SensorEvent'> device=[<class 'RFXtrx.RFXtrxDevice'> type='BTHR918' id='2f:00'] values=[('Barometer', 36), ('Battery numeric', 0), ('Forecast', 'unknown forecast'), ('Forecast numeric', 129), ('Humidity', 0), ('Humidity status', 'unknown humidity'), ('Humidity status numeric', 32), ('Rssi numeric', 6), ('Temperature', 24.7)]")

        #temphumidBaro, too short package length
        bytes_array = [0x10, 0x54, 0x01, 0x03, 0x2F, 0x00, 0x00, 0xF7, 0x00, 0x20, 0x00, 0x24, 0x81, 0x60, 0x82, 0x50]
        event = self.core.transport.parse(bytes_array)
        self.assertEquals(None, event)



    def test_equal_check(self):
        data1 = bytearray(b'\x11\x5A\x01\x00\x2E\xB2\x03\x00\x00'
                          b'\x02\xB4\x00\x00\x0C\x46\xA8\x11\x69')
        energy = RFXtrx.lowlevel.parse(data1)


        data2 = bytearray(b'\x0A\x14\x00\xAD\xF3\x94\xAB'
                          b'\x01\x01\x00\x60')
        light = RFXtrx.lowlevel.parse(data2)
        light2 = RFXtrx.lowlevel.parse(data2)

        data3 = bytearray(b'\x0A\x52\x02\x11\x70\x02\x00\xA7'
                         b'\x2D\x00\x89')
        temphum = RFXtrx.lowlevel.parse(data3)

        self.assertTrue(light==light2)
        self.assertFalse(light==energy)
        self.assertFalse(temphum==energy)

    def test_equal_device_check(self):
        data1 = bytearray(b'\x11\x5A\x01\x00\x2E\xB2\x03\x00\x00'
                          b'\x02\xB4\x00\x00\x0C\x46\xA8\x11\x69')
        energy = self.core.transport.receive(data1)


        data2 = bytearray(b'\x0A\x14\x00\xAD\xF3\x94\xAB'
                          b'\x01\x01\x00\x60')
        light = self.core.transport.receive(data2)
        light2 = self.core.transport.receive(data2)

        data3 = bytearray(b'\x0A\x52\x02\x11\x70\x02\x00\xA7'
                         b'\x2D\x00\x89')
        temphum = self.core.transport.receive(data3)

        bytes_array = bytearray(b'\x0A\x14\x00\xAD\xF3\x94\xAB\x01\x10\x00\x60')
        lighting5_subtype0 = self.core.transport.receive(bytes_array)

        bytes_array = bytearray(b'\x0A\x14\x01\xAD\xF3\x94\xAB\x01\x10\x00\x60')
        lighting5_subtype1 = self.core.transport.receive(bytes_array)

        self.assertFalse(light==light2)
        self.assertFalse(light==energy)
        self.assertFalse(temphum==energy)

        self.assertTrue(light.device==light2.device)
        self.assertFalse(light.device==energy.device)
        self.assertFalse(temphum.device==energy.device)

        self.assertFalse(lighting5_subtype0.device==lighting5_subtype1.device)

    def test_get_device(self):
        # Lighting1
        bytes_array = bytearray([0x07, 0x10, 0x00, 0x2a, 0x45, 0x05, 0x01, 0x70])
        event = self.core.transport.parse(bytes_array)
        device = RFXtrx.get_device(event.device.packettype, event.device.subtype, event.device.id_string)
        self.assertTrue(device==event.device)

        # Lighting2
        bytes_array =[0x0b, 0x11, 0x00, 0x2a, 0x01, 0x23, 0x45, 0x67, 0x05, 0x02, 0x07, 0x70]
        event = self.core.transport.parse(bytes_array)
        device = RFXtrx.get_device(event.device.packettype, event.device.subtype, event.device.id_string)
        self.assertTrue(device==event.device)

        # Lighting3
        bytes_array = [0x08, 0x12, 0x00, 0x2a, 0x01, 0x34, 0x02, 0x15, 0x79]
        event = self.core.transport.parse(bytes_array)
        device = RFXtrx.get_device(event.device.packettype, event.device.subtype, event.device.id_string)
        self.assertTrue(device==event.device)

        # Lighting5
        bytes_array = bytearray(b'\x0A\x14\x00\xAD\xF3\x94\xAB'
                              b'\x01\x01\x00\x60')
        event = self.core.transport.parse(bytes_array)
        device = RFXtrx.get_device(event.device.packettype, event.device.subtype, event.device.id_string)
        self.assertTrue(device==event.device)

        #Lighting 6
        bytes_array = [0x0b, 0x15, 0x00, 0x2a, 0x12, 0x34, 0x41, 0x05, 0x03, 0x01, 0x00, 0x70]
        event = self.core.transport.parse(bytes_array)
        device = RFXtrx.get_device(event.device.packettype, event.device.subtype, event.device.id_string)
        self.assertTrue(device==event.device)

        #energy sensor
        bytes_array = bytearray(b'\x11\x5A\x01\x00\x2E\xB2\x03\x00\x00'
                          b'\x02\xB4\x00\x00\x0C\x46\xA8\x11\x69')
        event = self.core.transport.parse(bytes_array)
        self.assertRaises(ValueError, RFXtrx.get_device,event.device.packettype, event.device.subtype, event.device.id_string)

    def test_receive(self):
        # Lighting1
        bytes_array = bytearray([0x07, 0x10, 0x00, 0x2a, 0x45, 0x05, 0x01, 0x70])
        event= self.core.transport.receive(bytes_array)
        self.assertEquals(RFXtrx.ControlEvent, type(event))

        self.assertEquals(event.__str__(),"<class 'RFXtrx.ControlEvent'> device=[<class 'RFXtrx.LightingDevice'> type='X10 lighting' id='E5'] values=[('Command', 'On'), ('Rssi numeric', 7)]")

        #status
        bytes_array = bytearray(b'\x0D\x01\x00\x01\x02\x53\x45\x00\x0C'
                                b'\x2F\x01\x01\x00\x00')
        event= self.core.transport.receive(bytes_array)
        self.assertEquals(RFXtrx.StatusEvent, type(event))
        self.assertEquals(event.__str__(),"<class 'RFXtrx.StatusEvent'> device=[Status [subtype=433.92MHz, firmware=69, devices=['ac', 'arc', 'hideki', 'homeeasy', 'lacrosse', 'oregon', 'x10']]]")
