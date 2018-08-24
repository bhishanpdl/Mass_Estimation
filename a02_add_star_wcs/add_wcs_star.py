#!python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : July 26, 2017
# Last update : July 1, 2018
# Imports
from __future__ import print_function, unicode_literals, division, absolute_import, with_statement
import glob
import os
import sys
import numpy as np
from astropy.io import fits
from astropy import wcs

def add_wcs(field):
    # Read field
    field = str(field)
    field_hdu = fits.open(field)

    # Get fake wcs from astropy
    w = wcs.WCS(naxis=2)
    w.wcs.crpix = [1800.0, 1800.0]
    w.wcs.crval = [0.1, 0.1]
    w.wcs.cdelt = np.array([-5.55555555555556E-05,5.55555555555556E-05])
    w.wcs.ctype = ["RA---TAN", "DEC--TAN"]
    wcs_hdr = w.to_header()

    # Add fake wcs to header of output file
    hdr = field_hdu[0].header
    hdr += wcs_hdr

    # Write output file
    field_hdu.writeto(field,clobber=True)
    field_hdu.close()

    # Print
    print('Fake WCS added to the galaxy field: {}'.format(field))

def main():
    """Run main function."""
    z = float(sys.argv[1])
    idir = sys.argv[2]
    nstar = sys.argv[3]
    starval = sys.argv[4]

    mono = ['lsst_mono','lsst_mono90']
    chro = ['lsst','lsst90']

    mono = ['{}/{}/'.format(idir,f) for f in mono]
    chro = ['{}/{}/'.format(idir,f) for f in chro]

    # star data
    # stars_z0.7_100_50000/starb_z0.7_100_50000.fits
    dat_stars =  [fits.getdata('stars_z{z}_{nstar}_{starval}/star{i}_z{z}_{nstar}_{starval}.fits'.format(
                 z=z,nstar=nstar,starval=starval,i=i)) for i in list('bdm')]

    # create output dirs
    wcsstr = 'wcs_star_{}_{}_'.format(nstar,starval)
    odirs = ['{}{}'.format(wcsstr,o) for o in mono+chro]
    for o in odirs:
        if not os.path.isdir(o):
            os.makedirs(o)

    # mono and mono90 dir
    for m in mono:
        for f in glob.glob('{}/*.fits'.format(m)):
            datm,hdr = fits.getdata(f,header=True)
            hdr['REDSHIFT'] = z
            hdr['EXPTIME'] = 6000 # from jedisim config file
            hdr['NGALS'] = (20000, 'jedisim simulation galaxies')
            hdr['Z-LENS']= (0.3, 'redshift of lens')
            hdr['sim-pix'] = (0.06, 'simulation pix scale of HST')
            hdr['f-pix'] = (0.2 , 'final pixscale of LSST in jedisim')

            odat = datm + dat_stars[2] # mono + starm
            head, tail = os.path.split(f)
            ofile = wcsstr + head + '/' + tail
            #print('\nWriting: ', ofile)
            fits.writeto(ofile,odat,header=hdr,clobber=True)
            add_wcs(ofile)

    # chro and chro90 dir
    for c in chro:
        for f in glob.glob('{}/*.fits'.format(c)):
            datc, hdr = fits.getdata(f, header=True)
            hdr['REDSHIFT'] = z
            hdr['EXPTIME'] = 6000 # from jedisim config file
            hdr['NGALS'] = (20000, 'jedisim simulation galaxies')
            hdr['Z-LENS']= (0.3, 'redshift of lens')
            hdr['sim-pix'] = (0.06, 'simulation pix scale of HST')
            hdr['f-pix'] = (0.2 , 'final pixscale of LSST in jedisim')
            odat = datc + dat_stars[0] + dat_stars[1] # chro + starb + stard
            head, tail = os.path.split(f)
            ofile = wcsstr + head + '/' + tail
            #print('\nWriting: ', ofile)
            fits.writeto(ofile,odat,header=hdr,clobber=True)
            add_wcs(ofile)


if __name__ == "__main__":
    main()

# Note: 1. idir must have lsst,lsst90,lsst_mono and lsst_mono90 dir.
#       2.  stars_z{z}_{nstar}_{starval}/star{b,d,m}_z{z}_{nstar}_{starval}.fits
#           eg: stars_z0.7_100_100000/starb_z0.7_100_100000.fits
#
#                                 z   idir            nstar starval
# Command: python add_wcs_star.py 0.7 jout_z0.7_000_099 100 100000 
#
# Outputs: wcs_star_$idir   with star and wcs added to input fitsfiles.
