{include file="header.tpl" title="Video Index Page"}

<body>

{foreach $source_videos as $video}
<div class="main-container">
<h1>{$video.s_filename|substr:0:-4}</h1>
<div class="poster">
<img src="images/{$video.s_filename|substr:0:-4}/{$video.s_filename|substr:0:-4}-000.png" width="320">
</div>
<div class="video-info">
    {$video.s_md5}<br>
    <a href="video.php?source_id={$video.source_id}">{$video.s_filename}</a><br>
    {$video.s_codec_name}<br>
    {$video.s_codec_long}<br>
    {$video.s_codec_tag}<br>
    {$video.s_codec_tag_string}<br>
    {$video.s_width} x {$video.s_height}<br>
    {$video.s_format}<br>
    {$video.s_format_long}<br>
    {$video.s_duration|date_format:"%H:%M:%S"}<br>
    {$video.s_size|filesize}<br>
    {$video.s_bit_rate}<br>
    {$video.s_timecode}<br>
    {$video.s_creation_time|date_format:"%b %d, %Y"}<br>
    {$video.s_year}<br>
    {$video.s_month}<br>
    {$video.s_day}<br>
    {$video.s_archive}<br>
</div>

</div>
{/foreach}

</body>
</html>