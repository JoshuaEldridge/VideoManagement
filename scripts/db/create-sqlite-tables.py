#!/usr/bin/python
import sqlite3
import os

home = os.path.expanduser("~")
conn = sqlite3.connect(os.path.join(home, 'Git/VideoManagement/video-library', 'home-video.db'))

c = conn.cursor()

c.execute('''CREATE TABLE source_videos
                (source_id integer primary key,
                    s_md5 text,
                    s_filename text,
                    s_codec_name text,
                    s_codec_long text,
                    s_codec_type text,
                    s_codec_tag text,
                    s_codec_tag_string text,
                    s_width integer,
                    s_height integer,
                    s_format text,
                    s_format_long text,
                    s_duration real,
                    s_size integer,
                    s_bit_rate integer,
                    s_timecode timestamp,
                    s_creation_time timestamp,
                    s_year integer,
                    s_month integer,
                    s_day integer,
                    s_archive_location boolean,
                    s_camera_name text,
                    s_scene_id_poster integer,
                    s_active boolean)''')

c.execute('''CREATE TABLE edited_videos
                (edited_id integer primary key,
                    source_id integer,
                    e_md5 text,
                    e_filename text,
                    e_length real,
                    e_scenes integer,
                    e_format text,
                    e_width integer,
                    e_height integer)''')

c.execute('''CREATE TABLE source_scenes
                (scene_id integer primary key,
                    source_id integer,
                    scene_active boolean,
                    scene_image text,
                    scene_ts real,
                    scene_desc text)''')

conn.commit()

conn.close()