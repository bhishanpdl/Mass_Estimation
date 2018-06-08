<!-- #===============================* -->
<!-- # Author  : Bhishan Poudel
<!-- # Date    : May 18, 2018
<!-- # Update  : June 5, 2018
<!-- #===============================* -->

# Create starc_z1.0.fits and starm_z1.0.fits
Jedisim gives chromatic and monochromatic fitsfiles without wcs and stars
added to it. The output from jedisim are lsst_z1.0_000.fits and lsst_mono_z1.0_000.fits.

While using DMstack for the mass estimation, the program processCcd.py needs
stars (psfs) added to the field. It also needs WCS added to the
fields. So we add stars and wcs to the output of jedisim.

Jedisim output : lsst_z1.0_000.fits
add starc_z1.0 : stars_wcs_lsst_z1.0_000.fits

Jedisim output : lsst_mono_z1.0_000.fits
add starm_z1.0 : stars_wcs_lsst_monoz1.0_000.fits


## Step 1: Create star.fits
To create star.fits first we create star_positions.csv file so that
all the stars are at given fixed points for all redshift images.
```
np.random.seed(100)
```

In our jedisim simulation HST files have NAXISn = 12288.
To make sure that there are no stars at border we create star positions
between offset to NAXIS1-offset where offset is 10 % of NAXISn.


In jedisim we convolve HST files (shape 12288,12288) with the psfm_z.fits
(shape 4000,4072 from Phosim) and get the LSST fitsfile (shape 3398,3398).

Similarly, here we create empty star.fits of shape 12288,12288 and then will
convolve it with the psf and get another shape.

```bash
shape of trial1_HST.fits = 12288,12288   (NOTE: 12228 = 12 * 1024)
shape of psfm.fits       = 4000,4072 (obtained from PHOSIM)
shape of lsst_mono       = 3398,3398
shape of star.fits       = 12288,12288
shape of starm_z1.0.fits = 3398,3398   (rescale decreases the size)

(12288-480)*0.06/0.2 = 3542.4
```

## Step 2: Create starb_z1.0.fits, stard_z1.0.fits, and starm_z1.0.fits
We convolve the star.fits with psfb or psfd or psfm and then rescale the file
to get rescaled convolved star file. We call it starb_z1.0.fits and so on.


## Step 3: Combine lsst_mono_z1.0_000.fits and starm_z1.0.fits and add wcs
While processing jedisim outputs with DMstack pipeline, the program
processCcd.py needs input fitsfile must have  PSFs and WCS.

We add the lsst files from jedisim with star and then add wcs information.

```
lsst_z1.0_000.fits  # output from jedisim
+ starb_z1.0.fits   # processCcd.py needs PSFs in the input fitsfile
+ stard_z1.0.fits   # processCcd.py needs PSFs in the input fitsfile
+ WCS               # processCcd.py needs WCS (ra and dec) in the input fitsfile
--------------------------------------------------------------------------------
= star_wcs_lsst_z1.0_000.fits
```

## Setp 4: Run mass estimation
After we get star_wcs_lsst files we can run DMstack pipeline to estimate
the mass of the field.
