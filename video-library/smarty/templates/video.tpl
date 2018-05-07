{include file="header.tpl" title="Video Detail Page"}

<body>

<div class="main-container">
  <video id="example_video_1" class="video-js vjs-default-skin" controls preload="none" width="418" height="320"
      inactivityTimeout=0
      poster="images/{$folder}/{$folder}-000.png"
      data-setup='{ "inactivityTimeout": 0 }'>
    <source src="videos/{$video_filename}" type='video/mp4' />
    <p class="vjs-no-js">To view this video please enable JavaScript, and consider upgrading to a web browser that <a href="http://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a></p>
  </video>

{foreach $static_images as $image}
    <a href="#" onclick="scrubVideo({$image.scene_ts})"><img src="images/{$folder}/{$image.scene_image}" width="75"></a>
{/foreach}
</div>

<!-- 
879.412746
907.507508
924.991658
936.403070
984.317651
1011.144478
1018.785452
1037.604271
1074.841508
1098.832165
1115.081748
1116.449783
1124.891558
1141.007674
1151.918585
1165.231899
1196.763430
 -->

</body>
</html>
