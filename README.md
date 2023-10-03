# label-maker
HTML/Python Label Generator with Barcode

README.txt 

INSTALLATION

1) If python3 isn't already installed, run python-3.10.9-amd64.exe to install Python 3.10.9
2) To install the prerequisite libraries required to run the program, run runbefore.py. This will install the barcode making function alongside other functionalities required for the program to run.
3) Run labels.py.

FUNCTIONALITY

The program will take ingredients separated by the English comma (,), the Backslash (/) and the Chinese Comma (，）. If the translation doesn't work, check the spacing inbetween the commas. Backslash lists don't require spaces after each backslash.

When you press translate, it will come out with a translation in English with the allergens highlighted in bold and encased in astericks (*). Words that can't be translated will be encased in square brackets ([]) and will look like 【面条】. To rectify these errors, press the rectify error button and enter it's corresponding English translation. This will add the translation into dictionary.csv. Then press translate again and your amendments will be shown.

The program is also trained to look for E number blacklists. If a blaclisted E-number is shown, the program will look for an alternate E number to use and prompt the user to select which one they want to use. ONLY PRESS OKAY ONCE and say no to the other E numbers. Otherwise, multiple E numbers will be printed for a singular ingredient. 

Nestled in the Program button on the top-left hand side is the Open CSV and Open Blacklist. Press either one to edit the CSV/Blacklist. In these windows you have the ability to add and delete entries to the respective CSVs.

Press Create HTML Label to start the label making process. Energy is in KCal, All nutritional info is in Grams so is the weight. Storage and distributor are drop down menus and you can choose between different storage and distributor options. The barcode is in EAN-13 standard which is 12 digits long. The program will process the checkdigit for you. You can write directions of use in the text box at the bottom and when you're ready you can press "Process". This will create a .HTML file with the filename of the productnumber you specified. This is the label you've created. 
