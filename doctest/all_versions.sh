#!/bin/sh

python2.6 --version
python2.6 -m doctest -v doctest/lighting.txt | grep failed
python2.6 -m doctest -v doctest/lowlevel.txt | grep failed

python2.7 --version
python2.7 -m doctest -v doctest/lighting.txt | grep failed
python2.7 -m doctest -v doctest/lowlevel.txt | grep failed

python3.1 --version
python3.1 -m doctest -v doctest/lighting.txt | grep failed
python3.1 -m doctest -v doctest/lowlevel.txt | grep failed

python3.2 --version
python3.2 -m doctest -v doctest/lighting.txt | grep failed
python3.2 -m doctest -v doctest/lowlevel.txt | grep failed

python3.3 --version
python3.3 -m doctest -v doctest/lighting.txt | grep failed
python3.3 -m doctest -v doctest/lowlevel.txt | grep failed
