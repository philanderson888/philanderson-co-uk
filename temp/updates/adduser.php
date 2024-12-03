<?php
//Welcome to this RED release. Written and annotated by Trivlax
//A basic key whitelist is very simple it mainly utilizes file_put_contents to store the contents into a text file. If you were to go a little extra you can hash your usernames
$user = $_GET['user']."\r\n";  //This basically uses the $_GET to get the following. URDOMAIN.domain/addkey.php?key=KEYHERE
if($user != ""){ // Checks if the key is not blank
	file_put_contents("./users.txt", $user, FILE_APPEND); // Places the key into the file designated
	echo "Whitelisted!"; //Returns whitelisted
}
else
{
	echo "Please input a username"; //catches if a key was not inputted.
}

?>