# License Generator

This project is a Python-based license generator that allows users to create `LICENSE` files for their projects. It supports multiple license templates and provides the ability to download additional license templates from a GitHub repository.

## Features

- Generate a `LICENSE` file from pre-defined JSON templates.
- Supports popular licenses such as MIT, Apache 2.0, GPL 3.0, and more.
- Allows users to download new license templates from a GitHub repository.
- Automatically replaces placeholders like `<YEAR>` and `<COPYRIGHT HOLDER>` in the license text.

## Licenses

### Built-In

- MIT License (mit.json)
- Public Domain (pd.json)

## Downloadable

- Academic Free License v3.0 (afl-3.0.json)
- Apache License 2.0 (apache-2.0.json)
- Artistic License 2.0 (artistic-2.0.json)
- Boost Software License 1.0 (boost-1.0.json)
- BSD 3-Clause License (bsd-3-clause.json)
- Creative Commons Zero v1.0 Universal (cc0-1.0.json)
- Eclipse Public License 2.0 (epl-2.0.json)
- GNU General Public License v3.0 (gpl-3.0.json)
- ISC License (isc.json)
- MIT License (mit.json)
- Mozilla Public License 2.0 (mpl-2.0.json)
- Open Software License 3.0 (osl-3.0.json)
- Public Domain (pd.json)
- The Unlicense (unlicense.json)
- Zlib License (zlib.json)

## Prerequisites

- Python 3.6 or higher
- Internet connection (for downloading licenses from GitHub)

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd license
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```bash
    python main.py
    ```

2. Follow the prompts to:
   - Select a license from the available templates.
   - Enter the required details (e.g., year, copyright holder).
   - Generate the `LICENSE` file.

3. To download new license templates from a GitHub repository, type `git` when prompted.

## Directory Structure

- main.py: The main script for generating licenses.
- licenses/: Directory containing JSON license templates.
- generated/: Directory where the generated `LICENSE` file will be saved.

## Adding New Licenses

To add a new license manually:

1. Create a JSON file in the `licenses` directory.
2. Follow the format of existing license JSON files (e.g., `meta` and `data` fields).

## Example

When you run the script, you will see a menu of available licenses. Select a license by entering its number, and the script will guide you through the process of generating a `LICENSE` file.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
