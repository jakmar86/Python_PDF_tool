# PDF Manipulation Tool

This is a basic Python script created for practicing Python. It uses the Tkinter library for the GUI and PyPDF2 for handling PDF files. The script allows you to select multiple PDF files, rearrange their order, and then merge them into a single PDF file. It also provides a function to split a PDF into separate pages.

## Features

- **Select PDF Files**: You can select multiple PDF files from your file system. The selected files will be displayed in a listbox, showing only the filenames for simplicity.
- **Rearrange Order**: You can rearrange the order of the selected PDF files using the "Move Up" and "Move Down" buttons. The order in the listbox will be the order in which the files are merged.
- **Merge PDFs**: You can merge the selected PDF files into a single PDF file. The merged file will contain all the pages from the selected files in the order they are listed in the listbox.
- **Split PDF**: You can split a PDF into separate pages. Each page will be saved as a separate PDF file.

## Usage

Run the script using Python 3. A window will open with buttons for selecting files, moving files up and down the list, and merging or splitting PDFs. Select the PDF files you want to merge, arrange them in the desired order, and then click "Merge PDFs" to merge the files. To split a PDF, select a single PDF file and click "Split PDF".

## Note

This is a basic script created for the purpose of practicing Python. It does not intend to include all the features of a fully-fledged PDF manipulation tool.
