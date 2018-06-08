#!python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : July 26, 2017
# Last update :
#
# Imports
from __future__ import print_function, unicode_literals, division, absolute_import, with_statement
from astropy.cosmology import FlatLambdaCDM
import glob
import os
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
    field_hdu.writeto(field,overwrite=True)
    field_hdu.close()

    # Print
    print('Fake WCS added to the galaxy field: {}'.format(field))

def main():
    """Run main function."""
    z = 1.0
    idir = 'jout_z1.0'

    mono = ['lsst_mono','lsst_mono90']
    chro = ['lsst','lsst90']

    mono = ['{}/{}/'.format(idir,f) for f in mono]
    chro = ['{}/{}/'.format(idir,f) for f in chro]

    # star data
    dat_stars = [fits.getdata('stars_z{}/star{}_z{}.fits'.format(z,i,z)) for i in list('bdm')]

    # create output dirs
    odirs = ['wcs_star_{}'.format(o) for o in mono+chro]
    for o in odirs:
        if not os.path.isdir(o):
            os.makedirs(o)

    # mono
    for m in mono:
        for f in glob.glob('{}/*.fits'.format(m)):
            datm = fits.getdata(f)
            odat = datm + dat_stars[2] # mono + starm
            head, tail = os.path.split(f)
            ofile = 'wcs_star_' + head + '/' + tail
            print('\nWriting: ', ofile)
            fits.writeto(ofile,odat,overwrite=True)
            add_wcs(ofile)

    # chro
    for c in chro:
        for f in glob.glob('{}/*.fits'.format(c)):
            datc = fits.getdata(f)
            odat = datc + dat_stars[0] + dat_stars[1] # chro + starb + stard
            head, tail = os.path.split(f)
            ofile = 'wcs_star_' + head + '/' + tail
            print('\nWriting: ', ofile)
            fits.writeto(ofile,odat,overwrite=True)
            add_wcs(ofile)


if __name__ == "__main__":
    main()
