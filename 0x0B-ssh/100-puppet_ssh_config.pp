#Puppet to change config file

file_line{'Turn of password auth':
path=> '/etc/ssh/ssh_config',
line=> 'PasswordAuthentication no'
}

file_line{'Declare identity file':
path=> '/etc/ssh/ssh_config',
line=> 'IdentiryFile ~/.ssh/school'

}
