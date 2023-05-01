#!/usr/bin/env python
# coding: utf-8

import s3fs
import datetime
from pathlib import Path
import xarray as xr
import pandas as pd
import os

# Set the current working directory
directory_path = Path.cwd()
subdir = '/data/'

# Create a new directory because it does not exist
isExist = os.path.exists('data')
if not isExist:
   os.makedirs('data')

# Connect to the AWS S3 bucket
fs = s3fs.S3FileSystem(anon=True)

# Download GOES-16 datasets -----------------------------------------------
# SST
bucket = 'noaa-goes18'
year = 2023
month = 4
day = 22
julian = datetime.datetime(year, month, day).strftime('%j')
hour = '20'
product = 'ABI-L2-SSTF'
fname = 'OR_ABI-L2-SSTF-M6_G18_s20231122000211_e20231122059519_c20231122105091.nc'

files_path = bucket + '/' + product + '/'  + str(year) + '/' + julian + '/' + str(hour).zfill(2)
match = files_path + '/' + fname

fs.get(match, str(directory_path) + subdir + fname)

# RSR
bucket = 'noaa-goes16'
year = 2023
month = 4
day = 22
julian = datetime.datetime(year, month, day).strftime('%j')
hour = '18'
product = 'ABI-L2-RSRF'
fname = 'OR_ABI-L2-RSRF-M6_G16_s20231121800204_e20231121809512_c20231121859124.nc'

files_path = bucket + '/' + product + '/'  + str(year) + '/' + julian + '/' + str(hour).zfill(2)
match = files_path + '/' + fname

fs.get(match, str(directory_path) + subdir + fname)

# Download JPSS datasets -----------------------------------------------
# AOD 
# https://twitter.com/AerosolWatch/status/1650515430451060747
bucket = 'noaa-jpss'
satellite = 'NOAA20'
sensor = 'VIIRS'
product = 'NOAA20_VIIRS_Aerosol_Optical_Depth_EDR'
year = 2023
month = 4
day = 22
fname = 'JRR-AOD_v2r3_j01_s202304220518119_e202304220519346_c202304220600390.nc'

files_path = bucket + '/' + satellite + '/' + sensor + '/' + product + '/' + str(year) + '/' + str(month).zfill(2) + '/' + str(day).zfill(2)
match = files_path + '/' + fname

fs.get(match, str(directory_path) + subdir + fname)

# Active Fire
bucket = 'noaa-jpss'
satellite = 'NOAA20'
sensor = 'VIIRS'
product = 'NOAA20_VIIRS_AF_I-Band_EDR_NRT'
year = 2023
month = 4
day = 22
fname = 'AF-Iband_v1r1_j01_s202304220518119_e202304220519346_c202304220557358.nc'

files_path = bucket + '/' + satellite + '/' + sensor + '/' + product + '/' + str(year) + '/' + str(month).zfill(2)  + '/' + str(day).zfill(2)
match = files_path + '/' + fname

fs.get(match, str(directory_path) + subdir + fname)

# Reformat into a text document for learning purposes
# Contains groups
afi = xr.open_dataset('data/'+fname, group='Fire Pixels')

lats = afi.FP_latitude.values
lons = afi.FP_longitude.values
frp = afi.FP_power.values
brt = afi.FP_T4.values

data = { 'Lon' : lons, 'Lat' : lats, 'brt_I04(K)' : brt, 'frp(MW)' : frp }

df = pd.DataFrame(data=data)
df.to_csv('data/VIIRS_AF_j01_s202304220518119_e202304220519346.csv', index=False)

# VIIRS L1
bucket = 'noaa-nesdis-n20-pds'
product = 'VIIRS-M16-SDR'
year = 2023
month = 4
day = 22
fname = 'SVM16_j01_d20230422_t0516461_e0518106_b28103_c20230422055438143201_oeac_ops.h5'

files_path = bucket + '/' + product + '/' + str(year) + '/' + str(month).zfill(2)  + '/' + str(day).zfill(2)
match = files_path + '/' + fname

fs.get(match, str(directory_path) + subdir + fname)