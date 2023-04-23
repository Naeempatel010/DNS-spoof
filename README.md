# DNS-spoof

Usage:

1) Edit runtime/scripts/start-network.sh

* change ip, gateway, and set parent to match the physical interface you are using

2) Build the docker with build.sh

3) Start the network with the script.

Verify with 

$docker inspect dns-net

4) launch your containers

docker run -it --rm -v <Path to directory on host>:<path to mount on docker> --name <name> --network dns-net dns-docker

5) See Mac and IP with docker inspect dns-net
