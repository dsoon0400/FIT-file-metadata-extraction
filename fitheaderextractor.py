from astropy.io import fits
import glob, json, os


def extract_fits_metadata(directory):

    # Initialize an empty list to store metadata records
    records = []

    # Find all FITS files in the specified directory (case-insensitive)
    fits_files = list(
        set(
        glob.glob(os.path.join(directory, "*.fits")) + 
        glob.glob(os.path.join(directory, "*.FITS"))
        )
    )

    # Process each FITS file and extract metadata
    for filepath in fits_files:
        with fits.open(filepath) as hdul:
            header = hdul[0].header
            metadata = {
                "filename": os.path.basename(filepath),
                "telescope": header.get("TELESCOP", "UNKNOWN"),
                "instrument": header.get("INSTRUME", "UNKNOWN"),
                "obs_date": header.get("DATE-OBS", "N/A"),
                "exposure_time": header.get("EXPTIME", 0.0),
            }
            records.append(metadata)

    # Save output catalog
    output_path = os.path.join(directory, "metadata_catalog.json")
    with open(output_path, "w") as result_file:
        json.dump(records, result_file, indent=2)

    # Print summary of processed files
    print(
        f"Successfully processed {len(records)} files. Output saved to: {output_path}"
    )


# Execute using raw string notation for Windows paths, can replace with any directory path needed
extract_fits_metadata("./")