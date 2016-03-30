from fabric.api import run,sudo
from fabric.operations import put


def parser(my_string):
    return my_string.split('_')

def host_type():
    run('uname -a')
    run('ip a s')

def puppet_install():
    run('sudo rpm -Uvh http://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm')
    run('sudo yum update')
    run('sudo yum -y install puppet')

def puppet_active():
    sudo('puppet resource package puppet ensure=latest')
    sudo('cat /etc/passwd')

def install_package():
    put('puppet.pp','/tmp/puppet.pp')
    sudo('puppet apply /tmp/puppet.pp')
    run('rm -f /tmp/puppet.pp')

def install_package_ondemand(*args):
    input_list = args
    # package_list = parser(input_list)
    # for package in package_list:
    #     print 'Do something with %s' % package
    print input_list