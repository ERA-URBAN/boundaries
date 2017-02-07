#!/usr/bin/env python2

'''
Description:    Download ECMWF ERA-Interim grib data needed for WRF boundaries
Author:         Ronald van Haren, NLeSC (r.vanharen@esciencecenter.nl)
Created:        -
Last Modified:  -
License:        Apache 2.0
Notes:          -
'''

# import ecmwf api
from ecmwfapi import ECMWFDataServer
import argparse
import os

def define_pl_dict(date_string):
  ''' 
  define pressure level dictionary for ECMWFDataServer call
  '''
  pl = {
      'stream'    : "oper",
      'levtype'   : "pl",
      'levelist'  : "all",
      'param'     : "129/130/131/132/157",
      'dataset'   : "interim",
      'step'      : "0",
      'grid'      : "128",
      'time'      : "00/06/12/18",
      'date'      : date_string,
      'type'      : "an",
      'class'     : "ei",
      'target'    : "interim_pl.grib"
  }
  return pl

def define_sfc_dict(date_string):
  ''' 
  define surface level dictionary for ECMWFDataServer call
  '''
  sfc = {
      'stream'    : "oper",
      'levtype'   : "sfc",
      'param'     : "172/134/151/165/166/167/168/235/33/34/31/141/139/170/183/236/39/40/41/42",
      'dataset'   : "interim",
      'step'      : "0",
      'grid'      : "128",
      'time'      : "00/06/12/18",
      'date'      : date_string,
      'type'      : "an",
      'class'     : "ei",
      'target'    : "interim_sfc.grib"
  }
  return sfc

def check_date(date_text):
  '''
  check if date has the required format YYYY-MM-DD
  and is in valid range
  '''
  import datetime
  try:
    datetime_object = datetime.datetime.strptime(date_text, '%Y-%m-%d')
  except ValueError:
    raise ValueError("Incorrect data format, should be YYYY-MM-DD")
  if not (datetime.datetime(1979,1,1) < datetime_object
          < datetime.datetime.now()):
    raise ValueError("Date must be between 1979-01-01 and now: " + date_text)
  return datetime_object

def move_downloaded_data(datadir, bdate):
  '''
  move downloaded files to data directory
  '''
  import shutil
  # create destination directory, remove existing one if needed
  try:
    os.makedirs(os.path.join(datadir,bdate))
  except OSError:  # directory exists
    shutil.rmtree(os.path.join(datadir,bdate))
    os.makedirs(os.path.join(datadir,bdate))
  # move files
  for file in ['interim_pl.grib', 'interim_sfc.grib']:
    try:
      shutil.move(file,os.path.join(datadir,bdate))
    except IOError:
      pass


def main(args):
  import re
  # define server
  server = ECMWFDataServer()

  if not True in [args.pl, args.sfc]:
    # add logging statement
    raise Exception('Nothing to do')

  dt1 = check_date(args.date)
  if args.date2:
    if not (check_date(args.date2) > dt1):
      raise ValueError('--date2 (' + args.date2 + ') must be after --date ('
                       + args.date + ').')
    else:
      date_string = args.date + '/to/' + args.date2
  else:
    date_string = args.date
  # define pressure and surface level dictionaries
  if args.pl:
    # define dictionary
    pl = define_pl_dict(date_string)
    # retrieve pressure level data
    server.retrieve(pl)

  if args.sfc:
    # define dictionary
    sfc = define_sfc_dict(date_string)
    # retrieve surface level data
    server.retrieve(sfc)
  
  # move downloaded data to data directory
  move_downloaded_data(args.datadir, re.sub('-','',args.date) + '00')

def str2bool(v):
  '''
  convert string to boolean
  '''
  return v.lower() in ("yes", "true", "t", "1")

if __name__=="__main__":
  # define argument parser
  parser = argparse.ArgumentParser(description='Download ERA-Interim fields (pl and sfc) to be used as WRF boundaries.')

  # optional arguments
  parser.add_argument('--pl', help='download pressure level fields [boolean, default: true]',
                      default=True, type=str2bool, required=False)
  parser.add_argument('--sfc', help='download surface level fields [boolean, default: true]',
                      default=True, type=str2bool, required=False)
  parser.add_argument('--date2', help='Optional second date YYYY-MM-DD. Data will be downloaded between --data and --data2 in used.', required=False, type=str)
  parser.add_argument('--datadir', help='destination directory [default: ' +
                      os.path.join(os.getcwd(),'ERAI') + ']',
                      default=os.path.join(os.getcwd(),'ERAI'), required=False)
  # required arguments
  req = parser.add_argument_group('required arguments')
  req.add_argument('--date', help='Date YYYY-MM-DD', required=True, type=str)

  # extract entered arguments
  args = parser.parse_args()
  
  # call main()
  main(args)
