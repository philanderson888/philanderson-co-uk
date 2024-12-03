<?php
    session_start();
    if(isset($_SESSION['loggedin'])) 
    {
        
    
?>
<html>
<h2>You have logged in!</h2>
</html>
<?php
    }else{
        echo "<script>window.location = '/philip/loginsite/index.php'</script>";
    }
    ?>