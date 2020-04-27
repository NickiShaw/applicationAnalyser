import pandas

# Import application responses "without serial info" on download option.
# Aplications are notmally output with two dummy rows before the headers and responses, which are removed in this case.
df = pandas.read_csv('C:/PATH/APPLICATION RESPONSES.csv', header=[2, ]) # ADD path and file name for .csv containing applcation responses.

# Check that 'Serial' is the first header in input dataframe (can be omitted if 'serial' is not applicable column name).
print('Data was imported with correct columns.') if df.columns[0] == 'Serial' else print('Columns are formatted '
                                                                                         'incorrectly.')
# Create list of questions to filter for making report.
markingInfo = ['Serial', 'Program', 'Co-op', 'What term will you be entering Fall 20xx?', # input year here.
               'Do you understand the requirements of this position, which will include mandatory training and events on evenings and weekends?',
               'Question 1',
               'Question 2',
               'Question 3',
               'Question 4',
               'Question 5'] # insert/edit questions as written on application form (omitted for privacy).

# Subset df with columns in markingInfo.
markingDf = df.reindex(markingInfo, axis='columns')

# Check that all questions in markingInfo were present in markingDf, if true export csv file.
if all(markingDf.columns == markingInfo):
    print('All questions in markingInfo were found')
    markingDf.to_csv('C:/PATH/markinginfo_ambapplication.csv', index=False) # ADD PATH.
else:
    print('NOT all questions in markingInfo were found')

# Create list of questions for full report (for cross-cehcking names when marking is complete).
fullInfo = ['Serial', 'Full Name', 'Preferred Name', 'UWaterloo Email', 'Program', 'Co-op',
            'What term will you be entering Fall 20xx?',  # input year here.
            'Do you understand the requirements of this position, which will include mandatory training and events on evenings and weekends?',
            'Question 1',
            'Question 2',
            'Question 3',
            'Question 4',
            'Question 5']  # insert/edit questions as written on application form (omitted for privacy).

# Subset df with columns in fullInfo.
fullDf = df.reindex(fullInfo, axis='columns')

# Check that all questions in fullInfo were present in fullDf, if true export csv file.
if all(fullDf.columns == fullInfo):
    print('All questions in fullInfo were found')
    fullDf.to_csv('C:/PATH/fullinfo_ambapplication.csv', index=False) # ADD PATH.
else:
    print('NOT all questions in fullInfo were found')

# Create applicant packages in more readable pdf format.
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm

# Format page.
PAGESIZE = (140 * mm, 216 * mm)
BASE_MARGIN = 5 * mm

# Format title.
def get_title_style():
    sample_style_sheet = getSampleStyleSheet()
    title_style = sample_style_sheet['Heading1']
    title_style.fontSize = 18
    return title_style

# Format headings for questions.
def get_heading_style():
    sample_style_sheet = getSampleStyleSheet()
    heading_style = sample_style_sheet['Heading2']
    heading_style.fontSize = 10
    return heading_style

# Format body for answers.
def get_body_style():
    sample_style_sheet = getSampleStyleSheet()
    body_style = sample_style_sheet['BodyText']
    body_style.fontSize = 10
    return body_style

# Build readable application pdfs.
def build_pdf(appRow):
    pdf_buffer = 'C:/PATH/Applicant_' + str(markingDf.loc[appRow, 'Serial']) + '.pdf' # ADD PATH.
    my_doc = SimpleDocTemplate(
       pdf_buffer,
        pagesize=PAGESIZE,
        topMargin=BASE_MARGIN,
        leftMargin=BASE_MARGIN,
        rightMargin=BASE_MARGIN,
        bottomMargin=BASE_MARGIN
    )
    body_style = get_body_style()
    heading_style = get_heading_style()
    title_style = get_title_style()
    flowables = [Paragraph("Applicant # " + str(markingDf.loc[appRow, 'Serial']), title_style)]
    markingInfoRead = markingInfo[1:]
    for x in markingInfoRead:
        flowables.append(Paragraph(str(x), heading_style))
        flowables.append(Paragraph(str(markingDf.loc[appRow, x]), body_style))
    my_doc.build(flowables)

for i in markingDf.index:
    build_pdf(i)
