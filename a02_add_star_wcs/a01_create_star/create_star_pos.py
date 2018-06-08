#!python
# -*- coding: utf-8 -*-#
"""
Create star position csv file.

Author : Bhishan Poudel
Date   : May 17, 2018
"""
# Imports
import numpy as np
np.random.seed(100)

# We do it just want, do not call this function from jedisim scripts.
def create_stars_positions(n_stars,star_value, star_positions):
    # Get values
    n_stars = int(n_stars)
    # NAXIS1 = fits.getheader(field)['NAXIS1'] # 12288
    # NAXIS2 = fits.getheader(field)['NAXIS2'] # 12288
    NAXIS1 = 12288
    NAXIS2 = 12288

    # Do not put stars on boundaries
    offset = int(NAXIS1*0.1)

    # Randomly put stars
    with open(star_positions,'w') as fo:
      for i in range(0,n_stars):
          x = np.random.randint(offset, NAXIS1-offset)
          y = np.random.randint(offset, NAXIS2-offset)
          out = '{} {}\n'.format(x,y)
          fo.write(out)

def main():
    n_stars = 100
    star_value = 20
    star_positions = 'star_positions.csv'
    create_stars_positions(n_stars,star_value, star_positions)

if __name__ == '__main__':
    main()
