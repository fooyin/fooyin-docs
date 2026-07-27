Scripting - Variables
=====================

Variable availability depends on the context in which a script is evaluated.
Metadata variables require a track, while playlist, queue, playback, library, and
system variables are provided by the relevant user-interface components.

Metadata
--------

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Variable**
     - **Description**
   * - ``%title%``
     - Track title. If missing, the filename is returned instead
   * - ``%artist%``
     - Artists. If missing, Album Artist, Composer, and Performer are checked
   * - ``%uniqueartist%``
     - Unique artists not present in album artists
   * - ``%album%``
     - Album title
   * - ``%albumartist%``
     - Album artist. If missing, Artist, Composer, and Performer are checked
   * - ``%track%``
     - Track number
   * - ``%tracktotal%``
     - Total tracks on the release
   * - ``%disc%``
     - Disc number
   * - ``%disctotal%``
     - Total discs on the release
   * - ``%genre%``
     - Genres, separated by a comma
   * - ``%composer%``
     - Composers
   * - ``%performer%``
     - Performers
   * - ``%duration%``
     - Track duration formatted as ``[HH:]mm:ss``
   * - ``%duration_s%``
     - Track duration in seconds
   * - ``%duration_ms%``
     - Track duration in milliseconds
   * - ``%comment%``
     - Comment tag
   * - ``%date%``
     - Release date
   * - ``%year%``
     - Release year
   * - ``%filesize%``
     - File size in bytes
   * - ``%filesize_natural%``
     - Human-readable file size
   * - ``%bitrate%``
     - Track bitrate
   * - ``%samplerate%``
     - Sample rate
   * - ``%bitdepth%``
     - Bit depth
   * - ``%firstplayed%``
     - First played timestamp
   * - ``%lastplayed%``
     - Last played timestamp
   * - ``%playcount%``
     - Play count
   * - ``%rating%``
     - Numeric rating in stars
   * - ``%rating_normalized%``
     - Normalised rating
   * - ``%stars%``
     - Numeric rating in stars
   * - ``%rating_stars%``
     - Rating shown as stars
   * - ``%rating_stars_padded%``
     - Rating shown as stars with trailing empty stars
   * - ``%rating_editor%``
     - Rating editor representation
   * - ``%codec%``
     - Codec name. If missing, the file extension is returned instead
   * - ``%codec_profile%``
     - Codec profile
   * - ``%tool%``
     - Encoding tool
   * - ``%tagtype%``
     - Tag type list
   * - ``%encoding%``
     - Encoding description
   * - ``%channels%``
     - Channel layout
   * - ``%createdtime%``
     - File creation timestamp
   * - ``%addedtime%``
     - Timestamp at which the track was added to the library
   * - ``%lastmodified%``
     - File's last-modified timestamp
   * - ``%filepath%``
     - Full file path
   * - ``%relativepath%``
     - Path relative to the library root
   * - ``%filename%``
     - Filename without the extension
   * - ``%extension%``
     - File extension
   * - ``%filename_ext%``
     - Filename including the extension
   * - ``%directory%``
     - Containing directory name
   * - ``%path%``
     - Containing directory path
   * - ``%subsong%``
     - Subsong index, used for multi-track files
   * - ``%replaygain_track_gain%``
     - ReplayGain track gain
   * - ``%replaygain_track_peak%``
     - ReplayGain track peak
   * - ``%replaygain_track_peak_db%``
     - ReplayGain track peak in dB
   * - ``%replaygain_album_gain%``
     - ReplayGain album gain
   * - ``%replaygain_album_peak%``
     - ReplayGain album peak
   * - ``%replaygain_album_peak_db%``
     - ReplayGain album peak in dB

Playlist
--------

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Variable**
     - **Description**
   * - ``%trackcount%``
     - Number of tracks in the list
   * - ``%playtime%``
     - Combined duration of the track list
   * - ``%playlist_size%``
     - Combined file size of the track list
   * - ``%playlist_duration%``
     - Alias for the total playlist duration
   * - ``%genres%``
     - Unique genres across the track list

Queue
-----

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Variable**
     - **Description**
   * - ``%queue_index%``
     - First playback queue index for the specified item
   * - ``%queue_indexes%``
     - Playback queue indexes for the specified item
   * - ``%queue_total%``
     - Total number of tracks in the playback queue for queued items

Playback
--------

These variables are available in playback-aware contexts such as the status bar.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Variable**
     - **Description**
   * - ``%playlist_elapsed%``
     - Elapsed time within the active playlist
   * - ``%playback_time%``
     - Current playback position formatted as ``[HH:]mm:ss``
   * - ``%playback_time_s%``
     - Current playback position in seconds
   * - ``%playback_time_remaining%``
     - Remaining playback time formatted as ``[HH:]mm:ss``
   * - ``%playback_time_remaining_s%``
     - Remaining playback time in seconds
   * - ``%isplaying%``
     - Returns 1 while playback is active
   * - ``%ispaused%``
     - Returns 1 while playback is paused
   * - ``%isstopped%``
     - Returns 1 while playback is stopped

Library and system
------------------

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Variable**
     - **Description**
   * - ``%libraryname%``
     - Current library name
   * - ``%librarypath%``
     - Current library path
   * - ``%datetime%``
     - Current date and time formatted as ``YYYY-MM-DD HH:MM:SS``
