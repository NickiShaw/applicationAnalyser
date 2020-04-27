# applicationAnalyser
Used to process applications to the science ambassador team at UWaterloo. Although can be used generally for applications.
Main purposes are to:
* Remove names for application marking.
* Convert applications into PDF format (one file per applicant).


## Dependencies
* pandas
* reportlab


## Usage for UWaterloo Ambassadors
Input file should be application responses "without serial info" for UWaterloo ambassador applications.

Open appProcessing.py in a GUI of your choice (I use PyCharm).
* Make edits to all instances of PATH including adding the filenames for input (noted in code). To get a path to a file, right click on the file > properties, and copy the 'Location'.
* Add questions found in the input file to both `markingInfo` and `fullInfo`. These lists can also be edited so only the columns named appear in each output file.

Run code, do not view **fullInfo.csv** until marking of applicants has been completed.

Use the applicant_# packages as a user-friendly reading format.

When the applications have been marked merge the scores onto the fullInfo spreadsheet, done!


## Usage for alternative users
Input file should be a .csv file with questions as column headings and application responses as rows.

Open appProcessing.py in a GUI of your choice (I use PyCharm).
* Remove the `header=[2, ]` in line 5 if column headings start on the first row of your file.
* Make edits to all instances of PATH including adding the filenames for input (noted in code). To get a path to a file, right click on the file > properties, and copy the 'Location'.
* Edit the lists `markingInfo` and `fullInfo` to include the questions asked on the application (all info goes into fullInfo, but identity-sensitive information sould be omitted from markinInfo such as names). These lists can also be edited so only the columns named appear in each output file.
Run code, do not view **fullInfo.csv** until marking of applicants has been completed.

Use the applicant_# packages as a user-friendly reading format.

When the applications have been marked merge the scores onto the fullInfo spreadsheet, done!


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
