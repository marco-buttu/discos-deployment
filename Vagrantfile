# -*- mode: ruby -*-
# vi: set ft=ruby :

$repo_provisioning = <<SCRIPT
sudo yum groupinstall -y 'development tools'
sudo yum install -y gcc libffi-devel python-devel openssl-devel
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
        repo.vm.hostname = "repo-test"
        repo.vm.network :private_network, ip: "192.168.200.199"
    end

    # ACS node n.1 (mng: manager)
    config.vm.define "discos-mng" do |node|
        node.vm.hostname = "discos-mng"
        node.vm.network :private_network, ip: "192.168.200.200"
    end

    # ACS node n.2 (as: active surface)
    config.vm.define "discos-as" do |node|
        node.vm.hostname = "discos-as"
        node.vm.network :private_network, ip: "192.168.200.201"
    end

    # ACS node n.3 (ms: minor servo)
    config.vm.define "discos-ms" do |node|
        node.vm.hostname = "discos-ms"
        node.vm.network :private_network, ip: "192.168.200.202"
    end

end
