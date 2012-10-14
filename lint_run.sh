#!/bin/sh

pylint -d W0105 -d R0902 -d R0903 -d R0911 -d R0913 RFXtrx

pep8 --count --statistics -v RFXtrx/
