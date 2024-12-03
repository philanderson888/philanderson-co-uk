<?php 
 $version = $_GET['versionnum'];
 file_put_contents("./versionnum.txt", "");
 file_put_contents("./versionnum.txt", $version);
?> 