# FITS Metadata Extraction Pipeline

A Python-based automated data pipeline designed to parse, extract, and standardize header metadata from Flexible Image Transport System (FITS) files commonly used in astronomical and heliophysics research (e.g., NASA SDO/AIA, SOHO).

The pipeline extracts key observational metadata such as telescope, instrument, observation timestamps, and exposure times, and aggregates them into a structured JSON catalog.

## Key Features

Automated Batch Processing: Ingests entire directories of .fits and .FITS data files.

Defensive Parsing: Handles missing or non-standard header keys using fallback values.

Resource Management: Utilizes Python context managers (`with` statements) to prevent memory leaks during batch operations.

Structured Output: Exports standardized records into a readable JSON catalog.

## Target Metadata Schema

The extractor captures these parameters (but can be customized to your liking):

TELESCOP -> telescope: Observatory or satellite name (Default: "UNKNOWN")

INSTRUME -> instrument: Specific onboard sensor/instrument (Default: "UNKNOWN")

DATE-OBS -> obs_date: UTC date/time of observation (Default: "N/A")

EXPTIME -> exposure_time: Exposure duration in seconds (Default: 0.0)

## Prerequisites

Python 3.8+

astropy library

Install dependencies using pip:

`python -m pip install astropy`

## Installation & Usage

Clone this repository:

`git clone https://github.com/dsoon0400/FIT-file-metadata-extraction.git`

`cd FitHeaderExtractor`

Run the extraction script:

`python fitheaderextractor.py`

View the generated JSON catalog in `metadata_catalog.json`.

## Sample Output
`
[

  {
  
    "filename": "sample.fits",
    
    "telescope": "HST",
    
    "instrument": "WFPC2",
    
    "obs_date": "1999-02-20",
    
    "exposure_time": 300.0
    
  }
  
]
`
You can upload your own .fit and .FIT files into your project directory to parse them; the script will parse all .FIT and .fit files within the project directory.

## Tech Stack

Languages: Python 3

Libraries: astropy.io.fits, os, glob, json
