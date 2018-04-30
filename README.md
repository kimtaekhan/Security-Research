##### If u don't have CentOS. Following Here ! Showing Make Easy Server Ways ! #####
##### Remember Please. I'm Use Mysql ID : root // Password : 111111 // because only do Tested. #####
##### and homepage is not make english , that's korean language. so if u want do more tested,  should be make ur homepage :) Good luck ! #####
##### 1. CentOS6.9 New server setup HERE #####
# make .sh file and Copy & Paste

#!/bin/sh

check1=`cat /etc/sysconfig/network | grep kimtaekhan.net | wc -l`
check2=`cat /etc/sysconfig/network | grep NOZEROCONF | wc -l`
check3=`hostname | grep kimtaekhan.net | wc -l`
if [ "$check1" -eq 0 ]; then
        sed -i 's/localhost.localdomain/kimtaekhan.net/g' /etc/sysconfig/network
fi
if [ "$check2" -eq 0 ]; then
        echo NOZEROCONF=yes >> /etc/sysconfig/network
fi
if [ "$check3" -eq 0 ]; then
        hostname kimtaekhan.net
fi

ifconfig eth0 | awk '/inet /' | awk '{print $2}' | awk -F: '{print $2}' > self_ip.txt

self_ip="`cat self_ip.txt`"

checkip=`cat /etc/hosts | grep "kth kimtaekhan.net" | wc -l`

if [ "$check1" -eq 0 ]; then
	echo $self_ip kth kimtaekhan.net >> /etc/hosts
fi

/etc/init.d/network restart

LANG=C yum -y groupinstall "Development Tools"
yum -y install rdate
LANG=C yum -y groupinstall "Web Server"
LANG=C yum -y groupinstall "MySQL Database server"
yum -y install java-1.8.0-openjdk java-1.8.0-openjdk-devel

# php 5 Version Apache Setting
yum -y install php php-devel php-pear php-mysql php-mbstring php-gd php-imap php-odbc php-xmlrpc php-xml

cat << EOF >> /etc/httpd/conf/httpd.conf
LoadModule php5_module modules/libphp5.so 
AddType application/x-httpd-php .php .php3 .php4 .php5 .html .htm .inc 
DirectoryIndex index.html index.htm index.php
EOF

# php-mysql Setting
yum -y install php-mysql
sed -i 's/short\_open\_tag \= Off/short\_open\_tag \= On/g' /etc/php.ini
/etc/init.d/httpd restart

# /etc/my.cnf [mysqld] Add below
sed -i '6acollation-server = utf8_general_ci' /etc/my.cnf
sed -i '6acharacter-set-server = utf8' /etc/my.cnf
sed -i '6ainit_connect = "SET NAMES utf8"' /etc/my.cnf
sed -i '6ainit_connect = "SET collation_connection = utf8_general_ci"' /etc/my.cnf
sed -i '6acharacter-set-client-handshake = FALSE' /etc/my.cnf


/etc/init.d/mysqld restart

rdate -s time.bora.net # change it south korea time

java -version > /dev/null 2>&1
if [ $? -eq 0 ];then # JDK Error Confirm !
    echo "JDK Setup Check : OK !"
else
    echo "JDK Setup Check : Fail !"
fi

#######################################################################


#################### 2. Original Server DB Setup ######################
###### Running MySQL and copy & paste ######
create database myhomepage;

use myhomepage;

create table member (
 id int not null auto_increment primary key,
 userid varchar(30) not null unique,
 userpw varchar(41) not null,
 username varchar(30) not null,
 email varchar(50) not null,
 date datetime
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

create table bbs1 (
no       int not null auto_increment primary key comment 'Article number',
userid   varchar(30) not null comment 'Writer', 
title    varchar(50) not null comment 'Title',
passwd   varchar(41) not null comment 'Writing password', 
contents text not null comment 'Content',
date     datetime  not null comment 'Writing Time',
ipaddr   varchar(15) not null comment 'Written IP address',
count    int not null comment 'View Article ',
uploadfile varchar(100) comment 'Upload file'
) ENGINE=MyISAM DEFAULT CHARSET utf8;

create table bbs2 (
no       int not null auto_increment primary key comment 'Article number',
userid   varchar(30) not null comment 'Writer', 
title    varchar(50) not null comment 'Title',
passwd   varchar(41) not null comment 'Writing password', 
contents text not null comment 'Content',
date     datetime  not null comment 'Writing Time',
ipaddr   varchar(15) not null comment 'Written IP address',
count    int not null comment 'View Article ',
uploadfile varchar(100) comment 'Upload file'
) ENGINE=MyISAM DEFAULT CHARSET utf8;

create table bbs3 (
no       int not null auto_increment primary key comment 'Article number',
userid   varchar(30) not null comment 'Writer', 
title    varchar(50) not null comment 'Title',
passwd   varchar(41) not null comment 'Writing passwor', 
contents text not null comment 'Content',
date     datetime  not null comment 'Writing Time',
ipaddr   varchar(15) not null comment 'Written IP address',
count    int not null comment 'View Article ',
uploadfile varchar(100) comment 'Upload file'
) ENGINE=MyISAM DEFAULT CHARSET utf8;

create table bbs4 (
no       int not null auto_increment primary key comment 'Article number',
userid   varchar(30) not null comment 'Writer', 
title    varchar(50) not null comment 'Title',
passwd   varchar(41) not null comment 'Writing passwor', 
contents text not null comment 'Content',
date     datetime  not null comment 'Writing Time',
ipaddr   varchar(15) not null comment 'Written IP address',
count    int not null comment 'View Article ',
uploadfile varchar(100) comment 'Upload file'
) ENGINE=MyISAM DEFAULT CHARSET utf8;

create table bbs5 (
no       int not null auto_increment primary key comment 'Article number',
userid   varchar(30) not null comment 'Writer', 
title    varchar(50) not null comment 'Title',
passwd   varchar(41) not null comment 'Writing passwor', 
contents text not null comment 'Content',
date     datetime  not null comment 'Writing Time',
ipaddr   varchar(15) not null comment 'Written IP address',
count    int not null comment 'View Article ',
uploadfile varchar(100) comment 'Upload file'
) ENGINE=MyISAM DEFAULT CHARSET utf8;
#############################################################

#################### 3. Hacker Server DB Setup ######################
###### Running MySQL and copy & paste ######
create database myhomepage;

use myhomepage;

create table checkyet (
 id int not null auto_increment primary key,
 userid varchar(30) not null unique,
 userpw varchar(41) not null,
 date datetime);

create table member (
id int not null auto_increment primary key,
userid varchar(30) not null unique,
userpw varchar(41) not null,
date datetime);
#############################################################
