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

# fancy-cd

fancy-cd is a fancy version of the default Bash cd command that allows you to jump to previously visited directories. Specifically, it caches previously visited directories, ranked by frequency of use, and if a directory is not found in the current directory when using the `cd` command, you can instead jump to a previously visited directory with the same name.

## Installation

Run the following commands to install this utility. You can also use the `install.sh` script. This will override the default cd command with this script. You can uninstall by removing the added lines from your `.bash_profile`. 

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

## Examples

Simple caching of past directories

```
username@:~$ cd Documents
username@:~/Documents$ cd ..
username@:~$ cd Desktop
username@:~/Desktop$ cd Documents
username@:~/Documents$
```

No need to escape directories with spaces

```
username@~$ cd dir1/dir2/Fun Stuff/December 2019
username@~/dir1/dir2/Fun Stuff/December 2019$ 
```

Conflicts are resolved by frequency of access

```
username@:~$ cd Documents
username@:~/Documents$ cd ..
username@:~$ cd Documents
username@:~/Documents$ cd ..
username@:~$ cd Desktop/Documents
username@:~/Desktop/Documents$ cd ~/Downloads
username@:~$ cd Documents
username@:~/Documents$ cd ..
```

