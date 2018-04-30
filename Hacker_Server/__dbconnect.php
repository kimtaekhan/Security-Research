<?
$DBHOST="localhost";
$DBUSER="root";
$DBPASS="111111";
$DBNAME = "myhomepage";

# DBMS 접속
# 형식 : resource mysql_connect(서버명,사용자,비번)
$connect = mysqli_connect($DBHOST, $DBUSER, $DBPASS, $DBNAME) or die("DBMS에 접속 실패");
mysqli_set_charset($connect, "utf8");

?>
