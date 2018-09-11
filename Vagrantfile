# -*- mode: ruby -*-
# vi: set ft=ruby :


vagrantfile_api_version = "2"
digest = (Digest::MD5.hexdigest Dir.pwd).to_i(16).to_s.slice(0, 16)
vb_dir = `VBoxManage list systemproperties | grep "Default machine folder"`.split(':')[1].strip()


Vagrant.configure(vagrantfile_api_version) do |config|

    # Common configuration for all virtual machines
    config.vm.synced_folder '.', '/vagrant', disabled: true
    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--ioapic", "on"]
        vb.memory = 4096
        vb.cpus = 4
    end


    # DISCOS storage
    config.vm.define "storage" do |node|
        node.vm.hostname = "storage"
        node.vm.box = "bento/centos-7.2"
        node.vm.network :private_network, ip: "192.168.10.200"

        node.vm.provider :virtualbox do |vb|
            vb.name = "deployment_storage_" + digest
            lustre_disk = File.join(vb_dir, vb.name, 'lustre_disk.vdi')
            unless File.file?(lustre_disk)
                vb.customize ['createhd', '--filename', lustre_disk, '--size', 10000] # 10Gb for emulation should be enough
                vb.customize ['storageattach', :id, '--storagectl', 'SATA Controller', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', lustre_disk]
            end
        end
    end


    # ACS node n.1 (manager)
    config.vm.define "manager" do |node|
        node.vm.hostname = "manager"
        node.vm.box = "bento/centos-6.8"
        node.vm.network :private_network, ip: "192.168.10.201"

        node.vm.provider :virtualbox do |vb|
            vb.name = "deployment_manager_" + digest
        end
    end


    # ACS node n.2 (console)
    config.vm.define "console" do |node|
        node.vm.hostname = "console"
        node.vm.box = "bento/centos-6.8"
        node.vm.network :private_network, ip: "192.168.10.202"

        node.vm.provider :virtualbox do |vb|
            vb.name = "deployment_console_" + digest
        end
    end

end
