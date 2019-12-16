#!/bin/bash

cat >> ~/.bash_profile <<'EOF'
fancycd() {
    cd "$(python ~/Documents/fancy-cd/fancycd.py "$*")"
}
EOF
echo 'alias cd="fancycd"' >> ~/.bash_profile
bash
