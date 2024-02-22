# This script fixes the server error using nginx

# Increase ULIMIT number
file { 'fix-for-nginx':
ensure  => 'file',
path    => '/etc/default/nginx',
content => inline_template('<%= File.read("/etc/default/nginx").gsub(/15/, "4096") %>'),
}

# restart nginx
-> exec { 'nginx-restart':
command => 'nginx restart',
path    => '/etc/init.d/',
}
