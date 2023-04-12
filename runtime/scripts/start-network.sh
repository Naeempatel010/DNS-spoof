docker network create -d macvlan \
  --subnet=192.168.12.197/24 \
  --gateway=192.168.12.1 \
  -o parent=wlp2s0b1 dns-net