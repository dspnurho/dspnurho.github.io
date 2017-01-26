from yattag import Doc

doc, tag, text = Doc().tagtext()

#with tag('h1'):
#    text('hello world')
#
#print(doc.getvalue())
doc.asis("<!DOCTYPE html>")
with tag('html'):
    with tag('head'):
        # basic page needs
        doc.stag('meta', charset='utf-8')
        doc.stag('meta', name='viewport', content='width=device-width, initial-scale=1')
        with tag('title'):
            text('ΔΣΠ | NP')
        doc.stag('meta', name='description', content='Delta Sigma Pi is a professional business fraternity')
        doc.stag('meta', name='keywords', content='brother deltasig delta sigma pi fraternity davis college business professional')

        # favicons
        doc.stag('link', rel='shortcut icon', href='img/favicon.ico', type='image/x-icon')
        doc.stag('link', rel='apple-touch-icon', href='img/apple-touch-icon.png')
        doc.stag('link', rel='apple-touch-icon', href='img/apple-touch-icon-72x72.png', sizes='72x72')
        doc.stag('link', rel='apple-touch-icon', href='img/apple-touch-icon-114x114.png', sizes='114x114')

        # bootstrap
        doc.stag('link', rel='stylesheet', type='text/css', href='../css/bootstrap.css')
        doc.stag('link', rel='stylesheet', type='text/css', href='../fonts/font-awesome/css/font-awesome.css')
        
        # slider - leave this out for now

        # stylesheet
        doc.stag('link', rel='stylesheet', type='text/css', href='../css/style.css')
        doc.stag('link', rel='stylesheet', type='text/css', href='../css/responsive.css')
        doc.stag('link', rel='stylesheet', type='text/css', href='http://fonts.googleapis.com/css?family=Lato:100,300,400,700,900,100italic,300italic,400italic,700italic,900italic')
        doc.stag('link', rel='stylesheet', type='text/css', href='http://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,700,300,600,800,400')

        doc.stag('script', type='text/javascript', src='../js/modernizr.custom.js')

        # comment
        doc.asis('<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->')
        doc.asis("<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->")
        doc.asis('<!--[if lt IE 9]>')
        doc.asis('<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>')
        doc.asis('<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>')
        doc.asis('<![endif]-->')

    #with tag('body'):

f = open('output.html', 'w')
f.write(doc.getvalue())
f.close()
