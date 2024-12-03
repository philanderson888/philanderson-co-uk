<!DOCTYPE HTML>

<?php

$username = $_POST['uname'];
$password = $_POST['password'];
session_start();
$server = 'localhost';
$user = 'c4290920';
$pass = 'Ci#BB6C3i3';
$db = 'c4290920_db01';
$con=mysqli_connect($server,$user,$pass,$db) or die('Could not connect to database');
$result = mysqli_query($con, "SELECT * FROM `login_info` WHERE `uname`= `$username` && `password`=`$password`");
$count = mysqli_num_rows($result);



echo $count;
if($count===1){
    $_SESSION['loggedin'] = 1;
    echo "<script>window.location = '/philip/loginsite/success.php'</script>";
}else{
    echo "Incorrect";
}

if(isset($_SESSION['loggedin']) && $_SESSION['loggedin'] == 1){
    echo "<script>window.location = '/philip/loginsite/success.php'</script>";  
}




?>


<html>
<body>
    <form method="post" action="index.php">
        Username:<br/>
        <input type="text" name="uname"><br/>
        Password:<br/>
        <input type="password" name="password"><br/>
        <input type="submit" value="Login"> 
    </form>
</body>
</html>
<?php
session_destroy();