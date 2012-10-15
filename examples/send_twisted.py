# This file is part of pyRFXtrx, a Python library to communicate with
# the RFXtrx family of devices from http://www.rfxcom.com/
# See https://github.com/woudt/pyRFXtrx for the latest version.
#
# Copyright (C) 2012  Edwin Woudt <edwin@woudt.nl>
#
# pyRFXtrx is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyRFXtrx is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pyRFXtrx.  See the file COPYING.txt in the distribution.
# If not, see <http://www.gnu.org/licenses/>.

from twisted.internet import reactor
from RFXtrx.twistedserial import TwistedSerialTransport
from RFXtrx import LightingDevice

def receive(event):
    if event is not None and isinstance(event.device, LightingDevice):
        reactor.callLater(5, turnoff, event.device)

def turnoff(device):
    device.send_off(transport)

transport = TwistedSerialTransport('/dev/cu.usbserial-05VN8GHS', receive, debug=True)
reactor.run()
