# DNS-spoof

Usage:

1) Edit docker compose file(s):
    - fill in appropriate IP info for the network
    - adjust ip addresses for the containers if necessary

* change ip, gateway, and set parent to match the physical interface you are using

2) Build the docker with build.sh

3) cd to the directory in "runtime" with the experiment you want to run

4) run 
    $ docker compose up -d

5) attach to containers you want to run commands from
    $ docker attach <container name>
