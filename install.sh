#!/bin/bash

cat >> ~/.bash_profile <<EOF
fancycd() {
    cd "\$(python $(pwd)/fancycd.py "\$*")"
}
EOF
echo 'alias cd="fancycd"' >> ~/.bash_profile
bash
