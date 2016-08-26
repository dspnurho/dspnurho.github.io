from yattag import Doc
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

def make_file(filename, bro):
#def make_file(filename):

    doc, tag, text = Doc().tagtext()
    
    
    doc.asis("<!DOCTYPE html>")
    with tag('html', lang='en'):
        with tag('head'):
    
            # basic page needs
            doc.asis('<meta charset="utf-8">')
            doc.asis('<meta name="viewport" content="width=device-width, initial-scale=1">')
            doc.asis('<title>ΔΣΠ | NP</title>')
            doc.asis('<meta name="description" content="Delta Sigma Pi is a professional business fraternity">')
            doc.asis('<meta name="keywords" content="brother deltasig delta sigma pi fraternity davis college business professional">')
    
            # favicons
            doc.asis('<link rel="shortcut icon" href="img/favicon.ico" type="image/x-icon">')
            doc.asis('<link rel="apple-touch-icon" href="img/apple-touch-icon.png">')
            doc.asis('<link rel="apple-touch-icon" sizes="72x72" href="img/apple-touch-icon-72x72.png">')
            doc.asis('<link rel="apple-touch-icon" sizes="114x114" href="img/apple-touch-icon-114x114.png">')
    
            # bootstrap
            doc.asis('<link rel="stylesheet" type="text/css"  href="../css/bootstrap.css">')
            doc.asis('<link rel="stylesheet" type="text/css" href="../fonts/font-awesome/css/font-awesome.css">')
    
            # stylesheet
            doc.asis('<link rel="stylesheet" type="text/css"  href="../css/style.css">')
            doc.asis('<link rel="stylesheet" type="text/css" href="../css/responsive.css">')
    
            doc.asis('<link href="http://fonts.googleapis.com/css?family=Lato:100,300,400,700,900,100italic,300italic,400italic,700italic,900italic" rel="stylesheet" type="text/css">')
            doc.asis('<link href="http://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,700,300,600,800,400" rel="stylesheet" type="text/css">')
    
            doc.asis('<script type="text/javascript" src="../js/modernizr.custom.js"></script>')
            
    
        with tag('body', style="background-color: #000000;"):
    
            ##### start div #####
            doc.stag('div', klass='space')
            with tag('div', id='tf-brothers-deltasigs'):
                with tag('div', klass='container'):
                    with tag('div', klass='row'):
                        with tag('div', klass='col-md-5'):
                            doc.stag('img', src='../img/brothers/ws16_solonyiu.jpg', klass='img-responsive', width='80%', height='auto', style='float: right; padding-right: 80px;')
            
                        with tag('div', klass='col-md-6'):
                            with tag('div', klass='brothers-text'):
                                with tag('div', klass='section-title'):
                                    with tag('h2'):
                                        with tag('strong'):
                                            #text('SOLON YIU')
                                            text(bro[0].upper())
            
                                    doc.asis('<hr>')
                                    doc.asis('<div class="clearfix"></div>')
                                    with tag('p', klass='intro', style='text-align: left;'):
                                        with tag('strong'):
                                            text('CONTACT:')
                                        #text(' shyiu@ucdavis.edu')
                                        text(' ' + bro[12])
                                        doc.stag('br')
            
                                        with tag('strong'):
                                            text('CLASS:')
                                        #text(' Alpha Phi')
                                        text(' ' + bro[4])
                                        doc.stag('br')
            
                                        with tag('strong'):
                                            text('YEAR:')
                                        #text(' Junior')
                                        text(' ' + bro[1])
                                        doc.stag('br')
            
                                        with tag('strong'):
                                            text('MAJOR(S):')
                                        #text(' Mechanical Engineering')
                                        text(' ' + bro[2])
                                        doc.stag('br')
            
                                        with tag('strong'):
                                            text('MINOR(S):')
                                        #text(' Technology Management')
                                        text(' ' + bro[3])
                                        doc.stag('br')
            
                                        with tag('strong'):
                                            text('HOMETOWN:')
                                        #text(' San Ramon, CA')
                                        text(' ' + bro[5])
                                        doc.stag('br')
            
                                        with tag('strong'):
                                            text('FRATERNAL POSITION(S) HELD:')
                                        #text(' Historian, Pledge Class Professional Chair')
                                        text(' ' + bro[6])
                                        doc.stag('br')
            
                                        with tag('strong'):
                                            text('OTHER INVOLVEMENT(S):')
                                        #text(' Mga Kapatid Modern Dance Team Member, Asian American Christian Fellowship Member')
                                        text(' ' + bro[7])
                                        doc.stag('br')
            
                                        with tag('strong'):
                                            text('WORK EXPERIENCE(S):')
                                        #text(' Yang Fan Academy (Teaching), Hollister Retail (Customer Service)')
                                        text(' ' + bro[10])
                                        doc.stag('br')
                                        doc.stag('br')
            
                                        with tag('strong'):
                                            text('BIOGRAPHY:')
                                        #text(' Solon hopes to apply the technical skills of his mechanical engineering major to technology consulting and eventually hopes to invest in real estate. During his spare time, Solon enjoys shooting landscape photography, playing competitive Pokemon, playing guitar, and listening to music. He also is accepting challenges from anyone to a Facebook 1v1 Tetris Battle with standard rules of no bombs or handicaps.')
                                        text(' ' + bro[8])
            
                                    doc.stag('br')
                                    #with tag('a', href='http://www.linkedin.com/in/solonyiu'):
                                    with tag('a', href=bro[9]):
                                        doc.stag('img', src='../img/linkedin.png', style='width:15%;height:15%;border:0;')
            
                ##### end div #####
                
                doc.asis('<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>')
                doc.asis('<script type="text/javascript" src="../js/bootstrap.js"></script>')
                doc.asis('<script type="text/javascript" src="../js/SmoothScroll.js"></script>')
                doc.asis('<script type="text/javascript" src="../js/jquery.isotope.js"></script>')
                
                doc.asis('<script type="text/javascript" src="../js/main.js"></script>')
        
    
    ##### write to file #####
    
    f = open(filename, 'w')
    f.write(doc.getvalue())
    f.close()

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    #spreadsheetId = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
    spreadsheetId = '1eGCNM7I159BvJo23ubZiWx6MTmyBaoS6iwUDB5daLcc'
    #rangeName = 'Class Data!A2:E'
    rangeName = 'Brothers!A:M'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    values = values[1:]

    if not values:
        print('No data found.')
    else:
        #print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            #print('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]))
            #print('\n')
            make_file(row[0].replace(' ', '') + '-autogenerated.html', row)


if __name__ == '__main__':
    main()

