<!doctype html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cycle2 Progressive Loading</title>
  <link rel=stylesheet href="scripts/demo-slideshow.css" />
  <script src="scripts/jquery-1.11.1.min.js"></script>
  <script src="scripts/jquery.cycle2.min.js"></script>
  <script type="text/javascript">
  
  </script>
  
</head>
<body>
<div id="main">

<style>
.auto   { width: 200px; height: 200px }
.manual { width: 300px; height: 225px }

/* display paused text on top of paused slideshow */
.cycle-loading:after {
    content: 'Loading'; color: white; background: black; padding: 10px;
    z-index: 500; position: absolute; top: 10px; right: 10px;
    border-radius: 10px;
    opacity: .5; filter: alpha(opacity=50);
}

.example3 > div { width: 100%; height: 100% }
.example3 p { 
    background: black; color: white; margin: 0; padding: 5px; 
    position: absolute; bottom: 0; opacity: .6; width: 100%;
    text-align: center;
}

.center { text-align: center; }

</style>

<h2 id="manual">Manual</h2>
<p>
This example shows that progressive loading works just as well for 
manual slideshows.
<div class="cycle-slideshow manual" 
    data-cycle-fx=scrollHorz
    data-cycle-timeout=0
    data-cycle-caption-template="{{slideNum}} / 4"
    data-cycle-next="#next"
    data-cycle-prev="#prev"
    data-cycle-loader=true
    data-cycle-progressive="#images4"
    >
    <div class="cycle-caption"></div>
    <img src="images/Reel-100902/Reel-100902-001.png">

    <script id="images4" type="text/cycle">
    [
        "<img src='images/Reel-100902/Reel-100902-001.gif'>",
        "<img src='images/Reel-100902/Reel-100902-002.gif'>",
        "<img src='images/Reel-100902/Reel-100902-003.gif'>",
        "<img src='images/Reel-100902/Reel-100902-004.gif'>",
        "<img src='images/Reel-100902/Reel-100902-005.gif'>",
        "<img src='images/Reel-100902/Reel-100902-006.gif'>",
        "<img src='images/Reel-100902/Reel-100902-007.gif'>"
    ]
    </script>

</div>
<div class=center>
    <a href=#><span id=prev>&lt;&lt; Prev</span></a>
    <a href=#><span id=stop> STOP </span></a>    
    <a href=#><span id=next>Next &gt;&gt;</span></a>
</div>

<div id=buttons>
    <button data-cycle-cmd="prev">Prev</button>
    <button data-cycle-cmd="next">Next</button>
    <button data-cycle-cmd="pause">Pause</button>
    <button data-cycle-cmd="resume">Resume</button>
    <button data-cycle-cmd="stop">Stop</button>
    <button data-cycle-cmd="destroy">Destroy</button>
    <button data-cycle-cmd="goto" data-cycle-arg="0">Goto Slide 0</button>
</div>

</body>
</html>