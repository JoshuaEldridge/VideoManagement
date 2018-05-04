<!doctype html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Home Video</title>
  <link rel=stylesheet href="scripts/home-video.css" />
  <link rel=stylesheet href="scripts/demo-slideshow.css" />
  <script src="scripts/jquery-1.11.1.min.js"></script>
  <script src="scripts/jquery.cycle2.min.js"></script>

</head>
<body>
<?php

function file_ext_strip($filename){
    return preg_replace('/.[^.]*$/', '', $filename);
}
// Pull out the associated metadata for the video for display.

$db = realpath('/Users/josh/Sites/front-end/home-video.db');

$db = new SQLite3($db, SQLITE3_OPEN_CREATE | SQLITE3_OPEN_READWRITE);

$results = $db->query('SELECT video_md5, video_filename, video_length, video_format, video_width, video_height FROM videos order by video_filename');

while ($r = $results->fetchArray()) {
    $basename = file_ext_strip($r['video_filename']);
    print("<p><a href='video_info.php?vid=" . $basename . "'>" . $r['video_filename'] . "</a><br />");
    print($r['video_md5'] . "<br />");
//     print($r['video_length'] . "<br />");
    print(gmdate("H:i:s", $r['video_length']) . "<br />");
    print($r['video_format'] . "<br />");
    print($r['video_width'] . "x" . $r['video_height']);
}
?>


</body>
</html>