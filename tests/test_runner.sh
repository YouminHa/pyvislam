#!/usr/bin/env bash

cd `dirname $0`/..
ROOTDIR=`pwd`
export PYTHONPATH=${PYTHONPATH}:${ROOTDIR}
py.test
