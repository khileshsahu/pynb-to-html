import nbformat
from nbconvert import HTMLExporter
import os

def convert_ipynb_to_html(input_file, output_file=None):
    """
    Converts a Jupyter Notebook (.ipynb) file to an HTML file.

    Args:
        input_file (str): Path to the input .ipynb file.
        output_file (str, optional): Path to the output HTML file. If not provided, 
                                     the output will have the same name as the input file with .html extension.

    Returns:
        str: Path to the generated HTML file.
    """
    if not input_file.endswith('.ipynb'):
        raise ValueError("Input file must be a .ipynb file")

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' does not exist")

    # Set the output file name
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.html'

    # Load the notebook
    with open(input_file, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    # Convert the notebook to HTML
    html_exporter = HTMLExporter()
    #html_exporter.exclude_input = True  # Exclude code cells (optional, remove if not needed)
    body, _ = html_exporter.from_notebook_node(notebook)

    # Write the HTML output to a file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(body)

    print(f"HTML file created: {output_file}")
    return output_file

# Example usage
if __name__ == "__main__":
    input_path = input("Enter the path to the .ipynb file: ").strip()
    output_path = input("Enter the desired output path for the .html file (or press Enter to use default): ").strip()

    if not output_path:
        output_path = None  # Use default output path

    try:
        convert_ipynb_to_html(input_path, output_path)
    except Exception as e:
        print(f"Error: {e}")
