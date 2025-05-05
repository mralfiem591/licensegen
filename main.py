import os
import json
import datetime
import requests  # Add this to your imports

def generate_license():
    """Generates a LICENSE file based on user selection from JSON templates."""
    os.system("cls" if os.name == "nt" else "clear")
    os.makedirs(os.path.join(os.path.dirname(__file__), "generated"), exist_ok=True)
    os.makedirs(os.path.join(os.path.dirname(__file__), "licenses"), exist_ok=True)
    licenses_dir = os.path.join(os.path.dirname(__file__), "licenses")
    available_licenses = {}

    # Read available licenses from JSON files in the 'licenses' directory
    for filename in os.listdir(licenses_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(licenses_dir, filename)
            try:
                with open(filepath, 'r') as f:
                    license_data = json.load(f)
                    license_name = license_data.get("meta", {}).get("name")
                    if license_name:
                        available_licenses[license_name] = license_data["data"]["license"]
                    else:
                        print(f"Warning: '{filename}' is missing the 'meta.name' field.")
            except json.JSONDecodeError:
                print(f"Warning: Could not decode JSON from '{filename}'.")
            except KeyError:
                print(f"Warning: '{filename}' is missing the 'data.license' field.")

    if not available_licenses:
        print("No valid license templates found in the 'licenses' directory.")
        if input("Do you want to download a new license template from GitHub? (y/n): ").lower() == 'y':
            download_license_from_github()
        return

    # Display the menu of available licenses
    license_names = sorted(available_licenses.keys())
    print("Available Licenses:")
    # license_names is already sorted above
    for i, name in enumerate(license_names):
        print(f"{i + 1}. {name}")

    # Get user's choice
    while True:
        try:
            choice = input("Enter the number of the license you want to use (or 'git' to get a new one): ")
            if choice.lower() == 'git':
                download_license_from_github()
                return
            license_index = int(choice) - 1
            if 0 <= license_index < len(license_names):
                selected_license_name = license_names[license_index]
                license_template = available_licenses[selected_license_name]
                break
            else:
                print("Invalid selection. Please enter a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get year and copyright holder information
    if license_template.__contains__("<YEAR>"):
        current_year = datetime.datetime.now().year
        year = input(f"Enter the copyright year (default: {current_year}): ") or str(current_year)
    else:
        print("This template does not require a year.")
        year = ""  # Default to empty if <YEAR> is not in the template
    if license_template.__contains__("<COPYRIGHT HOLDER>"):
        copyright_holder = input("Enter the copyright holder name: ")
    else:
        print("This template does not require a copyright holder.")
        copyright_holder = ""  # Default to empty if <COPYRIGHT HOLDER> is not in the template

    # Replace placeholders in the license text
    generated_license = license_template.replace("<YEAR>", year).replace("<COPYRIGHT HOLDER>", copyright_holder)

    # Write the license to a LICENSE file
    with open(os.path.join(os.path.dirname(__file__), "generated", "LICENSE"), "w") as f:
        f.write(generated_license)

    print(f"LICENSE file generated successfully, in {os.path.join(os.path.dirname(__file__), 'generated', 'LICENSE')}!")

def download_license_from_github():
    """Download a license JSON file from a GitHub repository."""
    os.system("cls" if os.name == "nt" else "clear")
    github_repo = "https://api.github.com/repos/mralfiem591/licenses/contents"
    licenses_dir = os.path.join(os.path.dirname(__file__), "licenses")

    try:
        # Fetch the list of files in the GitHub repo directory
        response = requests.get(github_repo)
        response.raise_for_status()
        files = response.json()

        # List available files
        print("Available licenses in the GitHub repository:")
        json_files = [file for file in files if file["name"].endswith(".json")]
        for i, file in enumerate(json_files):
            print(f"{i + 1}. {file['name']}")

        # Get user's choice
        choice = int(input("Enter the number of the license you want to download: ")) - 1
        if 0 <= choice < len(json_files):
            selected_file = json_files[choice]
            download_url = selected_file["download_url"]

            # Download the selected file
            response = requests.get(download_url)
            response.raise_for_status()

            # Save the file to the licenses directory
            with open(os.path.join(licenses_dir, selected_file["name"]), "w") as f:
                f.write(response.text)

            print(f"License '{selected_file['name']}' downloaded successfully to the 'licenses' directory.")
        else:
            print("Invalid selection.")
    except requests.RequestException as e:
        print(f"Error fetching licenses from GitHub: {e}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    generate_license()