DROP DATABASE IF EXISTS media_library;
CREATE DATABASE media_library;
USE  media_library;
DROP TABLE IF EXISTS videos;
CREATE TABLE videos (
    video_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    md5 CHAR(32),
    filename VARCHAR(255),
    codec_name VARCHAR(35),
    codec_long VARCHAR(255),
    codec_type VARCHAR(25),
    codec_tag CHAR(10),
    codec_tag_string VARCHAR(25),
    width SMALLINT UNSIGNED,
    height SMALLINT UNSIGNED,
    format VARCHAR(75),
    format_long VARCHAR(255),
    duration DECIMAL(11, 6),
    size BIGINT UNSIGNED,
    bit_rate INT UNSIGNED,
    timecode CHAR(11),
    creation_time TIMESTAMP,
    year SMALLINT UNSIGNED,
    month TINYINT UNSIGNED,
    day TINYINT UNSIGNED,
    archive_flag BOOLEAN DEFAULT 0,
    camera_name VARCHAR(55),
    scene_id_poster INTEGER UNSIGNED,
    active_flag BOOLEAN,
    original_source_flag BOOLEAN,
    long_description TEXT,
    PRIMARY KEY (video_id)
);
drop table if exists scenes;
CREATE TABLE scenes (
    scene_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    video_id INTEGER UNSIGNED NOT NULL,
    active_flag BOOLEAN DEFAULT 1,
    image_name VARCHAR(125),
    ts DECIMAL(11, 6),
    description TINYTEXT,
    PRIMARY KEY (scene_id)
);
drop table if exists photos;
CREATE TABLE photos (
    photo_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    md5 CHAR(32),
    active_flag BOOLEAN DEFAULT 1,
    image_name VARCHAR(125),
    exif JSON,
    description TINYTEXT,
    year SMALLINT UNSIGNED,
    month TINYINT UNSIGNED,
    day TINYINT UNSIGNED,
    PRIMARY KEY (photo_id)
);
/* INSERT INTO photos (md5, image_name, exif, year, month, day) VALUES ('3a909cdb4e555b8ec0a56a2905532c1b', 'IMG_5370.JPG', 

'[{
  "SourceFile": "IMG_5369.JPG",
  "ExifToolVersion": 10.99,
  "FileName": "IMG_5369.JPG",
  "Directory": ".",
  "FileSize": "1691 kB",
  "FileModifyDate": "2018:01:31 12:01:46-05:00",
  "FileAccessDate": "2018:05:30 14:06:59-04:00",
  "FileInodeChangeDate": "2018:01:31 12:01:46-05:00",
  "FilePermissions": "rw-r--r--",
  "FileType": "JPEG",
  "FileTypeExtension": "jpg",
  "MIMEType": "image/jpeg",
  "ExifByteOrder": "Big-endian (Motorola, MM)",
  "Make": "Apple",
  "Model": "iPhone 6s",
  "Orientation": "Rotate 90 CW",
  "XResolution": 72,
  "YResolution": 72,
  "ResolutionUnit": "inches",
  "Software": "11.2.2",
  "ModifyDate": "2018:01:30 12:38:47",
  "YCbCrPositioning": "Centered",
  "ExposureTime": "1/247",
  "FNumber": 2.2,
  "ExposureProgram": "Program AE",
  "ISO": 25,
  "ExifVersion": "0221",
  "DateTimeOriginal": "2018:01:30 12:38:47",
  "CreateDate": "2018:01:30 12:38:47",
  "ComponentsConfiguration": "Y, Cb, Cr, -",
  "ShutterSpeedValue": "1/247",
  "ApertureValue": 2.2,
  "BrightnessValue": 7.523751523,
  "ExposureCompensation": 0,
  "MeteringMode": "Multi-segment",
  "Flash": "Auto, Did not fire",
  "FocalLength": "4.2 mm",
  "SubjectArea": "2015 1511 2956 1330",
  "RunTimeFlags": "Valid",
  "RunTimeValue": 83547346486000,
  "RunTimeScale": 1000000000,
  "RunTimeEpoch": 0,
  "AccelerationVector": "-0.01411850199 -0.9745644599 -0.2100189633",
  "SubSecTimeOriginal": "098",
  "SubSecTimeDigitized": "098",
  "FlashpixVersion": "0100",
  "ColorSpace": "sRGB",
  "ExifImageWidth": 4032,
  "ExifImageHeight": 3024,
  "SensingMethod": "One-chip color area",
  "SceneType": "Directly photographed",
  "ExposureMode": "Auto",
  "WhiteBalance": "Auto",
  "FocalLengthIn35mmFormat": "39 mm",
  "SceneCaptureType": "Standard",
  "LensInfo": "4.15mm f/2.2",
  "LensMake": "Apple",
  "LensModel": "iPhone 6s back camera 4.15mm f/2.2",
  "Compression": "JPEG (old-style)",
  "ThumbnailOffset": 1730,
  "ThumbnailLength": 14221,
  "ImageWidth": 3024,
  "ImageHeight": 3024,
  "EncodingProcess": "Baseline DCT, Huffman coding",
  "BitsPerSample": 8,
  "ColorComponents": 3,
  "YCbCrSubSampling": "YCbCr4:2:0 (2 2)",
  "Aperture": 2.2,
  "ImageSize": "3024x3024",
  "Megapixels": 9.1,
  "RunTimeSincePowerUp": "23:12:27",
  "ScaleFactor35efl": 9.4,
  "ShutterSpeed": "1/247",
  "SubSecCreateDate": "2018:01:30 12:38:47.098",
  "SubSecDateTimeOriginal": "2018:01:30 12:38:47.098",
  "ThumbnailImage": "(Binary data 14221 bytes, use -b option to extract)",
  "CircleOfConfusion": "0.003 mm",
  "FOV": "49.6 deg",
  "FocalLength35efl": "4.2 mm (35 mm equivalent: 39.0 mm)",
  "HyperfocalDistance": "2.45 m",
  "LightValue": 12.2
}]', 2018, 1, 31
);