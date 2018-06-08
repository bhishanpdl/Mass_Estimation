#!/bin/bash
#
# Author: Bhishan Poudel
# Date  : May 17, 2018
#====================================

function star_convolved_rescaled() {
    local star=star/star.fits # input
    local psf=psf/psf${1}_z${2}.fits # input

    local outdir=outputs/convolved${1} # created from another func
    local convolved_txt=outputs/convolved_bands${1}.txt
    local convolved_fits=$outdir/convolved_bands${1}.fits
    local convolved_rescaled=$outdir/star${1}_z${2}.fits


    # Debug
    # echo $psf
    # echo $convolved_rescaled
    # echo

    # convolve
    echo -e "\n Running jediconvolve ..."
    ./executables/jediconvolve $star $psf $outdir/ && # we need /

    # paste
    echo -e "\n Running jedipaste ..."
    ./executables/jedipaste 12288 12288  $convolved_txt  $convolved_fits &&

    # rescale
    echo -e "\n Running jedirescale ..."
    ./executables/jedirescale $convolved_fits 0.06 0.2 480 480 $convolved_rescaled &&

    echo "jedirescale finished."
}




## Create two text files NOTE: 'EOF' will not read $variable values.
function input_conv_txt() {

# create outdir
mkdir -p outputs/convolvedb
mkdir -p outputs/convolvedd
mkdir -p outputs/convolvedm

# bulge
cat << 'EOF' > outputs/convolved_bandsb.txt
outputs/convolvedb/convolved_band_1.fits
outputs/convolvedb/convolved_band_2.fits
outputs/convolvedb/convolved_band_0.fits
outputs/convolvedb/convolved_band_3.fits
outputs/convolvedb/convolved_band_4.fits
outputs/convolvedb/convolved_band_5.fits
EOF

# disk
cat << 'EOF' > outputs/convolved_bandsd.txt
outputs/convolvedd/convolved_band_1.fits
outputs/convolvedd/convolved_band_2.fits
outputs/convolvedd/convolved_band_0.fits
outputs/convolvedd/convolved_band_3.fits
outputs/convolvedd/convolved_band_4.fits
outputs/convolvedd/convolved_band_5.fits
EOF


# mono
cat << 'EOF' > outputs/convolved_bandsm.txt
outputs/convolvedm/convolved_band_1.fits
outputs/convolvedm/convolved_band_2.fits
outputs/convolvedm/convolved_band_0.fits
outputs/convolvedm/convolved_band_3.fits
outputs/convolvedm/convolved_band_4.fits
outputs/convolvedm/convolved_band_5.fits
EOF
}


# Now run the commands
z=1.0
input_conv_txt &&
star_convolved_rescaled 'b' $z &&
star_convolved_rescaled 'd' $z &&
star_convolved_rescaled 'm' $z &&

echo "Success!"


# Command: bash convolveRescale.sh
