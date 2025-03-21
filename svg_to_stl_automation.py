import os
import subprocess
import platform # For platform detection
import tempfile
import shutil

# --- Configuration --- (Keep paths configurable)
SVG_INPUT_DIR = os.path.join(os.path.dirname(__file__), "symbols")
STL_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "models", "symbols")
OPENSCAD_EXECUTABLE = "openscad"
DEFAULT_EXTRUDE_HEIGHT = 5.0
EXPORT_FORMAT = "binstl"

# --- Platform-specific OpenSCAD executable ---
if platform.system() == "Windows": # Check for Windows
    OPENSCAD_EXECUTABLE = "openscad.com" # Use openscad.com on Windows
else:
    OPENSCAD_EXECUTABLE = "openscad" # Default to "openscad" (assuming it's in the system's PATH)


# Ensure output directory exists
os.makedirs(STL_OUTPUT_DIR, exist_ok=True)

def svg_to_stl(svg_filepath, stl_output_filepath, extrusion_height):

    svg_filepath_forward_slashes = os.path.abspath(svg_filepath).replace('\\', '/') # <--- Convert to forward slashes!

    """Converts an SVG file to STL using OpenSCAD."""
    openscad_script = f"""
resize([50,0,0], auto=[true,true,false])
    linear_extrude(height = {extrusion_height}, center = false)
        import("{svg_filepath_forward_slashes}", center= true); // Absolute path in import() - KEEP
"""
    try:
        # Create a temporary file with .scad extension - using 'with' for automatic deletion
        with tempfile.NamedTemporaryFile(mode="w", suffix=".scad", delete=False) as tmp_scad_file: # delete=False for now, we'll manually delete later for debugging
            tmp_scad_filepath = tmp_scad_file.name # Get the temporary file path
            tmp_scad_file.write(openscad_script) # Write the OpenSCAD script to the temp file
            tmp_scad_file.flush() # Ensure content is written to disk

        # Make sure temporary file loads fine
        print(f"Temporary .scad file content: {tmp_scad_filepath}")
        try:
            with open(tmp_scad_filepath, "r") as f:  # Re-open to read content
                print(f.read())  # Print the content of the temp .scad file
        except Exception as e_read: # Catch potential read errors (though unlikely here)
            print(f"Error reading temporary file for logging: {e_read}")
        finally:
            print(f"End of temporary .scad file content")


        command = [OPENSCAD_EXECUTABLE, "-o", stl_output_filepath, "--export-format", f"{EXPORT_FORMAT}", tmp_scad_filepath] #  <--- Use tmp_scad_filepath as input! NO SVG FILE PATH at the end
        print(f"Executing OpenSCAD command: {command}") # Log command

        process = subprocess.Popen(command, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        return_code = process.returncode

        if return_code == 0:
            print(f"Successfully converted: {svg_filepath} -> {stl_output_filepath}")
            return True
        else:
            print(f"Error converting {svg_filepath} (Return Code: {return_code}):")
            print(f"  Stderr:\n{stderr}")
            return False

    except FileNotFoundError:
        print(f"Error: OpenSCAD executable not found. Please ensure '{OPENSCAD_EXECUTABLE}' is correctly configured.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred during SVG to STL conversion for {svg_filepath}: {e}")
        return False
    finally: # Ensure temporary file is deleted, even if errors occur
        if os.path.exists(tmp_scad_filepath): # Double check file exists before deleting
            os.remove(tmp_scad_filepath) # Manually delete temporary .scad file
            print(f"Deleted temporary file: {tmp_scad_filepath}") # Log deletion for debugging (optional)


if __name__ == "__main__":
    svg_files_with_paths = [] # List to store tuples of (svg_filepath, relative_path)

    for root, _, files in os.walk(SVG_INPUT_DIR):  # Recursively walk symbols folder.
        for filename in files:
            if filename.lower().endswith(".svg"):
                svg_filepath = os.path.join(root, filename)
                relative_path = os.path.relpath(svg_filepath, SVG_INPUT_DIR) # Get relative path from SVG_INPUT_DIR
                svg_files_with_paths.append((svg_filepath, relative_path)) # Store filepath and relative path

    if not svg_files_with_paths:
        print(f"No SVG files found in input directory (recursive search): {SVG_INPUT_DIR}")
    else:
        print(f"Found {len(svg_files_with_paths)} SVG files (recursive) in: {SVG_INPUT_DIR}")
        for svg_filepath, relative_path in svg_files_with_paths: # Loop through filepaths and relative paths
            stl_filename_relative = os.path.splitext(relative_path)[0] + ".stl" # STL filename from relative SVG path
            stl_output_filepath_relative = os.path.join(STL_OUTPUT_DIR, stl_filename_relative) # Output STL path
            if os.path.exists(stl_output_filepath_relative):
                print(f"Skipping {stl_output_filepath_relative} as it already exists")
                continue

            stl_output_dir_for_file = os.path.dirname(stl_output_filepath_relative) # Ensure output directory for THIS FILE exists
            os.makedirs(stl_output_dir_for_file, exist_ok=True) # Create directory if it doesn't exist

            svg_to_stl(svg_filepath, stl_output_filepath_relative, DEFAULT_EXTRUDE_HEIGHT) # Convert each SVG to STL - using relative output path

            stl_output_dir_for_file = os.path.dirname(stl_output_filepath_relative) # Get the output directory (already defined, but geting our own copy
            svg_output_filepath = os.path.join(stl_output_dir_for_file, os.path.basename(svg_filepath)) # Output SVG path - same name, same directory as STL
            try:
                shutil.copy(svg_filepath, svg_output_filepath) # Copy SVG, for thumbnail
                print(f"Successfully copied SVG thumbnail: {svg_filepath} -> {svg_output_filepath}")
            except Exception as e_copy_svg:
                print(f"Error copying SVG thumbnail: {svg_filepath} -> {svg_output_filepath}: {e_copy_svg}")
        # --- End of SVG thumbnail copy ---

    print("SVG to STL conversion process finished (recursive, folder structure preserved).")