# MOCHA: Motif Orientation and Characterization for High-throughput Assays

This bioinformatic analysis will analyze enzyme profiling data, and evaluate the specificity of your enzyme.

Input data must be in a text file, with 1 substrate per line.

- For an example of a correctly formatted file, refer to: exampleData.txt

# Install Modules:

You will need to install the following Python modules:

    pip install Flask
    pip install logomaker
    pip install networkx
    pip install seaborn
    pip install wordcloud

# Running the Program:

To use the program, run the app.py script.

The code will generate an IP address for a website that is hosted on your device. 

- Once the IP has been an displayed, click on it and the application will open in your browser.

Futher instructions will be displayed on the webpage.

# Limitations:

This tool is only compatable with enzymes that interact with protein sequences.

Input sequences can only contain the standard 20 amino acids:

    'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'

# Note:

Defending upon how long your extracted motif is, the Bar Graphs might cut of part of the sequence when working with longer motifs. Or they could have excessive space when displaying shorter motifs.

- To adjust the spacing on the bottom of the figure, open the script: functions.py

- Find the line where this function the is defined: plotBarGraph
    
- Adjust the "bottom" parameter in the line: fig.subplots_adjust(bottom=0.11)
