#!python
# -*- coding: utf-8 -*-#
"""
Create convolved star fits files.

Author : Bhishan Poudel
Date   : May 10, 2018
"""
# Imports
import numpy as np
from astropy.io import fits

def create_fitsfile(star_positions,NAXISn,star_fits,star_value):
    # NOTE: from numpy to ds9 image: x,y ==> y+1, x+1
    # i.e. data[1][5] in numpy is ds9 image position 6,2.
    pos = np.genfromtxt(star_positions,dtype=int)
    data = np.zeros((NAXISn,NAXISn),dtype=np.float)
    for p in pos:
        i,j = p
        print(i,j)
        data[i,j] = star_value


    # write
    fits.writeto(star_fits,data)


def add_fits(in1,in2,out):
    data1, hdr1 = fits.getdata(in1, header=True)
    data2, hdr2 = fits.getdata(in2, header=True)
    fits.writeto(out,data1+data2, header=hdr1)

def main():
    """Run main function."""
    star_positions = 'star_positions.csv'
    star_fits = 'star.fits'
    star_value = 20.0
    NAXISn = 12288
    create_fitsfile(star_positions,NAXISn,star_fits,star_value)

if __name__ == "__main__":
    main()
