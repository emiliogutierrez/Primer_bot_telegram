#    ! /usr/bin/bash


for i in {1..50000}
do
    echo "Sur"
    ./bajaimagenes.py http://contingencias.mendoza.gov.ar/radar/sur.php
    echo "Norte"
    ./bajaimagenes.py http://contingencias.mendoza.gov.ar/radar/norte.php
    echo "Ultima Imagen"
    ./bajaimagenes.py http://www.contingencias.mendoza.gov.ar/radar/latest.php
    echo "Centro"
    ./bajaimagenes.py http://contingencias.mendoza.gov.ar/radar/centro.php
    echo "Animacion"
    ./bajaimagenes.py http://www.contingencias.mendoza.gov.ar/radar/animacion.php
    echo "fin"
    date  '+%A %d-%m-%Y a las %R.-'  > ultimaactualizacion.txt
    sleep 10m
done
