Scripting - Variables
=======================

The following list of variables can be used anywhere:

.. list-table:: 
   :widths: 20 80
   :header-rows: 1

   * - **Variable**
     - **Description**
   * - %title%
     - Title of the track. If missing, the filename is returned instead
   * - %artist%
     - Artist of the track. If missing, the following fields are checked: Album Artist, Composer, Performer
   * - %uniqueartist%
     - Track artists not present in album artists
   * - %album%
     - Album name of the track
   * - %albumartist%
     - Album artist of the track. If missing, the following fields are checked: Artist, Composer, Performer
   * - %track%
     - Track number of the track within its album
   * - %tracktotal%
     - Total number of tracks in the album
   * - %disc%
     - Disc number of the track in the album
   * - %disctotal%
     - Total number of discs in the album
   * - %genre%
     - Genres of the track - separated by a comma
   * - %composer%
     - Composer of the track
   * - %performer%
     - Performer of the track
   * - %duration%
     - Duration of the track ([HH:]mm:ss)
   * - %duration_s%
     - Duration of the track in seconds
   * - %comment%
     - Comment tag
   * - %date%
     - Date of the track's release (yyyy-MM-dd)
   * - %year%
     - Year of the track's release
   * - %filesize%
     - Size of the file in bytes
   * - %bitrate%
     - Bitrate of the audio file (e.g. 1011 kbps)
   * - %samplerate%
     - Sample rate of the audio file (e.g. 44100 Hz)
   * - %firstplayed%
     - Datetime when the track was first played (yyyy-MM-dd HH:mm:ss)
   * - %lastplayed%
     - Datetime when the track was last played (yyyy-MM-dd HH:mm:ss)
   * - %playcount%
     - Number of times the track has been played
   * - %rating%
     - Rating of the track in the range 0.0-1.0
   * - %rating_stars%
     - Rating of the track in the range 1-10 (2=1 star)
   * - %codec%
     - Codec used to encode the audio file (e.g. PCM, FLAC). Returns the extension if empty.
   * - %channels%
     - Number of audio channels (e.g. Mono, Stereo, 6ch).
   * - %bitdepth%
     - Bit depth/bits per sample of the audio file
   * - %addedtime%
     - Datetime when the track was added to the library (yyyy-MM-dd HH:mm:ss)
   * - %lastmodified%
     - Datetime when the file was last modified (yyyy-MM-dd HH:mm:ss)
   * - %filepath%
     - Absolute file path to the audio file.
   * - %filename%
     - Filename without the extension
   * - %extension%
     - File extension (e.g. mp3, flac)
   * - %filename_ext%
     - Filename including the extension
   * - %directory%
     - Name of the containing directory
   * - %path%
     - Absolute path to the directory of the file
   * - %subsong%
     - Subsong index - used for multi-track files

The following list of variables can be used in the status bar:

.. list-table:: 
   :widths: 20 80
   :header-rows: 1

   * - **Variable**
     - **Description**
   * - %playback_time%
     - Elapsed time of the track ([HH:]mm:ss)
   * - %playback_time_s%
     - Elapsed time of the track (seconds)
   * - %playback_time_remaining%
     - Time remaining until the track ends ([HH:]mm:ss)
   * - %playback_time_remaining_s%
     - Time remaining until the track ends (seconds)