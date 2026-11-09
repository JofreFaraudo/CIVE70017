# CIVE70017 Project
This is a repo with the only purpose to deal with the student project. No details about what it is will be provided whatsoever.
The data used is proprietary and confidential; therefore, it won't be uploaded.

## Usage
Download the provided data and unpack the zip inside a folder named `data_raw`, including parquets and excel files.
All output and auxiliary files will be stored inside the folder `data_parsed`, which should be created before running the code.

## TO-DO's
### Workflow for LTOs
1. Group all LTO combinations for aicraft, airport (icao code), and landing/takeoff (as bool) -> `count`.
2. Obtain, and append to new columns, unitary results from the unparsed cells (totals) -> `W40:48` or `AO40:48`.
3. Perform scaling to match actual number.

### Workflow for Main
