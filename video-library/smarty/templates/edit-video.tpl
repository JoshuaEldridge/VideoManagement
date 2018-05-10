{include file="header.tpl" title="Edit Video Page"}

<body>

<form>
<input name>
<div class="main-container">
  <video id="example_video_1" class="video-js vjs-default-skin" controls preload="none" width="418" height="320"
      inactivityTimeout=0
      poster="images/{$folder}/{$folder}-000.png"
      data-setup='{ "inactivityTimeout": 0 }'>
    <source src="videos/{$video_filename}" type='video/mp4' />
    <p class="vjs-no-js">To view this video please enable JavaScript, and consider upgrading to a web browser that <a href="http://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a></p>
  </video>

<form action="edit-video.php" method="post">
{foreach from=$video_fields item=field_value key=field_name}

{$field_name}: <input type="text" name="{$field_name}" value="{$field_value}"></br>

{/foreach}
<input type="submit" name="submit" value="submit">
</form>
</div>



{include file="footer.tpl"}

