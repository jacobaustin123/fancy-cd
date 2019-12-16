# fancy-cd

fancy-cd is a fancy version of the default Bash cd command that allows you to jump to previously visited directories. Specifically, it caches previously visited directories, ranked by frequency of use, and if a directory is not found in the current directory when using the `cd` command, you can instead jump to a previously visited directory with the same name.

## Installation

Run the following commands to install this utility

```
git clone https://github.com/ja3067/fancy-cd.git ~/Documents/fancy-cd/
cat >> ~/.bash_profile <<'EOF'
fancycd() {
    cd "$(python ~/Documents/fancy-cd/fancycd.py "$*")"
}
EOF
echo 'alias cd="fancycd"' >> ~/.bash_profile
bash
```