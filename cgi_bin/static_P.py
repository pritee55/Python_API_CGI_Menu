#!/usr/bin/python3
print("content-type:text/plain")
print()

import subprocess as sp
import cgi

field = cgi.FieldStorage()
btn = field.getvalue("btn")
output = (0,"")

if btn == "vgbtn":
    name1 = field.getvalue("vgname")
    part1 = field.getvalue("spoint")
    part2 = field.getvalue("epoint")
    output = sp.getstatusoutput("parted {} mkpart primary ext4 {}G {}G;".format(name1, part1, part2))
    output = sp.getstatusoutput("lsblk")
    if output[0] == 0:
        print("Successfully created a static partition")
        inf = sp.getstatusoutput("lsblk")
        print(inf[1])
elif btn == "lvbtn":
    name3 = field.getvalue("pname")
    task = sp.getstatusoutput("mkfs.ext4 {}".format(name3))
    name4 = field.getvalue("mpoint")
    task2 = sp.getstatusoutput("mkdir /{}".format(name4))
    task3 = sp.getstatusoutput("mount {} {}".format(name3, name4))
    output = sp.getstatusoutput("lsblk")
    print(output)
    print("Formated and mounted the partision")
elif btn == "stbtn":
    name1 = field.getvalue("num1")
    num1 = field.getvalue("lvname")
    size1 = field.getvalue("size")
    task = sp.getstatusoutput("parted {} resizepart {} {}G".format(name1, num1, size1))
    output = sp.getstatusoutput("lsblk")
    print("output")
    print("Increased the size of the static partition")
elif btn == "delvgbtn":
    name1 = field.getvalue("num1")
    num1 = field.getvalue("lvname")
    size1 = field.getvalue("size")
    task = sp.getstatusoutput("parted {} resizepart {} {}G".format(name1, num1, size1))
    output = sp.getstatusoutput("lsblk")
    print("output")
    print("Increased the size of the static partition")
elif btn == "dellbtn":
    name1 = field.getvalue("num1")
    num1 = field.getvalue("lvname")
    task2 = sp.getstatusoutput("parted {} rm {}".format(name1, num1))
    output = sp.getstatusoutput("lsblk")
    print("output")
    print("Deleted the static partition successfully")

if(output[0] != 0):
    print("Something went wrong!! : \n {} ".format(output[1]))
