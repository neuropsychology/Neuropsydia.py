# CURRENT DEV: 1.0.0
### New functions
- `remove_following_duplicates()`: Remove the duplicates that are following themselves, returning a list of ordered items.


# CURRENT STABLE: 0.1.3 (2016-11-12)
Pushed to pypi!
### New functions
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
