# Jedisim
We run jedisim to get outputs lsst,lsst\_mono and thier 90 degree rotated versions.

# Add WCS and Stars
We add WCS and stars to the jedisim outputs using script `add_wcs_star.py`.
This needs `stars_z1.5_100_100000` directory with required stars.

# Get source catalog using **obs\_file**
We run the scripts from  **obs\_file** module to get the source catalog and KSB parameters.
The obs_file module gives a fits table with many parameters we can convert this table to csv file 
or hdf5 format. The `hdf5` format is later needed by `Clusters` module.

# Get the mass estimation
We use **Clusters** module to get the maximum likelihood of the given galaxy field.
The process of getting catalog and estimation can be done using following commands:
```
cd wcs_star_added_directory_having_lsst_etc.
cpdm # copy my local scripts to pwd
lsst # go to lsst env
obs # activate obs_file module
# Now we can run four commands simultaneously in four different terminals.
python aa_run_dmstack.py -z 0.7 -f lsst > /dev/null 2>&1 
python aa_run_dmstack.py -z 0.7 -f lsst90 > /dev/null 2>&1
python aa_run_dmstack.py -z 0.7 -f lsst_mono > /dev/null 2>&1
python aa_run_dmstack.py -z 0.7 -f lsst_mono90 > /dev/null 2>&1
```

# The parameters in source catalog
```   
id (0)                                       coord_ra (1)                                 coord_dec (2)
parent (3)                                   deblend_nChild  (4)                          deblend_psfCenter_x (5)
deblend_psfCenter_y (6)                      deblend_psfFlux (7)                          base_GaussianCentroid_x (8)
base_GaussianCentroid_y (9)                  base_NaiveCentroid_x  (10)                   base_NaiveCentroid_y (11)


base_SdssCentroid_x (12)                     base_SdssCentroid_y (13)                     base_SdssCentroid_xSigma (14)
base_SdssCentroid_ySigma (15)                base_SdssShape_xx (16)                       base_SdssShape_yy (17)
base_SdssShape_xy  (18)                      base_SdssShape_xxSigma (19)                  base_SdssShape_yySigma (20)
base_SdssShape_xySigma (21)                  base_SdssShape_x (22)                        base_SdssShape_y (23)
base_SdssShape_flux  (24)                    base_SdssShape_fluxSigma (25)                base_SdssShape_psf_xx (26)
base_SdssShape_psf_yy (27)                   base_SdssShape_psf_xy (28)                   base_SdssShape_flux_xx_Cov (29)
base_SdssShape_flux_yy_Cov (30)              base_SdssShape_flux_xy_Cov  (31)             ext_shapeHSM_HsmPsfMoments_x (32)


ext_shapeHSM_HsmPsfMoments_y(33)           ext_shapeHSM_HsmPsfMoments_xx (34)          ext_shapeHSM_HsmPsfMoments_yy (35)
ext_shapeHSM_HsmPsfMoments_xy(36)          ext_shapeHSM_HsmShapeRegauss_e1 (37)        ext_shapeHSM_HsmShapeRegauss_e2 (38)
ext_shapeHSM_HsmShapeRegauss_sigma(39)     ext_shapeHSM_HsmShapeRegauss_resolution(40) ext_shapeHSM_HsmSourceMoments_x (41)
ext_shapeHSM_HsmSourceMoments_y(42)        ext_shapeHSM_HsmSourceMoments_xx(43)        ext_shapeHSM_HsmSourceMoments_yy (44)
ext_shapeHSM_HsmSourceMoments_xy (45)          


base_CircularApertureFlux_3_0_flux (46)      base_CircularApertureFlux_3_0_fluxSigma (47) 
base_CircularApertureFlux_4_5_flux (48)      base_CircularApertureFlux_4_5_fluxSigma (49) 
base_CircularApertureFlux_6_0_flux (50)      base_CircularApertureFlux_6_0_fluxSigma (51)
base_CircularApertureFlux_9_0_flux (52)      base_CircularApertureFlux_9_0_fluxSigma (53)
base_CircularApertureFlux_12_0_flux (54)     base_CircularApertureFlux_12_0_fluxSigma (55)
base_CircularApertureFlux_17_0_flux (56)     base_CircularApertureFlux_17_0_fluxSigma (57)
base_CircularApertureFlux_25_0_flux (58)     base_CircularApertureFlux_25_0_fluxSigma (59) 
base_CircularApertureFlux_35_0_flux (60)     base_CircularApertureFlux_35_0_fluxSigma (61)
base_CircularApertureFlux_50_0_flux  (62)    base_CircularApertureFlux_50_0_fluxSigma (63)
base_CircularApertureFlux_70_0_flux (64)     base_CircularApertureFlux_70_0_fluxSigma (65)


base_GaussianFlux_flux (66)                  base_GaussianFlux_fluxSigma (67)
base_PsfFlux_flux (68)                       base_PsfFlux_fluxSigma (69)
base_Variance_value (70)                     base_PsfFlux_apCorr (71)
base_PsfFlux_apCorrSigma (72)                base_GaussianFlux_apCorr (73)
base_GaussianFlux_apCorrSigma (74)           base_ClassificationExtendedness_value (75)
footprint (76)
```
