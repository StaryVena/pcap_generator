#!/bin/bash

mkdir -p ~/.pandoc/templates
cp pcap_template.latex ~/.pandoc/templates/pcap_template.latex

mkdir -p pdf

pandoc -s README.md --template pcap_template -o pdf/aa.pdf

if [ $# -eq 1 ]; then
    for dir in scenarios/*/ ; do
        dir=${dir%*/}
        echo "$dir"
        pandoc -s ${dir}/README.md --template pcap_template -o pdf/${dir##*/}.pdf
    done
fi

pdfunite $(ls -v pdf/*.pdf) manual.pdf
rm -r pdf