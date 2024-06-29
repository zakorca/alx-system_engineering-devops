# kills a process named killmenow.

exec { 'pkill -f':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
