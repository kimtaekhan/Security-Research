#!/usr/bin/env python
# -*- coding: utf-8 -*-

# "#!"은 2Byte의 매직넘버(magic number)로 이 스크립트를 실행시켜줄 프로그램의 경로를 지정한다.
# env는 환경 변수에서 지정한 언어의 위치를 찾아서 실행됩니다.

import socket, subprocess, sys
from logging import getLogger, ERROR # Import Logging Things (로깅기능을 수행하기 위해 모듈을 불러온다.)
getLogger("scapy.runtime").setLevel(ERROR) # Get Rid if IPv6 Warning (IPv6에 대한 경고를 없앤다.)
from scapy.all import *
import time # sleep 적용하기 위해 time 모듈을 불러온다.
#from termcolor import colored # print 에 컬러 적용을 위해 모듈을 불러온다.

subprocess.call('clear',shell=True) # 콘솔명령어를 적용함

print """
\033[1;34m
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                  ################################################################
                           ._________    _  ___________  __________  ____    
                           |   |/  /     |__   __|       |   |__|  |          
                           |   /  /        |\ /|         |   /__\  |         
                           |   \  \        |/ \|         |   /__ \ |         
                           | __|\__\       |\_/|         /__/|  |_\|        
                          /\      \\/      //    \/        //      /\  \\/ 
                  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                ######################################################################
\033[1;m
                                    \033[1;41mMAKE BY KIMTAEKHAN\033[1;m


                                      \033[1;44m[!] 경고 !!!!!\033[1;m
                        \033[1;44m함부로 외부에다가 공격시도 하지마세요 !!!!!\033[1;m

"""

############ 시간 설정 ############
time_counter=1.00 # 시간 설정 1초
###################################

################## 공격 설정  ##################
try:
                subprocess.call("ifconfig eth0 | awk '/inet /' | awk '{print $2}' > self_ip",shell=True) # 콘솔명령어를 적용함

                f = open("self_ip","r")
                arp_addrs = f.readline()
                pattern = re.compile(r'\s+')
                # re 모듈의 compile 함수는 정규식 패턴을 입력으로 받아들여 정규식 객체를 리턴하는데, 즉 re.compile(검색할문자열) 와 같이 함수를 호출하면 정규식 객체 (re.RegexObject 클래스 객체)를 리턴하게 된다.
                # \s 화이트 스페이스를 의미하는데, [\t\n\r\f] 와 동일
                # r 은 정규식 객체를 사용하기 위해 사용된다.
                arp_addrs = re.sub(pattern, '', arp_addrs)
                # re.sub() - 패턴과 일치하는 문자열 변경
                subprocess.call("rm -f self_ip", shell=True)

except KeyboardInterrupt: #사용자가 프로그램을 종료하고자 할때 키보드의 입력에 따른 메세지를 출력.
       print "\n\n\033[1;m \033[1;35m[!]\033[1;m\033[1;36m공격자의 명령에 의해 프로그램을 종료합니다.\033[1;m\n" # 메세지 출력
       print "\033[1;31m[!]\033[1;m \033[1;33m종료중\033[1;m" # 메세지 출력
       print "\033[1;34m   .\033[1;m" # 메세지 출력
       time.sleep(time_counter) # 설정 시간 적용
       print "\033[1;35m   .\033[1;m" # 메세지 출력
       time.sleep(time_counter) # 설정 시간 적용
       print "\033[1;36m   .\033[1;m" # 메세지 출력
       time.sleep(time_counter) # 설정 시간 적용
       print "\n\033[1;32m[!]\033[1;m \033[1;38m완료 !!\033[1;m" # 메세지 출력
       sys.exit(1) # 종료

conf.verb = 0 # 동작간 메세지 출력하지 않음
arp_addr = (arp_addrs + "/24")
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=arp_addr),timeout=1)
#print colored('####################### 찾은 MAC 주소 #######################', 'red')
print '\033[1;31m####################### 찾은 MAC 주소 #######################\033[1;m' # 메세지 출력
ans.summary(lambda (s,r): r.sprintf("\033[1;44m%Ether.src% %ARP.psrc%\033[1;m"))
#print colored("#############################################################", "red")
print "\033[1;31m#############################################################\033[1;m" # 메세지 출력
f.close()