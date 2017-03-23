# -*- mode: ruby -*-
# vi: set ft=ruby :

$repo_provisioning = <<SCRIPT
yum -y update
sudo yum groupinstall -y 'development tools'
sudo yum install -y gcc libffi-devel python-devel zlib-dev
sudo yum install -y openssl-devel sqlite-devel bzip2-devel
yum install xz-libs
wget http://www.python.org/ftp/python/2.7.10/Python-2.7.10.tar.xz
xz -d Python-2.7.10.tar.xz
tar -xvf Python-2.7.10.tar
cd Python-2.7.10
./configure --prefix=/usr/local
make
make altinstall
sudo rm Python* -r -f
export PATH="/usr/local/bin:$PATH"
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
rm get-pip.py
sudo yum remove -y python-crypto
sudo pip install ansible
SCRIPT

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    # Common configuration for all virtual machines
    config.ssh.insert_key = false
    config.vm.box = "bento/centos-6.8"
    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--ioapic", "on"]
        vb.memory = 4048
        vb.cpus = 4
    end

    # Provisioning server: it will deploy all ACS nodes
    config.vm.define "repository" do |repo|
        repo.vm.provision "shell", inline: $repo_provisioning
        repo.vm.hostname = "repository"
        repo.vm.network :private_network, ip: "192.168.200.199"
    end

    # ACS node n.1
    config.vm.define "manager" do |node|
        node.vm.hostname = "manager"
        node.vm.network :private_network, ip: "192.168.200.200"
    end

    # ACS node n.2 (active surface)
    config.vm.define "as" do |node|
        node.vm.hostname = "as"
        node.vm.network :private_network, ip: "192.168.200.201"
    end

    # ACS node n.3 (minor servo)
    config.vm.define "ms" do |node|
        node.vm.hostname = "ms"
        node.vm.network :private_network, ip: "192.168.200.202"
    end

end
