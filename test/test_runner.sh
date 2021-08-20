#!/usr/bin/env bash

cd `dirname $0`/..
ROOTDIR=`pwd`/src
export PYTHONPATH=${PYTHONPATH}:${ROOTDIR}
py.test
