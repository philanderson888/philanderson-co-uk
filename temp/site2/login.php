

<?php
	
	if($_POST["firstname"] == "Philip"){
		if($_POST["password"] == "Godisgood"){	
			$correct = TRUE;
		}else{
			$correct = FALSE;
		}
	}else{
		$correct = FALSE;
	}

	if($correct == TRUE){

		echo "<script>window.location = '/philip/site2/dashboard'</script>";
		echo "<h3 id='login'>Correct Username and Password, Welcome Back!</h3>";
		 
	}else{
		echo "<script>window.location = '/philip/site2/'</script>";
	}
?>

<html>
    <head>
<script data-ad-client="ca-pub-6406272216834493" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        <title>Philip - Login!</title>
		<link rel="stylesheet" href="style.css" type="text/css">
    </head>
    <body>
			<!-- <button class="btn btn-primary">Default</button> -->
	<div class="navigation">
			<header>
				<nav>
					<ul>
						<li><a href="index.html">Home</a></li>
						<li><a href="about.html">About</a></li>
						<li><a href="register.html">Register</a></li>
						<li><a href="login.html">Login</a></li>
					</ul>
				</nav>
			</header>
		</div>
			<section>
					<div id="titlediv">
				<h2 class="title">Login</h2>
				</div>
				<hr>

			</section>
        <br>
        <br>

    </body>
</html>



