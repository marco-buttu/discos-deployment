# -*- mode: ruby -*-
# vi: set ft=ruby :


VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    # Common configuration for all virtual machines
    config.ssh.insert_key = false
    config.vm.box = "bento/centos-6.8"
    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--ioapic", "on"]
        vb.memory = 4096
        vb.cpus = 4
    end


    # ACS node n.1
    config.vm.define "manager" do |node|
        node.vm.hostname = "manager"
        node.vm.network :private_network, ip: "192.168.10.200"
    end


    # ACS node n.2 (console)
    config.vm.define "console" do |node|
        node.vm.hostname = "console"
        node.vm.network :private_network, ip: "192.168.10.201"
    end

end
