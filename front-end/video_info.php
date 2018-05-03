<?php

// Make sure we have a video id for display.
// If not, redirect to the main page.
$video_id = htmlspecialchars($_GET["vid"]);
$image_folder = "images/" . $video_id;

if(file_exists($image_folder)) {
    $folder_contents = scandir($image_folder);
    $poster_image = $image_folder . "/" . $video_id . "-001.png";

    $files_array = array();

    foreach ($folder_contents as &$file) {
        $files_array[$image_folder . "/" . $file] = mime_content_type($image_folder . "/" . $file);
    }
//     print_r($images_array);
}

// Build out the JSON array of animated images for the progressive loader.
$animated_images = array();
foreach($files_array as $file_name => $file_type) {
    if($file_type == "image/gif") {
        array_push($animated_images, "\"<img src='" . $file_name . "'>\"");
    }
}
$json_formatted_images = implode(",\n\t", $animated_images);

// Count the number of images to display on the carousel. + 1 for the still image.
$number_of_images = count($animated_images)+1;

// Pull out the associated metadata for the video for display.
// 
// 
// $db = realpath('/Users/161619/Sites/front-end/home-video.db');
// 
// $db = new SQLite3($db, SQLITE3_OPEN_CREATE | SQLITE3_OPEN_READWRITE);
// 
// $results = $db->query('SELECT * FROM videos');
// 
// while ($row = $results->fetchArray()) {
//     var_dump($row);
// }

?>

<!doctype html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cycle2 Progressive Loading</title>
  <link rel=stylesheet href="scripts/home-video.css" />
  <link rel=stylesheet href="scripts/demo-slideshow.css" />
  <script src="scripts/jquery-1.11.1.min.js"></script>
  <script src="scripts/jquery.cycle2.min.js"></script>
</head>
<body>
<div id="main">

<style>
body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; }

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
.center-buttons { margin: auto; width: 50%; }


</style>

<h2 id="manual">VIDEO INFORMATION</h2>
<p>

<a href="index.php">Home</a>

<div class="cycle-slideshow manual" 
    data-cycle-fx=scrollHorz
    data-cycle-timeout=0
    data-cycle-caption-template="{{slideNum}} / <?php print($number_of_images) ?>"
    data-cycle-next="#next"
    data-cycle-prev="#prev"
    data-cycle-loader=true
    data-cycle-progressive="#cycle-images"
    >
    <div class="cycle-caption"></div>
<!-- 
    <img src="images/Reel-1014-01/Reel-1014-01-001.png">
 -->
    <img src="<?php print($poster_image); ?>">
    
    <script id="cycle-images" type="text/cycle">
    [
    <?php print($json_formatted_images); ?>

    ]
    </script>

<div id="buttons" class="center-buttons">
    <button data-cycle-cmd="prev">Prev</button>
    <button data-cycle-cmd="goto" data-cycle-arg="0">Stop</button>
    <button data-cycle-cmd="next">Next</button>
</div>

</div>

</body>
</html>