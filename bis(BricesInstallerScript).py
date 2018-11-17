# MIT LICENSE
# Copyright (c) 2018 Brice Vadnais

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# This is an installer script for the fresh install of an ubuntu based distro

from subprocess import *
import os
import sys

############################################################################################################

print("----------------------------------------------------------------------------")
print("--------------------------Brices Installer Script---------------------------")
print("----------------------------------------------------------------------------")

print("Updating & Upgrading the System...")
up_proc = Popen('sudo apt update && upgrade -y', shell=True)
up_proc.wait()
up_proc1 = Popen('sudo apt dist-upgrade -y', shell=True)
up_proc1.wait()
up_proc2 = Popen('sudo apt autoremove -y', shell=True)
up_proc2.wait()


############################################################################################################

def plank_autostart():
    home = os.environ["HOME"]
    launcher = ["[Desktop Entry]", "Name=Plank", "Exec=plank &",
                "Type=Application", "X-GNOME-Autostart-enabled=true"]
    dr = home+"/.config/autostart/"
    if not os.path.exists(dr):
        os.makedirs(dr)
    file = dr+"Plank".lower()+".desktop"

    if not os.path.exists(file):
        with open(file, "wt") as out:
            for l in launcher:
                out.write(l+"\n")
    else:
        print("file exists, choose another name")


print("----------------------------------------------------------------------------")
app_in = input("Would you like to install apps? (y/N)\n")

if app_in == 'y':
    print("Installing apps...")
    install_app_proc = Popen('sudo apt install python python3 vlc clementine vim emacs geany mupdf evince plank thunderbird\
     firefox galculator aptitude synaptic neofetch virtualbox mutt cmus audacity ranger lynx bc dc sqlite3 ffmpeg -y', shell=True)
    install_app_proc.wait()
    plank_autostart()
    install_app_proc1 = Popen(
        'sudo add-apt-repository ppa:twodopeshaggy/jarun -y', shell=True)
    install_app_proc1.wait()
    install_app_proc2 = Popen(
        'sudo apt update && sudo apt install nnn -y', shell=True)
    install_app_proc2.wait()
else:
    print("Skipping apps...")


############################################################################################################


print("----------------------------------------------------------------------------")
tools_in = input("Would you like to install all tools and toolchains? (y/N)\n(clang, git, hg, gcc, coreutils, binutils, pry, htop, sed , awk, fzf, tmux, \
youtube-dl, powertop, tlp, ncdu, albert, npm, pip, gem, gdb, lldb, curl, wget)\n")

if tools_in == 'y':
    print("Installing tools and toolchains...")
    install_app_proc = Popen(
        'sudo apt install npm curl wget lldb ffmpeg gdb gem powertop tlp coreutils binutils gcc clang git sed gawk htop tmux pry ncdu python2.7-dev python3.6-dev -y', shell=True)
    install_app_proc.wait()
    print("Installing pip...")
    install_pip_proc = Popen('cd ~', shell=True)
    install_pip_proc.wait()
    install_pip_proc1 = Popen(
        'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py', shell=True)
    install_pip_proc1.wait()
    install_pip_proc2 = Popen('python get-pip.py --user', shell=True)
    install_pip_proc2.wait()
    add_pip_path = Popen('export PATH=~/.local/bin:$PATH', shell=True)
    add_pip_path.wait()
    add_pip_path1 = Popen('source ~/.bashrc', shell=True)
    add_pip_path1.wait()
    print("Installing Mercurial...")
    install_hg_proc = Popen('cd ~', shell=True)
    install_hg_proc.wait()
    install_hg_proc1 = Popen('pip install Mercurial --user', shell=True)
    install_hg_proc1.wait()
    # install_fzf_proc = Popen('cd ~',shell=True)
    # install_fzf_proc.wait()
    # install_fzf_proc1 = Popen('mkdir ~/.fzf',shell=True)
    # install_fzf_proc1.wait()
    # install_fzf_proc2 = Popen('git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf')
    # install_fzf_proc2.wait()
    # install_fzf_proc3 = Popen('~/.fzf/install')
    # install_fzf_proc3.wait()
    print("Installing youtube-dl...")
    install_youtubedl_proc = Popen(
        'sudo pip install --upgrade youtube_dl', shell=True)
    install_youtubedl_proc.wait()
    print("Installing Albert Launcher...")
    install_albert_proc = Popen('cd ~', shell=True)
    install_albert_proc.wait()
    install_albert_proc1 = Popen(
        'wget -nv -O Release.key https://build.opensuse.org/projects/home:manuelschneid3r/public_key', shell=True)
    install_albert_proc1.wait()
    install_albert_proc2 = Popen(
        'sudo apt-key add - < Release.key', shell=True)
    install_albert_proc2.wait()
    install_albert_proc3 = Popen('sudo apt update', shell=True)
    install_albert_proc3.wait()
    install_albert_proc4 = Popen(
        'sudo sh -c \"echo \'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_18.04/ /\' > /etc/apt/sources.list.d/home:manuelschneid3r.list\"', shell=True)
    install_albert_proc4.wait()
    install_albert_proc5 = Popen('sudo apt update', shell=True)
    install_albert_proc5.wait()
    install_albert_proc6 = Popen('sudo apt install albert -y', shell=True)
    install_albert_proc6.wait()
else:
    print("Skipping tools and toolchains...")


############################################################################################################

print("----------------------------------------------------------------------------")
lang_in = input("Would you like to install all Languages ? (y/N)\n(Go, Rust, Swift, Crystal, Nim, Java, Kotlin, Clojure, Ruby, CommonLisp, Haskell, octave, Mono, NodeJS, Lua/LuaJIT)\n")

if lang_in == 'y':
    print("Installing languages...")
    install_langs_proc = Popen(
        'sudo apt install octave sbcl lua5.3 ghc ruby nim nodejs leiningen golang curl mono-devel -y', shell=True)
    install_langs_proc.wait()
    print("Installing Rust...")
    install_rust_proc = Popen(
        'curl https://sh.rustup.rs -sSf | sh', shell=True)
    install_rust_proc.communicate(input='\n')
    install_rust_proc.wait()
    print("Installing Crystal...")
    install_crystal_proc = Popen(
        'curl -sSL https://dist.crystal-lang.org/apt/setup.sh', shell=True)
    install_crystal_proc.wait()
    install_crystal_proc1 = Popen('sudo apt install crystal -y', shell=True)
    install_crystal_proc1.wait()
    # Libraries for crystal and one for swift
    install_crystal_proc2 = Popen(
        'sudo apt install libssl-dev libxml2-dev libyaml-dev libgmp-dev libreadline-dev libicu-dev -y ', shell=True)
    install_crystal_proc2.wait()
    install_swift_proc = Popen('sudo apt install ubuntu-make -y', shell=True)
    install_swift_proc.wait()
    print("Installing swift...")
    install_swift_proc1 = Popen('umake swift', shell=True)
    install_swift_proc1.wait()
    print("Installing kotlin...")
    install_kotlin_proc = Popen('umake kotlin kotlin-lang', shell=True)
    install_kotlin_proc.wait()
#     print("Installing maven...")
#     install_maven_proc = Popen('umake maven maven-lang', shell=True)
#     install_maven_proc.wait()
# else:
    print("Skipping languages...")


############################################################################################################

print("----------------------------------------------------------------------------")
txtide_in = input("Would you like to install text editors and ides? (y/N)\n")

if txtide_in == 'y':
    print("Installing text editors and ides...")
    # Install Portacle, Nightcode, Vscode, Sublime Text, pycharm, intellij, netbeans, codeblocks, Lighttable, neovim, spacemacs, redcar for ruby, glade, qtcreator
    install_apps_proc = Popen(
        'sudo apt install glade qtcreator codeblocks neovim python-neovim python3-neovim libgconf2-4 -y', shell=True)
    install_apps_proc.wait()
    make_idedir = Popen('cd ~', shell=True)
    make_idedir.wait()
    make_idedir1 = Popen('mkdir ides', shell=True)
    make_idedir1.wait()
    make_idedir2 = Popen('cd ~/ides', shell=True)
    make_idedir2.wait()
    print("Installing portacle...")
    install_portacle_proc = Popen(
        'wget https://github.com/portacle/portacle/releases/download/1.2b/lin-portacle.tar.xz', shell=True)
    install_portacle_proc.wait()
    install_portacle_proc1 = Popen('tar -xvzf lin-portacle.tar.xz', shell=True)
    install_portacle_proc1.wait()
    cleanup_portacle_install = Popen('rm -rf lin-portacle.tar.xz', shell=True)
    cleanup_portacle_install.wait()
    change_to_idedir = Popen('cd ~/ides', shell=True)
    change_to_idedir.wait()
    print("Installing Nightcode...")
    install_nightcode_proc = Popen(
        'wget https://github.com/oakes/Nightcode/releases/download/2.6.0/Nightcode-2.6.0.deb', shell=True)
    install_nightcode_proc.wait()
    install_nightcode_proc1 = Popen('dpkg -i Nightcode-2.6.0.deb', shell=True)
    install_nightcode_proc1.wait()
    print("Installing Sublime Text and Merge...")
    install_st_proc = Popen(
        'wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -', shell=True)
    install_st_proc.wait()
    install_st_proc1 = Popen(
        'sudo apt install apt-transport-https -y', shell=True)
    install_st_proc1.wait()
    install_st_proc2 = Popen(
        'echo \"deb https://download.sublimetext.com/ apt/stable/\" | sudo tee /etc/apt/sources.list.d/sublime-text.list', shell=True)
    install_st_proc2.wait()
    install_st_proc3 = Popen('sudo apt update', shell=True)
    install_st_proc3.wait()
    install_st_proc4 = Popen(
        'sudo apt install sublime-text sublime-merge -y', shell=True)
    install_st_proc4.wait()
    # print("Installing android studio...")
    # install_android_proc = Popen('umake android', shell=True)
    # install_android_proc.wait()
    print("Installing pycharm...")
    install_pycharm_proc = Popen('umake ide pycharm', shell=True)
    install_pycharm_proc.communicate(input='\n')
    install_pycharm_proc.wait()
    print("Installing intellij idea...")
    install_idea_proc = Popen('umake ide idea', shell=True)
    install_idea_proc.communicate(input='\n')
    install_idea_proc.wait()
    print("Installing lighttable...")
    install_lighttable_proc = Popen('umake ide lighttable', shell=True)
    install_lighttable_proc.communicate(input='\n')
    install_lighttable_proc.wait()
    print("Installing netbeans...")
    install_netbeans_proc = Popen('umake ide netbeans', shell=True)
    install_netbeans_proc.communicate(input='\n')
    install_netbeans_proc.wait()
    print("Installing vscode...")
    install_vscode_proc = Popen('umake ide visual-studio-code', shell=True)
    install_vscode_proc.communicate(input='\n')
    install_vscode_proc.wait()
    print("Installing redcar for ruby...")
    install_redcar_proc = Popen('gem install redcar', shell=True)
    install_redcar_proc.wait()
    print("Installing Spacemacs...")
    install_spacemacs_proc = Popen(
        'git clone https://github.com/syl20bnr/spacemacs ~/.emacs.d', shell=True)
    install_spacemacs_proc.wait()
else:
    print("Skipping text editors and ides...")

############################################################################################################

print("----------------------------------------------------------------------------")
improve_look_in = input("Would you like to update the look? (y/N)\n")
# Installing Vimix and Updating Plank Theme...\nAdding Plank to start up...\n")

if improve_look_in == 'y':
    print("Installing vimix and antishade themes...")
    install_antishade_proc = Popen(
        'git clone https://github.com/KenHarkey/plank-themes.git ~/.local/share/plank/themes', shell=True)
    install_antishade_proc.wait()
    install_vimix_proc = Popen(
        'sudo apt install gtk2-engines-murrine gtk2-engines-pixbuf -y', shell=True)
    install_vimix_proc.wait()
    install_vimix_proc1 = Popen(
        'git clone https://github.com/vinceliuice/vimix-gtk-themes.git ~/Downloads', shell=True)
    install_vimix_proc1.wait()
    install_vimix_proc2 = Popen(
        'sudo chmod +x ~/Downloads/vimix-gtk-themes/Install', shell=True)
    install_vimix_proc2.wait()
    install_vimix_proc3 = Popen(
        '~/Downloads/vimix-gtk-themes/Install', shell=True)
    install_vimix_proc3.wait()
    print("Installing papirus icons...")
    install_papirus_proc = Popen(
        'sudo add-apt-repository ppa:papirus/papirus -y', shell=True)
    install_papirus_proc.wait()
    install_papirus_proc1 = Popen('sudo apt update', shell=True)
    install_papirus_proc1.wait()
    install_papirus_proc2 = Popen(
        'sudo apt install papirus-icon-theme -y', shell=True)
    install_papirus_proc2.wait()
    print("Getting some backgrounds...")
    install_backgrounds_proc = Popen(
        'git clone https://github.com/elementary/wallpapers.git /usr/share/backgrounds', shell=True)
    install_backgrounds_proc.wait()
    install_backgrounds_proc1 = Popen(
        'git clone https://github.com/pop-os/wallpapers.git ~/Downloads', shell=True)
    install_backgrounds_proc1.wait()
    install_backgrounds_proc2 = Popen(
        'cp -r ~/Downloads/wallpapers/original /usr/share/backgrounds', shell=True)
    install_backgrounds_proc2.wait()
    cleanup_backgrounds_proc = Popen(
        'rm -rf ~/Downloads/wallpapers', shell=True)
    cleanup_backgrounds_proc.wait()
else:
    print("Skipping improving the look...")


############################################################################################################

print("----------------------------------------------------------------------------")
work_on_proj = input("Would you like to work on RISCV VM? (y/N)")

if work_on_proj == 'y':
    # git clone my directory and then maybe open it up in vscode or something
    print("Getting Project...")
    install_myproj_proc = Popen('mkdir ~/Documents/myprojects', shell=True)
    install_myproj_proc.wait()
    install_myproj_proc2 = Popen(
        'git clone https://github.com/brice-v/riscv_vm.git ~/Documents/myprojects', shell=True)
    install_myproj_proc2.wait()
else:
    print("Skipping project...")

############################################################################################################

closup_proc = Popen('sudo apt update && upgrade -y', shell=True)
closup_proc.wait()
closup_proc1 = Popen('sudo apt dist-upgrade -y', shell=True)
closup_proc1.wait()
closup_proc2 = Popen('sudo apt autoremove -y', shell=True)
closup_proc2.wait()


print("----------------------------------------------------------------------------")
print("--------------------------Installation's Complete---------------------------")
print("----------------------------------------------------------------------------")
