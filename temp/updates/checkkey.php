<?php 
//This basically checks if a key exists in the storage. A very easy thing to write and can be used to check if a whitelist exists
if(file_get_contents("./keystorage.txt", $_GET['keycheck']) !== false)
{
	echo "WHITELISTED"; //Returns whitelisted if exists!
}
else
{
	echo "KEY IS NOT WHITELISTED"; //returns not whitelisted
}
?> 