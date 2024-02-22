# This script fixes the server error using nginx

file { 'fix-for-nginx':
ensure  => 'file',
path    => '/etc/default/nginx',
content => inline_template('<%= File.read("/etc/default/nginx").gsub(/15/, "4096") %>'),
}

-> exec { 'nginx-restart':
command => 'service nginx restart',
path    => '/etc/init.d/',
}
