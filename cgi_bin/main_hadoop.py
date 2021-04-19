#!/usr/bin/python3
print("content-type:text/plain")
print()

import os 
import subprocess as sp
import cgi

field = cgi.FieldStorage()
btn = field.getvalue("btn")
ouput=(0,"")

if btn == "configbtn":
        node = field.getvalue("node")
        if node == 'namenode':
            ip = field.getvalue("IP")
            folder = field.getvalue("folder")
            rc = sp.getoutput("sudo mkdir {}".format(folder))
            print("Folder created for namenode")
            cc = ('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>'''.format(ip))
            text_file = open("/etc/hadoop/core-site.xml", 'w')
            n = text_file.write(cc)
            text_file.close()
            print("Configured the core-site.xml File")
            dd = ('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>{}</value>
</property>
</configuration>
'''.format(folder))
            hdf_file = open("/etc/hadoop/hdfs-site.xml", 'w')
            m = hdf_file.write(dd)
            hdf_file.close()
            print("COnfigured the hdfs-site.xml file")
            outputt = sp.getoutput("echo Y | hadoop namenode -format")
            outputt = print(outputt)
            print("NameNode configured on the system {} successfully".format(ip))
        else:
            ip = field.getvalue("IP")
            folder = field.getvalue("folder")
            rc = sp.getoutput("sudo mkdir {}".format(folder))
            print("Folder created for Datanode")
            cc = ('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>'''.format(ip))
            text_file = open("/etc/hadoop/core-site.xml", 'w')
            n = text_file.write(cc)
            text_file.close()
            print("configured the core-site.xml file of datnode")
            dd = ("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>{}</value>
</property>
</configuration>
""".format(folder))
            hdf_file = open("/etc/hadoop/hdfs-site.xml", 'w')
            m = hdf_file.write(dd)
            hdf_file.close()
            print("configured the hdfs-site.xml file of datnode")
            print("DataNode configured on the system {} successfully".format(ip))
elif btn == "stnbtn":
        task = field.getvalue("task")
        outputt = sp.getoutput("sudo hadoop-daemon.sh {} namenode".format(task))
        print(outputt)
        output = print("Namenode {} Successfully!!".format(task))
elif btn == "stdbtn":
        task = field.getvalue("task")
        outputt = sp.getoutput("sudo hadoop-daemon.sh {} datanode".format(task))
        print(outputt)
        output = "Datanode {} Successfully!!".format(task)
        print(outputt)

elif btn == "configcbtn":

        ip = field.getvalue("IP")
        ctree = ET.parse("/etc/hadoop/core-site.xml")
        croot = ctree.getroot()
        if(len(croot) == 0):
                cp = ET.SubElement(croot, 'property')
        else:
                cp = croot[0]
        if(len(cp) == 0):
                cn = ET.SubElement(cp, 'name')
                cv = ET.SubElement(cp,'value')
        else:
                cn = cp[0]
                cv = cp[1]

        cn.text = "fs.default.name"
        cv.text = "hdfs://{}:9001".format(ip)
        ctree.write("/etc/hadoop/core-site.xml",pretty_print=True)

        print("System configured as Client Successfully!!")
elif btn == "opbtn":
        file = field.getvalue("file")
        operation = field.getvalue("operation")
        if operation == "-put":
                output = sp.getstatusoutput("sudo hadoop fs -put {} /".format(file))
                if output[0] == 0:
                        print("File uploaded Successfully!! \n {} ".format(output[1]))

        elif operation == "-cat":
                output = sp.getstatusoutput("sudo hadoop fs -cat {}".format(file))
                if output[0] == 0:
                        print("File read Successfully \n {} ".format(output[1]))
        elif operation == "-touchz":
                output = sp.getstatusoutput("sudo hadoop fs -touchz {}".format(file))
                if output[0] == 0:
                        print("File created Successfully \n {} ".format(output[1]))

        elif operation == "-rm":
                output = sp.getstatusoutput("sudo hadoop fs -rm {}".format(file))
                if output[0] == 0:
                        print("File removed Successfully \n {} ".format(output[1]))

elif btn == "infobtn":
        output = sp.getstatusoutput("sudo hadoop dfsadmin -report | less")
        if output[0] == 0:
                print("Information of Cluster:  \n {} ".format(output[1]))

elif btn == "fileinfobtn":
        output = sp.getstatusoutput("sudo hadoop fs -ls /")
        if output[0] == 0:
                print("Files information in the Cluster: \n {} ".format(output[1]))

elif btn == "getlink":
        ip = field.getvalue("IP")
        print("Link to WebUI : 'http://{}:50070'".format(ip))
        output = (0,"")

else:
    print("hello")
