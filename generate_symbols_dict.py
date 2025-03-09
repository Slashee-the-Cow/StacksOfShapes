import os

# --- Configuration ---
MODELS_SYMBOLS_DIR = os.path.join(os.path.dirname(__file__), "models", "symbols")
OUTPUT_DICT_FILE = "symbols_dict_output.txt"  # Output filename for the dictionary text

PATH_KEY = "PATH_KEY" # Replicate your PATH_KEY and TOOLTIP_KEY constants - for clarity in generated dict
TOOLTIP_KEY = "TOOLTIP"
ALT_TOOLTIP_KEY = "ALT_TOOLTIP"

def generate_symbols_dictionary():
    """Generates a Python dictionary representation of symbols from the models/symbols directory."""
    symbols_dict = {}

    category_folders = [
        folder for folder in os.listdir(MODELS_SYMBOLS_DIR)
        if os.path.isdir(os.path.join(MODELS_SYMBOLS_DIR, folder))
    ]

    for category_folder in category_folders:
        category_dict = {}
        category_path = os.path.join(MODELS_SYMBOLS_DIR, category_folder)
        stl_files = [
            f for f in os.listdir(category_path)
            if f.lower().endswith(".stl")
        ]

        for stl_file in stl_files:
            symbol_name_base = os.path.splitext(stl_file)[0]  # Filename without extension
            symbol_name_pretty = symbol_name_base.replace("_", " ").title() # Basic filename to pretty name - adjust as needed
            symbol_key = f'catalog.i18nc("symbol_name", "{symbol_name_pretty}")' # Create catalog.i18nc key - adjust name format if needed

            relative_path = os.path.join("symbols", category_folder, stl_file) # Construct relative path
            category_dict[symbol_key] = {
                PATH_KEY: relative_path.replace("\\", "/"),
                TOOLTIP_KEY: "", # Empty tooltip - you'll fill this in manually
                ALT_TOOLTIP_KEY: "",
                "BASE_NAME": symbol_name_base,
            }

        category_key = f"_symbols_category_{category_folder.lower()}" # Category key based on folder name
        symbols_dict[category_key] = category_dict

    return symbols_dict

def nameFromCategoryKey(category_key: str) -> str:
    return '_'.join(category_key.split('_')[3:])

if __name__ == "__main__":
    generated_dict = generate_symbols_dictionary()

    # --- Output to .txt file ---
    with open(OUTPUT_DICT_FILE, "w") as outfile:
        # Import and set active i18n catalog
        outfile.write("from UM.i18n import i18nCatalog\ncatalog = i18nCatalog(\"stacksofshapes\")\n\n")
        # Insert constants which I really should grab from another file but whatever
        outfile.write("PATH_KEY: str = \"path\"\n")
        outfile.write("TOOLTIP_KEY: str = \"tooltip\"\n")
        outfile.write("ALT_TOOLTIP_KEY: str = \"altTooltip\"\n\n")
        
        # Create definitions for each folder key
        for category_key in generated_dict.keys():
            outfile.write(f"{category_key}: str = catalog.i18nc(\"symbol_category\", \"{nameFromCategoryKey(category_key)}\")\n")

        outfile.write("\nSymbols = {\n") # Start of dictionary

        for category_key, category_symbols in generated_dict.items():
            outfile.write(f"    {category_key}: {{\n") # Category comment

            for symbol_key, symbol_data in category_symbols.items():
                outfile.write(f"        {symbol_key}: {{\n") # Symbol key
                outfile.write(f"            {PATH_KEY}: \"{symbol_data[PATH_KEY]}\",\n") # PATH_KEY
                outfile.write(f'            {TOOLTIP_KEY}: catalog.i18nc("symbol_tooltip_{nameFromCategoryKey(category_key)}:{symbol_data["BASE_NAME"]}", ""),\n') # TOOLTIP_KEY - empty
                outfile.write(f'            {ALT_TOOLTIP_KEY}: catalog.i18nc("symbol_alt_tooltip_{nameFromCategoryKey(category_key)}:{symbol_data["BASE_NAME"]}", ""),\n') # TOOLTIP_KEY - empty
                outfile.write(f"        }},\n") # End of symbol entry
            outfile.write(f"    }},\n\n") # End of category

        outfile.write("}\n") # End of dictionary

        outfile.write(f"\nSymbol_Category_Tooltips = {{\n")
        for category_key in generated_dict.keys():
            outfile.write(f"    {category_key}: catalog.i18nc(\"category_tooltip\",\"\"),\n")
            outfile.write(f"    {category_key}_alt: catalog.i18nc(\"category_tooltip_alt\",\"\"),\n")
        outfile.write(f"}}\n")  # Close dictionary

        outfile.write(f"\nSymbol_Category_Thumbnail_Filenames = {{\n")
        for category_key in generated_dict.keys():
            outfile.write(f"    {category_key}: \"symbols/{nameFromCategoryKey(category_key)}.png\",\n")
        outfile.write(f"}}\n")  # Close dictionary

    print(f"Symbols dictionary generated and saved to: {OUTPUT_DICT_FILE}")