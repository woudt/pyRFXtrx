import time
from threading import Thread
from RFXtrx.pyserial import PySerialTransport
from RFXtrx import SensorEvent

class Core(object):
    """The main class for rfxcom-py.
    Has methods for sensors. 
    """

    def __init__(self, device, protocols=None, debug=True):
        """Create a new RfxtrxCore instance. """
    
        self._sensors = {}
  
        thread = Thread(target = self._connect, args = (device, debug) )
        thread.start()
        

    def _connect(self, device, debug):
        self.transport = PySerialTransport(device, debug)
        self.transport.reset()
        while True:
            print("fasf")
            event = self.transport.receive_blocking()
            print(event)
            if isinstance(event, SensorEvent):
                self._sensors[event.device.id_string] = event.device
 
    def sensors(self):
        """Return all found sensors.
        :return: dict of :class:`Sensor` instances.
        """
        return self._sensors


