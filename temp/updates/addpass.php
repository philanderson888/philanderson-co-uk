<?php
//Welcome to this RED release. Written and annotated by Trivlax
//A basic key whitelist is very simple it mainly utilizes file_put_contents to store the contents into a text file. If you were to go a little extra you can hash your usernames
$pass = $_GET['pass']."\r\n";  //This basically uses the $_GET to get the following. URDOMAIN.domain/addkey.php?key=KEYHERE
if($pass != ""){ // Checks if the key is not blank
	file_put_contents("./pass.txt", $pass, FILE_APPEND); // Places the key into the file designated
	echo "Whitelisted!"; //Returns whitelisted
}
else
{
	echo "Please input a password"; //catches if a key was not inputted.
}

?>