# Python_Scroll_Package

**Python_Scroll_Package** is a versatile package that allows users to analyze and manipulate text documents and perform various statistical tests on the data.

## Features
- Extract text from .txt and .docx files.
- Preprocess the text data by cleaning, removing big dots and tab characters, and removing content between specified symbols.
- Calculate word counts and auxiliary tables for further analysis, such as row's length variance, number of rows in columns, and counts of corrections.
- Apply base statistical tests functions (including Wald test and comparison of column distribution) for statistical analysis and comparisons between different writers based on their texts.
- Utilize permutation tests for enhanced analysis and additional insights into the data.
- Create visual graphs to summarize the data and facilitate easier understanding.

## Getting Started
These instructions will help you set up the necessary tools to use the Python_Scroll_Package.

1. Clone the repository or download the package as a .zip file.
2. Install the required packages:
pip install -r requirements.txt

3. Run the following command to install the package in an editable mode:
pip install -e .

4. Now you can use the package by importing it in your Python script:
```python
import Python_Scroll_Package
Usage
The Python_Scroll_Package provides various functionalities and utilities to analyze and manipulate text documents. Here are a few examples of how to use the package:

# Import the Python_Scroll_Package
import Python_Scroll_Package

# Create an instance of the Python_Scroll class
scroll = Python_Scroll_Package.Python_Scroll("example_text.txt")

# Clean the data by removing unwanted characters and content
scroll.clean_data()

# Calculate word counts
scroll.word_counts([("word1", "word2")])

# Perform statistical tests
scroll.statistical_tests(start_1=1, stop_1=10, start_2=11, stop_2=20)

# Generate graphs for better understanding
scroll.plot_single_column_data("path_to_save_plots")
```

For more detailed usage instructions, please refer to the documentation.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License.
