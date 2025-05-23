from flask import Flask, jsonify, render_template, request
from functions import processData, subsDefault


app = Flask(__name__)


@app.route('/run', methods=['POST'])
def run():
    # Get file from the form
    try:
        substrates = request.files.get('textFile')
        loadFile = False
        if substrates:
            loadFile = True

            # Read the contents of the file
            substrate = substrates.read().decode('utf-8')

            # Split the content by lines to get each substrate sequence
            substrates = substrate.splitlines()
        else:
            # Use template substrates
            substrates = subsDefault()

    except Exception as e:
        return jsonify({"error": f"Error: {str(e)}"}), 400


    # Get other data from the form
    enzymeName = request.form.get('enzymeName') if loadFile else 'Template Enzyme'
    entropyMin = request.form.get('entropyMin')
    NSelect = int(request.form.get('N'))

    # if loadFile:
    # Evaluate: Data
    dataset = processData(substrates, entropyMin, NSelect, enzymeName, loadFile)

    result = {
        "enzyme": enzymeName,
        "entropyMin": entropyMin,
        "NSelect": NSelect,
        "NBinSubs": dataset['NBinSubs'],
        "figProb": dataset['probability'],
        "figEntropy": dataset['entropy'],
        "figLogo": dataset['pLogo'],
        "barCounts": dataset['barCounts'],
        "barProb": dataset['barProb'],
        "figWords": dataset['words'],
        "figTrie": dataset['trie']
    }

    return jsonify(result)


@app.route('/')
def home():
    return render_template('home.html',
        black='#151515', white='#FFFFFF',
        grey='#303030', greyDark='#202020',
        green='#23FF55', greenHighlight='#1AD747',
        spacer=20, spacerMini=5,
        padSide=50, padTB=30, padInput=8,
        marginB=12, marginButton=12,
        fontSize=16,
        borderRad=5,

    pg1="For enzymes that interact with protein and peptide substrates, this "
        "program will take profiling data for a given enzyme, and identify the "
        "Motif, or the recognition site, that is present within the larger protein "
        "sequence. The Motif is identified by the positions in the substrate that have "
        "an Entropy score (∆S) ≥ a user defined minimum ∆S value.",
    pg2="∆S is evaluated at each position in the substrate sequence and is found by "
        "calculating the difference between the Maximum Entropy (S<sub>Max</sub>) and "
        "the Shannon Entropy (S<sub>Shannon</sub>)<br>",
    equation="∆S = S<sub>Max</sub> - S<sub>Shannon</sub> = log<sub>2</sub>(20) - "
            "∑(-prob<sub>AA</sub> * log<sub>2</sub>(prob<sub>AA</sub>))",
    pg3="<br>Once the Motif has been have identified, the substrates are binned by "
        "selecting only the recognition sequence. In other words, the parts of the "
        "sequence that are not important for an Enzyme-Substrate interaction are "
        "removed.<br>- The non-important positions are identified by meeting the "
        "condition: ∆S < minimum ∆S",
    pg4="The program will then count the occurrences of each Motif, and collect the "
        "top \"N\" number of sequences. The subset is used to make Bar Graphs, and a "
        "Word Cloud. These figures display the most common combinations of active "
        "substrates within your dataset.",
    pg5="We can further evaluate the top Motifs by feeding the data into a Suffix "
        "Tree. This analysis will select the specific residues within the Motif, "
        "and plot the amino acids as nodes, with lines connecting the observed "
        "combinations of residues across the Motif. The figure reveals the unique "
        "preferences for a given amino acid when another is present in a preferred "
        "substrate.",
    )


if __name__ == '__main__':
    app.run(debug=True)
