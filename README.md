# mininetCustomsTopo
'data' file is a data file descripting yourself Topo and it can only include switch and host.

In first line,'h2' means there are two hosts in this topo.And in the second line, 's2' means there are 2 switches.

Under two lines,they are linker ,such as "s1,s2",comma is necessary.

Finally, the command is 
sudo mn --custom ~/mininet/custom/MyTopo.py --topo mytopo,filename='./data' --test pingall

In this command, filename is your topodata filename.
