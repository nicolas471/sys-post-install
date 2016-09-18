#! /usr/bin/env python3

import subprocess


def update():
    '''Update and upgrade fresh fedora installation'''
    p = subprocess.Popen(['sudo dnf update -y'], stderr=subprocess.PIPE,
                         shell=True)
    output, err = p.communicate()


def install_repositories():
    '''Add third party repositories'''
    commads = [
        {'rpmfusion':
         'rpm -Uvh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora.noarch.rpm)'
         },
        {'horst3180':
         'dnf config-manager --add-repo http://download.opensuse.org/repositories/home:Horst3180/Fedora_$(rpm -E %fedora)/home:Horst3180.repo'},
        {'snwh Paper':
         'dnf config-manager --add-repo http://download.opensuse.org/repositories/home:snwh:paper/Fedora_$(rpm -E %fedora)/home:snwh:paper.repo'},
    ]

    for c in commads:
        for k, v in c.items():
            subprocess.Popen(v, stderr=subprocess.PIPE, shell=True)


def system_packages():
    '''Read from a list all packages needed and install'''
    subprocess.Popen(['dnf install -y $(cat data/system-packages.list)'],
                     shell=True)


def install_thirdparty():
    '''Install third party packages(ej: chrome)'''
    pass


def python_packages():
    '''Read from a list all packages needed and install via pip'''
    subprocess.Popen(['pip3 install -r data/python-packages.list'], shell=True)


def clean():
    '''Remove unnecessary packages'''
    pass


if '__main__' == __name__:
    update()
    install_repositories()
    system_packages()
    python_packages()
