# CURRENT DEV: 1.0.5

### Breaking changes
### New functions
- Added `save_data` and `save_data` for use in association with neuropsydia.ass
### Major changes
### Minor changes
- Added an icon and a name for the neuropsydia's window


# CURRENT STABLE: 1.0.3 (2017-03-03)

### Breaking changes
- `image()`: changed the default scaling: `size=1` now means 1 in neuropsydia's coordinates (20 = full screen)
- removed many functions related to statistics or signal processing to include them in [NeuroTools](https://github.com/neuropsychology/NeuroTools.py)


### New functions
- `Coordinates.from_physical()`: convert physical distances in cm  or inches to pixels
- `Coordinates.to_physical()`: convert neuropsydia's distances to cm  or inches to pixels
- `Time`: added now() method to Time class
- `start_screen()` and `end_screen()`: displaying logos and welcome screens
- `sound()`: plays wav sounds
- `opendoc()`: opens the neuropsydia github webpage
- `resting_state_brief_assessment()`: standardized resting state assessment
- Added `color_luminance()` and `color_contrast()` functions

### Major changes
- `image()`: support of size in cm or inches
- `instructions()`: Added `subtitle`, `top_space` parameter and color control

### Minor changes
- Added "teal" color style for scales

# CURRENT STABLE: 1.0.0 (2016-11-12)
Pushed to pypi!
### New functions
- `remove_following_duplicates()`: Remove the duplicates that are following themselves, returning a list of ordered items.
- `acq_to_df()`: read and format an BIOPAC's AcqKnowledge file into a Pandas' dataframe
- `get_creation_date()`: get creation date of a file
- `process_EDA()`: Thanks to [Luca Citi and Alberto Greco](http://ieeexplore.ieee.org/document/7229284/)
- `binarize_signal()`: signal processing
- `find_events()`: Find event onsets (signal processing)
- `select_events()`: Find and select event onsets (signal processing)
- `create_mne_events()`: Create MNE compatible events.
- `create_epochs()`: Create epoched data (signal processing)
- `create_evoked()`: Create evoked data (signal processing)

### Breaking changes
### Major changes


## 0.1.2 (2016-11-06)
- added two signal processing functions:
 - `extract_peaks()`
 - ~~`triggers_from_photodiode()`~~: removed for now. Will be replaced by a more universal function.


## 0.1.0 (2016-10-20)
- added `Trigger()` class to ease trigger sending (TTL, cedrus stimtracker or photosensor).

## 0.0.3
### Breaking Changes
- `background()` renamed to `newpage()`.
	- default parameter `auto_refresh` set to `True`.
- `background` argument in all functions renamed `background`.
