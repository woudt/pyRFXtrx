#!/bin/sh

pylint -d W0105 RFXtrx

pep8 --count --statistics -v RFXtrx/
