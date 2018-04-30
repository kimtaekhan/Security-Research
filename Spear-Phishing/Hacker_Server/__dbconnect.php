<?
$DBHOST="localhost";
$DBUSER="root";
$DBPASS="111111";
$DBNAME = "myhomepage";

# DBMS CONNECT
$connect = mysqli_connect($DBHOST, $DBUSER, $DBPASS, $DBNAME) or die("DBMS CONNECT FAILED");
mysqli_set_charset($connect, "utf8");

?>
