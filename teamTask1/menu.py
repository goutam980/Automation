                                      #  ARTH2020.3.5  TASK 1
import os 
import subprocess 
# ----------------------------------------------------------------------------------------------------------
# functions



def hadoop_setup():
    had_r=input(""""

press 1 to install Java in your system(if not installed already).
press 2 to download and  install hadoop 1.2.1 in your system(if not installed already).
Press 3 to configure master and get its terminal.
Press 4 to configure slave and get report.
Press 5 to configure client and get its terminal to use the HDFS.
Enter 6 for exit: """)

    had_r=int(had_r)
    
####################### Hadoop installation ############################
    if had_r == 2:
        ansi = input("enter your ip here and please make shour your firewall is disable and ssh is on")
        
        os.system("ansible {} -m copy -a src=/root/hadoop-1.2.1-1.x86_64.rpm  dest=/root".format(ansi))
        #o = subprocess.getoutput("rpm -ivh --force /root/hadoop-1.2.1-1.x86_64.rpm  ")
        print(o[0:250])
        print("\n\t\tInstallation successful")
        input("press any key to continue")


############################# Java installations #####################

    elif had_r == 1:
        a = input("Enter ip of system where you want install Java: ")
        os.system("scp /home/love/Downloads/jdk-8u171-linux-x64.rpm root@{}:/root/".format(a))
        #os.system("ssh root@{} wget 35.244.242.82/yum/java/el7/x86_64/jdk-8u171-linux-x64.rpm".format(a))
        #os.system("ssh root@{} echo 3 > /proc/sys/vm/drop_caches".format(a))
        os.system("ssh root@{} rpm -i /root/jdk-8u171-linux-x64.rpm".format(a))
        input("press any key to continue")


    elif had_r == 3:

#################################### CORE-SITE>XML####################################
        a=input("Enter your IP:")
        b = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>""".format(a)
        f = open('/home/love/Desktop/hadoop/core-site.xml', 'w')
        f.write(b)
        f.close()

#################################### HDFS-SITE>XML####################################
        d=input("Enter Directory name to configure as default namenode dir:")
        b = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{}</value>
</property>
</configuration>""".format(d)
        f = open('/home/love/Desktop/hadoop/hdfs-site.xml', 'w')
        f.write(b)
        f.close()
        
        os.system("scp /home/love/Desktop/hadoop/* root@{}:/etc/hadoop/ ".format(a))
        #os.system("ssh root@{} echo 3 > /proc/sys/vm/drop_caches".format(a))
        os.system("ssh root@{} hadoop namenode -format".format(a))
        os.system("ssh root@{} hadoop-daemon.sh start namenode".format(a))
        
        
        print("\t\t\tWelcome Master Node")
        print("\t\ttype   'exit'   to get out of master's terminal")
        
        os.system("ssh root@{}".format(a))


################################### DATANODE #################################
    
    elif had_r == 4:
#################################### CORE-SITE>XML####################################
        a=input("Enter IP of MASTER:")
        
        b = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>""".format(a)
        
        f = open('/home/love/Desktop/hadoop/core-site.xml', 'w')
        f.write(b)
        f.close()

#################################### HDFS-SITE>XML####################################
        d=input("Enter Directory name to configure as default datanode dir:")
        
        b = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{}</value>
</property>
</configuration>""".format(d)
        f = open('/home/love/Desktop/hadoop/hdfs-site.xml', 'w')
        f.write(b)
        f.close()

        slave_ip = input("Enter IP of slave to be configured:")
        os.system("scp /home/love/Desktop/hadoop/* root@{}:/etc/hadoop/ ".format(slave_ip))
        #os.system("ssh root@{} echo 3 > /proc/sys/vm/drop_caches".format(a))
        os.system("ssh root@{} hadoop-daemon.sh start datanode".format(slave_ip))
        
        print("\n\n\n\n")
        os.system("ssh root@{} hadoop dfsadmin -report".format(slave_ip))

        #print("\n\n\n\t\t\tSlave with IP: {} is Configured Successfully".format(slave_ip))


################################ Client ###########################    
    
    elif had_r == 5:
        a=input("Enter IP of Master to configure the client:")
        
        b = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>""".format(a)
        f = open('/home/love/Desktop/hadoop/core-site.xml', 'w')
        f.write(b)
        f.close()

        client_ip = input("Enter IP of Client to get its terminal:")
        os.system("scp /home/love/Desktop/hadoop/* root@{}:/etc/hadoop/ ".format(client_ip))
        #os.system("ssh root@{} echo 3 > /proc/sys/vm/drop_caches".format(a))

        
        print("\n\n\t\t\tWelcome client Node")

        os.system("ssh root@{}".format(client_ip))
    
    elif had_r == 6:
        exit()
    
    else:
        print("wrong input sir .......")




#######################################################################################################################################


def yum_configure():
    try:
        a = input("Enter ip of system where yum configuration is to be done")
        os.system("scp  /home/love/Desktop/docker/*  root@{}:/etc/yum.repos.d/".format(a))
        #os.system("ssh root@{} echo 3 > /proc/sys/vm/drop_caches".format(a))
        print("\n\n\t\t\tYour yum is configured now. ")
    except ValueError:
        print("Error ...... Please try later...")
        c=input("Press Enter to continue...")



######################################################################################################################################

def doc_docker():
    ip = input("Enter IP of system where you want to use Docker:") 
    key=input(""""

press 1 to configure Docker:
press 2 to download a docker image:
Press 3 to launch a Docker container:
Press 4 to to list all containers(running+stoped):
press 5 to list all available docker images:
press 6 to get terminal of an existing container:
press 7 to remove a container:
Enter 8 for exit: """)

    key=int(key)
    if key == 1:
        try:
            yes_no = input("please configure yum before installing docker.......enter yes if already configured else press any key:")
            yes_no = yes_no.lower()
            if yes_no == "yes":
                #a = input("Enter IP of system where you want to install docker")
                os.system("ssh root@{} yum install docker-ce --nobest -y".format(ip))
                os.system("ssh root@{} systemctl start docker ".format(ip))
                print("Docker sucessfully installed....")
            else:
                yum_configure()
                doc_docker()
                c=input("Press Enter to continue...")
        except ValueError:
            print("Error ...... Please try later...")
            input("Press Enter to continue...")
    
    elif key == 2:
        print("Some of the available Docker images: \nUBUNTU\nCENTOS\nFEDORA\netc....")
        name = input("Enter name of image to download:").lower()
        os.system("ssh root@{} docker pull {}".format(ip, name))

    elif key == 3:
        print("\n\t\tAvailable image:")
        os.system("ssh root@{} docker image ls".format(ip))
        image = input("Enter name of image to launch container: ").lower()
        name = input("Give a uniqe name for the container: ").lower()
        ask  = input("do you want to get terminal of container after running(yes/no): ").lower()
        if ask=="yes":
            os.system("ssh root@{} docker run -it --name {} {}".format(ip, name, image))
        elif ask=="no":
            os.system("ssh root@{} docker run --name {} {}".format(ip, name, image))
        else:
            print("Invalid operation")
    
    elif key == 4:
        print("\n\n")
        os.system("ssh root@{} docker ps -a".format(ip))
    
    elif key == 5:
        print("\n\t\tAvailable docker images:")
        os.system("ssh root@{} docker images".format(ip))
    
    elif key == 6:
        print("\n\n\t\tExisting containers:")
        os.system("ssh root@{} docker ps -a".format(ip))
        print()
        name = input("Enter name of container you want to get terminal for:").lower()
        os.system("ssh root@{} docker start {}".format(ip,name))
        os.system("ssh root@{} docker attach {}".format(ip,name))
    
    elif key == 7:
        print("\n\tAvailable containers:")
        os.system("ssh root@{} docker ps -a".format(ip))
        name = input("\n\nEnter name of container you want to remove(terminate):").lower()
        os.system("ssh root@{} docker rm {} ".format(ip,name))
    
    elif key == 8:
        exit()
    
    else:
        print("wrong input sir .......")



#------------------------------------------------- AWS  ----------------------------------------------------------------	

def aws():
    pass

# ------------------------------------------------aws module end ---------------------------------------------------------


def main():
    print("\t\t\tWelcome to Team:3.5 Menu App")
    print("\t\t\t-------------------------------")
    
    print("""
Enter 1 To setup yum configuration:
Enter 2 To setup and use hadoop :
Enter 3 To setup and use  docker:
Press 4 To setup and use aws services:
""")
    a=int(input("Enter your choice here:"))
    
    if a==1:
        yum_configure()
    
    elif a==2:
        hadoop_setup()
    
    elif a==3:
        doc_docker()
    
    elif a==4:
        aws()
    
    else:
        print("you know nothing johnsno")



