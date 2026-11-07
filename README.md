# KovaaK's Score Tracker

Python script which reads my KovaaK's stats and shows my best score for each scenario along with the date. I built it to see all my best scores in one place. It was able to handle 537 of my runs across 134 scenarios.

## Example Output

    1w2ts Pasu Perfected Easy: 99.0 - 2026.09.28
    1w2ts reload: 78.0 - 2026.09.29
    1w2ts reload smallflicks larger: 130.0 - 2026.10.02

## How to run

You need Python 3 and KovaaK's installed.

1. Open 'main.py' and set 'folder' to your KovaaK's stat folder.
2. Run 'python main.py'.

## How it works

KovaaK's saves each run in a stats folder as CSV files. The script simply goes through each file and finds the 'Score:' and 'Scenario:' lines and keeps the highest score for each senario in a dictionary. Then it reads the file name and splits it to get the date for that scenario.

## Planned Features

- Funcitonal user interface
- Show charts and cool graphs

## Development notes

This was my first project outside of my python course. I coded it myself to reinforce my understanding of the basics. Still, I found it difficult and had to ask to help with the OS module.