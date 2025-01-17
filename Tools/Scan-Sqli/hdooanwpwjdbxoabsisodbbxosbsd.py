import urllib2, cookielib, random, re, sys, socket, time, httplib, ssl, os
from time import sleep
if sys.platform == 'linux2' or sys.platform == 'linux':
    R = '\x1b[31m'
    W = '\x1b[0;1m'
    B = '\x1b[35m'
    G = '\x1b[32m'
    glp = '\x1b[2m'
    Y = '\x1b[33;1m'
    C = '\x1b[1;36m'
    U = '\x1b[1;34m'
else:
    R = ''
    W = ''
    Y = ''
    B = ''
    G = ''
    glp = ''
filename = 'VULNERABILITY.txt'
vuln = open(filename, 'a')
finallist = []
header = [
 'Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
 'Microsoft Internet Explorer/4.0b1 (Windows 95)',
 'Opera/8.00 (Windows NT 5.1; U; en)',
 'amaya/9.51 libwww/5.4.0',
 'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
 'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']
errors = {'MySQL': 'error in your SQL syntax', 'MiscError': 'mysql_fetch',
   'MiscError2': 'num_rows',
   'Oracle': 'ORA-01756',
   'JDBC_CFM': 'Error Executing Database Query',
   'JDBC_CFM2': 'SQLServer JDBC Driver',
   'MSSQL_OLEdb': 'Microsoft OLE DB Provider for SQL Server',
   'MSSQL_Uqm': 'Unclosed quotation mark',
   'MS-Access_ODBC': 'ODBC Microsoft Access Driver',
   'MS-Access_JETdb': 'Microsoft JET Database',
   'Error Occurred While Processing Request': 'Error Occurred While Processing Request',
   'Server Error': 'Server Error',
   'Microsoft OLE DB Provider for ODBC Drivers error': 'Microsoft OLE DB Provider for ODBC Drivers error',
   'Invalid Querystring': 'Invalid Querystring',
   'OLE DB Provider for ODBC': 'OLE DB Provider for ODBC',
   'VBScript Runtime': 'VBScript Runtime',
   'ADODB.Field': 'ADODB.Field',
   'BOF or EOF': 'BOF or EOF',
   'ADODB.Command': 'ADODB.Command',
   'JET Database': 'JET Database',
   'mysql_fetch_array()': 'mysql_fetch_array()',
   'Syntax error': 'Syntax error',
   'mysql_numrows()': 'mysql_numrows()',
   'GetArray()': 'GetArray()',
   'FetchRow()': 'FetchRow()',
   'Input string was not in a correct format': 'Input string was not in a correct format',
   'Not found': 'Not found'}
sites = [
 'ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao',
 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb',
 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bm', 'bn', 'bo',
 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd',
 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr',
 'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do',
 'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi',
 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf',
 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs',
 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu',
 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it',
 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn',
 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk',
 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me',
 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr',
 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc',
 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz',
 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn',
 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru',
 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj',
 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'su', 'sv', 'sy',
 'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm',
 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug',
 'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi',
 'vn', 'vu', 'wf', 'ws', 'ye', 'yt', 'za', 'zm', 'zw', 'com',
 'net', 'org', 'biz', 'gov', 'mil', 'edu', 'info', 'int', 'tel',
 'name', 'aero', 'asia', 'cat', 'coop', 'jobs', 'mobi', 'museum',
 'pro', 'travel']

def cek():
    print U + 43 * '='
    hasil = []
    for url in finallist:
        print R + '[!] ' + Y + 'SCANNING WEBS VULN-_-_-_-\r',
        sys.stdout.flush()
        EXT = "'"
        host = url + EXT
        try:
            source = urllib2.urlopen(host).read()
            for type, eMSG in errors.items():
                if re.search(eMSG, source):
                    print C + '\r[+]' + U + ' Vuln  ' + W + ': ' + host.replace("'", '')
                    print U + '[-]' + C + ' Error ' + W + ': ' + glp + type + W
                    hasil.append(host.replace("'", ''))

        except:
            pass

    if len(hasil) == 0:
        pass
    else:
        print U + 43 * '='
        print R + '[!] ' + W + 'Saving Vuln Web...',
        sys.stdout.flush()
        for x in hasil:
            vuln.write(x + '\n')

        vuln.close()
        print B + '\r[+] ' + G + 'SUCCESSFULLY SAVE IN THIS ' + W + filename
    print B + '\r[-] ' + G + 'TOTALS VULN WEBSITE ' + W + ': %s ' % len(hasil)
    print R + 43 * '=' + '\n'


def cari(inurl, site, maxc):
    print W + '[!] ' + C + 'Please Wait..' + glp,
    sys.stdout.flush()
    urls = []
    page = 0
    try:
        while page < int(maxc):
            jar = cookielib.FileCookieJar('cookies')
            query = inurl + '+site:' + site
            results_web = 'http://www.search-results.com/web?q=' + query + '&hl=en&page=' + repr(page) + '&src=hmp'
            request_web = urllib2.Request(results_web)
            agent = random.choice(header)
            request_web.add_header('User-Agent', agent)
            opener_web = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
            text = opener_web.open(request_web).read()
            stringreg = re.compile('(?<=href=")(.*?)(?=")')
            names = stringreg.findall(text)
            page += 1
            for name in names:
                if name not in urls:
                    if re.search('\\(', name) or re.search('<', name) or re.search('\\A/', name) or re.search('\\A(http://)\\d', name):
                        pass
                    elif re.search('google', name) or re.search('youtube', name) or re.search('phpbuddy', name) or re.search('iranhack', name) or re.search('phpbuilder', name) or re.search('codingforums', name) or re.search('phpfreaks', name) or re.search('%', name):
                        pass
                    else:
                        urls.append(name)

            percent = int(1.0 * page / int(maxc) * 100)
            urls_len = len(urls)
            (sys.stdout.write('\r[-] URLS: %s | PERCENTS: %s | PAGE: %s [-]' % (repr(urls_len), repr(percent) + '%', repr(page))),)
            sys.stdout.flush()

    except KeyboardInterrupt:
        pass
    except urllib2.URLError as e:
        print W + '\r-- ' + C + 'Error ' + W + '-- ' + Y + ': %s' % e
        print U + 43 * '='
        sys.exit()
    except socket.error as s:
        print W + '\r-- ' + C + 'Error ' + W + '-- ' + Y + ': %s' % s
        print U + 43 * '='
        sys.exit()
    except httplib.IncompleteRead as h:
        print W + '\r-- ' + C + 'Error ' + W + '-- ' + Y + ': %s' % h
        print U + 43 * '='
        sys.exit()
    except ValueError as V:
        print W + '\r-- ' + C + 'Error ' + W + '-- ' + Y + ': %s' % V
        print U + 43 * '='
        sleep(4)
        os.system('clear')
        os.system('python2 project.py')

    tmplist = []
    for url in urls:
        try:
            host = url.split('/', 3)
            domain = host[2]
            if domain not in tmplist and '=' in url:
                finallist.append(url)
                tmplist.append(domain)
        except:
            pass

    print '\n' + W + 43 * '='
    print C + '[+] ' + U + 'URLS [SORTED] ' + C + ': %s Url' % len(finallist)
    if site == '':
        print C + '[+] ' + U + 'SITE          ' + C + ': random'
    else:
        print C + '[+] ' + U + 'SITE          ' + C + ': %s' % site
    return finallist


if __name__ == '__main__':
    os.system('clear')
    inurl = raw_input(Y + '[~]' + C + ' URL-DORK    ' + W + ': ' + G + '')
    site = raw_input(Y + '[~]' + C + ' SITE        ' + W + ': ' + G + '')
    maxc = raw_input(Y + '[~]' + C + ' MAX PAGES   ' + W + ': ' + G + '')
    print U + 43 * '='
    cari(inurl, site, maxc)
    cek()
