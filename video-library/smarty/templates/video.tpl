{include file="header.tpl" title="Video Detail Page"}

<body>
<h1>{$folder}</h1>
<div class="main-container">
  <video id="example_video_1" class="video-js vjs-default-skin" controls preload="none" width="418" height="320"
      inactivityTimeout=0
      poster="images/{$folder}/{$folder}-000.png"
      data-setup='{ "inactivityTimeout": 0 }'>
    <source src="videos/{$video_filename}" type='video/mp4' />
    <p class="vjs-no-js">To view this video please enable JavaScript, and consider upgrading to a web browser that <a href="http://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a></p>
  </video>

{foreach $static_images as $image}
    {$image.scene_id}
    <a href="#" onclick="scrubVideo({$image.scene_ts})"><img src="images/{$folder}/{$image.scene_image}" width="75"></a>
{/foreach}
</div>

{include file="footer.tpl"}

