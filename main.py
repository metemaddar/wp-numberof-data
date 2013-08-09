Content = '<!-- If you want to add a new language, ask for it in the talk pages, not here directly. --><onlyinclude>{{#switch:{{{1}}}\n'
Template = '| %(language) = {{#switch:{{{2}}}
  | NUMBEROFARTICLES | ARTICLES = %(articles)
	| NUMBEROFFILES | FILES = %(files)
	| NUMBEROFPAGES | PAGES = %(pages)
	| NUMBEROFUSERS | USERS = %(users)
	| NUMBEROFACTIVEUSERS | ACTIVEUSERS = %(activities)
	| NUMBEROFADMINS | ADMINS = %(admins)
	| NUMBEROFEDITS | EDITS = %(edits)
	| 0 }}\n'
  
from urllib import urlopen
from xml.dom import minidom

langs = ['en','fa','de','es']
URL_template = 'http://%(s).wikipedia.org/w/api.php?action=query&meta=siteinfo&siprop=statistics&format=xml'
for lang in langs:
    url = (URL_template % {'s':lang})
    stat_string = urlopen(url).read()
    stat_xml = minidom.parseString(stat_string)
    
    
    element = stat_xml.getElementByName('statistics')
    
    articles = element[0].attributes['articles']
    files = element[0].attributes['files']
    pages = element[0].attributes['pages']
    users = element[0].attributes['users']
    activities = element[0].attributes['activities']
    admins = element[0].attributes['admins']
    edits = element[0].attributes['edits']
    
    this_content = Template % {'articles' : articles , 'files' : files , 'pages' : pages , 'users' : users , 'activities' : activities , 'admins' : admins , 'edits' : edits }
    content = content + this_content

print content
