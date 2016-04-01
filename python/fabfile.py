from fabric.api import run,sudo
from fabric.operations import put


def parser(my_string):
    return my_string.split('_')

def host_type():
    run('uname -a')
    run('ip a s')

def puppet_install():
    sudo('rpm -Uvh http://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm')
    sudo('yum update')
    sudo('yum -y install puppet')

def puppet_active():
    sudo('puppet resource package puppet ensure=latest')
    sudo('cat /etc/passwd')

def install_package_ondemand(*args):
    input_list = args
    old_string = 'package_to_install'
    templ_file = 'template.pp'
    lines = []
    for package in input_list:
        for line in open(templ_file):
            line = line.replace(old_string,package)
            lines.append(line)
    f = open('puppet.pp','w')
    for line in lines:
            f.write(line)
    f.close()
    put('puppet.pp','/tmp/puppet.pp')
    sudo('puppet apply /tmp/puppet.pp')
    run('rm -f /tmp/puppet.pp')