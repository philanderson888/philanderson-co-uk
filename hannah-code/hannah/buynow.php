<html>
<head>

<link rel="icon" href="images/icon5.png">
<link rel="stylesheet" href="phphelp.css">

<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.1/css/all.css" integrity="sha384-vp86vTRFVJgpjF9jiIGPEEqYqlDwgyBgEF109VFjmqGmIY/Y4HV4d3Gp2irVfcrp" crossorigin="anonymous">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">


<title>DTD - Pay Now!</title>

<style>
        body {
          font-family: "Lucida Console", "Courier New", monospace;
          background-color: white;
          background-color: #ffffff;
          background-position: center;
          background-repeat: repeat;
          background-size: cover;
        }

        body {
            font-family: "Open Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", Helvetica, Arial, sans-serif; 
        }
        
        /* Navbar links */
        .navbar a {
            float: left;
            text-align: center;
            padding: 12px;
            color: white;
            text-decoration: none;
            font-size: 17px;
        }
        
        /* Navbar links on mouse-over */
        .navbar a:hover {
            background-color: #000;
        }
        
        
        /* Add responsiveness - will automatically display the navbar vertically instead of horizontally on screens less than 500 pixels */
        @media screen and (max-width: 500px) {
            .navbar a {
            float: none;
            display: block;
            }
        }

        .bg-img {
  /* The image used */
  background-image: url("https://i.pinimg.com/originals/60/e9/3d/60e93de6c2475b184f5aca595fa53237.jpg");

  min-height: 380px;

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;

  /* Needed to position the navbar */
  position: relative;
}

/* Position the navbar container inside the image */
.container {
  position: absolute;
  margin: 20px;
  width: auto;
}

/* The navbar */
.topnav {
  overflow: hidden;
  background-color: #333;
}

/* Navbar links */
.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.shoppy-wrapper{
  display:none;
}
</style>

<body>

<div class="navbar">
<div class="bg-img">
  <div class="container">
    <div class="topnav">
 
  <a href="index.html"><i class="fa fa-fw fa-home"></i> Home</a> 
  <a href="#"><i class="fa fa-fw fa-search"></i>Watch</a> 
  <a href="#"><i class="fa fa-fw fa-envelope"></i>My Work</a> 
  <a href="#"><i class="fa fa-fw fa-user"></i> Find Out More</a>
  </div>
  </div>
</div>

</body>


<button>
<img class="card-img-top" src="https://cdn.homedit.com/wp-content/uploads/2012/05/house-amoberen-berg5.jpg" width="500" height="300" alt="Image" onclick='payButton()'>
<u style="color: red"><h1 style="color: red">DTD</h1></u>
<u style="color: red"><p style="color: red"><b>DTD is a webiste that sells ideas and pictures for other people,<br> 
    while they send us pictures and infomation to do their house up for them.</b></p></u>
</button>

<div class="shoppy-wrapper" id="shoppy-wrapper" name="shoppy-product" data-id="Jlxcu8K"><span class="shoppy-close" id="shoppy-close" onclick="hideShoppy()"></span><div class="shoppy-container"><iframe src="https://shoppy.gg/product/embed?embed=&amp;product=Jlxcu8K"></iframe></div></div>

<script src="https://code.jquery.com/jquery-3.5.1.js" integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" crossorigin="anonymous"></script>
<script src="https://shoppy.gg/api/embed.js"></script>
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@10"></script>
<script>
function payButton(){
    Swal.fire({
        title: 'Payment methods',
        html: `
        <p>How would you like to pay?</p>
        <img src="images/paypal.png" onclick="showShoppy()" width="300">
        <br><br><br><br>
        <img onclick="openSteam()" id="option_steam" src="images/steam.png"  width="300">`,
    })
}



function openSteam(){ 
  Swal.fire({
        title: 'Payment methods',
        html: `
        <form action="purchase.php" method="POST">
<label for="email">Your Email Address</label>
<input id="email" name="email" type="email" placeholder="Enter your email here" required></input>
<br><br>
<label for="cardcode">Gift Card Code</label>
<input id="cardcode" name="cardcode" type="text" placeholder="Enter your card code here" required></input>
</form>`

 })
}


function showShoppy(){
  document.getElementById("shoppy-wrapper").style.display = "block";
}

function hideShoppy(){
  document.getElementById("shoppy-wrapper").style.display = "none";
}
</script>



</head> 
</html>