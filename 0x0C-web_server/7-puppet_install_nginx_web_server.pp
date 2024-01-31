# nginx_setup.pp

class { 'nginx':
  ensure => 'installed',
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Class['nginx'],
  notify  => Service['nginx'],
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => file,
  content => 'Hello World!',
  require => Class['nginx'],
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
  require => Class['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [
    File['/etc/nginx/sites-enabled/default'],
    File['/var/www/html/index.nginx-debian.html'],
    File['/var/www/html/404.html'],
  ],
}
