# ARP SCANNER

A python tool which uses web APIs to gather informaation about a an IP Address.

## Langauge Used : Python

## Prerequisits :

Python 3.x and Python IDLE/Shell

## Libraries Used :

Scapy<br/>
Sys<br/>
Time<br/>
Os<br/>

Make sure the the required Libraries are installed correctly.

## Installation :

Clone the repository into your system by typing :

```
$ git clone https://github.com/whokilleddb/ArpScan  

```

Once cloned , cd into the directory and install the requirements as follows :

```
$ cd ArpScan  
$ pip3 install -r requirements.txt
```
 
Now type run the script using :

```
$ sudo python3 ArpScan.py
```
#### NOTE : This Program Requires The Sudo Command To Work

The following should give a similar output as :

![](https://github.com/whokilleddb/ArpScan/blob/master/Images/SS.png)


To Scan A Network , Enter The Interface Name And The IP Range You Want To Scan.

```
$ sudo python3 ARP_Scanner.py wlan0 192.168.0.1/24
```
Once The Scan Is Completed , You Should Get An Output Like This :

![](https://github.com/whokilleddb/iprecon/blob/master/Images/SS.png)

