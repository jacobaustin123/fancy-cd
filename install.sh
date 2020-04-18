#!/bin/bash

git clone https://github.com/jacobaustin123/fancy-cd.git ~/Documents/fancy-cd/
cat >> ~/.bash_profile <<'EOF'
fancycd() {
    cd "$(python ~/Documents/fancy-cd/fancycd.py "$*")"
}
EOF
echo 'alias cd="fancycd"' >> ~/.bash_profile
bash
