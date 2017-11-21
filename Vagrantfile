# -*- mode: ruby -*-
# vi: set ft=ruby :


VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    # Common configuration for all virtual machines
    config.ssh.insert_key = false
    config.vm.box = "bento/centos-6.7"
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


    # ACS node n.2 (active surface)
    config.vm.define "as" do |node|
        node.vm.hostname = "as"
        node.vm.network :private_network, ip: "192.168.10.201"
    end


    # ACS node n.3 (minor servo)
    config.vm.define "ms" do |node|
        node.vm.hostname = "ms"
        node.vm.network :private_network, ip: "192.168.10.202"
    end

end
