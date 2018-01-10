#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import sys
import argparse

from sense_hat import SenseHat

def check_temperature(warn, crit):

    # Grab the temperature for the specified adapter by splitting the string
    # into a list and then getting the index number for the adapter name and
    # adding 5 to the index number.
    # Lastly, we strip away the + sign and the degree symbols and typecast it
    # to a float

    sense = SenseHat()
    temp = sense.get_temperature()
    
    #temp = 22
    
    # Print temperature and message and then exit with the correct return code
    if temp < warn:
        print ("OK - Temperature is " + str(temp))
        sys.exit(0)
    elif temp > warn and temp < crit:
        print ("WARNING - Temperature is " + str(temp))
        sys.exit(1)
    elif temp >= crit:
        print ("CRITICAL - Temperature is " + str(temp))
        sys.exit(2)
    else:
        print ("UNKNOWN - Something went wrong with " + sys.argv[0] + "!")
        sys.exit(3)
        
def check_humidity(warn, crit):

    sense = SenseHat()
    humidity = sense.get_humidity()
    
    #humidity = 22
    
    # Print temperature and message and then exit with the correct return code
    if temp < warn:
        print ("OK - Humidity is %s %%rH" % humidity)
        sys.exit(0)
    elif temp > warn and temp < crit:
        print ("WARNING - Humidity is %s %%rH" % humidity)
        sys.exit(1)
    elif temp >= crit:
        print ("CRITICAL - Humidity is %s %%rH" % humidity)
        sys.exit(2)
    else:
        print ("UNKNOWN - Something went wrong with " + sys.argv[0] + "!")
        sys.exit(3)

def main():
    
    # Parse command line options with argparse
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument('-m', metavar='N', type=str, required=True,
        help='check mode') 
    cli_parser.add_argument('-w', metavar='N', type=float, required=True,
        help='warning value')
    cli_parser.add_argument('-c', metavar='N', type=float, required=True,
        help='critical value')
    args = cli_parser.parse_args()

    if args.m == "temperature":
        check_temperature(args.w, args.c)
    elif args.m == "humidity":
        check_humidity(args.w, args.c)
    else:
        print "UNKNOWN"
        
if __name__=='__main__':
    main()