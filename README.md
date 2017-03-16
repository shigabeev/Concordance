# Concordance
<p>Python project for finding context for each word in text</p>

## Usage:
<p>
    <br> this script takes 4 optional arguments, to run it from terminal you'll need python 3
    <pre>$ python3 concordance.py Data 2 2 DB.json</pre>
    <br> Takes 4 arguments:
    <ol>
        <li> Folder with data(Data by default).</li>
        <li> Left context</li>
        <li> Right context</li>
        <li> JSON to grab data from</li>
    </ol>
    <br> Settings are selected right in code.
    <br> Defaults settings are:
</p>
<ul>
    <li>left = 2    - left context</li>
    <li>right = 2   - right context</li>
    <li>start_line = 30 - which lines to scan. Limited for testing purposes</li>
    <li>end_line = 100</li>
    <li>export = "DB.json"  - where to save result</li>
</ul>