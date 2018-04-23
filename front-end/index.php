<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HTML5 Site</title>
  <link rel=stylesheet href="scripts/demo-slideshow.css" />

  <script src="scripts/jquery-1.11.1.min.js"></script>
  <script src="scripts/jquery.cycle2.min.js"></script>


</head>

<body>
<div id="main">

<div class="cycle-slideshow manual" 
    data-cycle-fx=scrollHorz
    data-cycle-timeout=0
    data-cycle-caption-template="{{slideNum}} / 4"
    data-cycle-next="#next"
    data-cycle-prev="#prev"
    data-cycle-loader=true
    data-cycle-progressive="#slides"
    >
    <div class="cycle-caption"></div>

    <img src="img/Xexyz (USA).png">

    <script id="slides" type="text/cycle">
        [
        "<img src='img/Xexyz (USA).gif'>",
        "<img src='img/oh-hello.gif'>"
        ]
    </script>

</div>
<div class=center>
    <a href=#><span id=prev>&lt;&lt; Prev</span></a>
    <a href=#><span id=next> Next&gt;&gt;</span></a>
</div>


</body>
</html>