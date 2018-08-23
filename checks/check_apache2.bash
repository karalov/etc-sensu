#!/bin/bash
num=`ps -ef | grep apache2 | grep root | wc -l`
if [[  $num -ne 1 ]]
then
  echo "CRITICAL FAILURE! Apache2 server is down"
  exit 2
else
  echo "OK. Apache2 is up and running"
  exit 0
 fi