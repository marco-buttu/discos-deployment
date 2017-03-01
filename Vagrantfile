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
        repo.vm.network :private_network, ip: "192.168.60.10"
    end


    # ACS node n.1 (ms: minor servo)
    config.vm.define "nuraghe-ms" do |ms|
        ms.vm.hostname = "nuraghe-ms"
        ms.vm.network :private_network, ip: "192.168.60.11"
    end

end
