<!DOCTYPE html>
<html>
<head>
  <title>{$title|default:"My Home Video"}</title>
  <link href="video-library.css" rel="stylesheet" type="text/css">
  <link href="video-js/video-js.css" rel="stylesheet" type="text/css">
  <script src="video-js/video.js"></script>
  <script>
    videojs.options.flash.swf = "video-js/video-js.swf";
  </script>
    <script>
    function scrubVideo(t) {
        var t = t + 0.2
        var myPlayer = videojs('example_video_1');
        if(myPlayer.paused()) {
            myPlayer.currentTime(t)
            myPlayer.play()
        } else {
            myPlayer.currentTime(t)
        }
    }
    </script>
</head>