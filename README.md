========
pyRFXtrx
========

A Python library to communicate with the RFXtrx family of devices
from http://www.rfxcom.com/

See https://github.com/woudt/pyRFXtrx for the latest version.


Using
=====

Install pySerial first::
	$ sudo easy_install -U pyserial


After that, see the examples in the examples directory


Developers
==========

To run the test scripts::
	$ ./test_run.sh

To run the test scripts for all supported Python versions (requires a proper
environment, with all Python versions (2.6, 2.7, 3.1, 3.2 and 3.3) installed)::
	$ doctest/all_versions.sh

Run pylint and pep8 checks on the source code:
	$ sudo easy_install -U pep8 logilab-common logilab-astng pylint
	$ ./lint_run.sh


Licensing
=========

Copyright (C) 2012  Edwin Woudt <edwin@woudt.nl>

pyRFXtrx is free software: you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyRFXtrx is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pyRFXtrx.  See the file COPYING.txt in the distribution.
If not, see <http://www.gnu.org/licenses/>.
