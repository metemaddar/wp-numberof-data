content = '<!-- If you want to add a new language, ask for it in the talk pages, not here directly. --><onlyinclude>{{#switch:{{{1}}}\n'
Template = '| %(language)s = {{#switch:{{{2}}}\n  | NUMBEROFARTICLES | ARTICLES = %(articles)s\n		| NUMBEROFFILES | FILES = %(images)s\n	| NUMBEROFPAGES | PAGES = %(pages)s\n	| NUMBEROFUSERS | USERS = %(users)s\n	| NUMBEROFACTIVEUSERS | ACTIVEUSERS = %(activeusers)s\n	| NUMBEROFADMINS | ADMINS = %(admins)s\n	| NUMBEROFEDITS | EDITS = %(edits)s\n	| 0 }}\n'
  
from urllib import urlopen
from xml.dom import minidom
import wikipedia
langs = ['en','fa','de','es']
URL_template = 'http://%(s)s.wikipedia.org/w/api.php?action=query&meta=siteinfo&siprop=statistics&format=xml'
for lang in langs:
    url = URL_template % {'s':lang}
    stat_string = urlopen(url).read()
    stat_xml = minidom.parseString(stat_string)
    
    
    element = stat_xml.getElementsByTagName('statistics')
    
    articles = element[0].attributes['articles'].value
    images = element[0].attributes['images'].value
    pages = element[0].attributes['pages'].value
    users = element[0].attributes['users'].value
    activeusers = element[0].attributes['activeusers'].value
    admins = element[0].attributes['admins'].value
    edits = element[0].attributes['edits'].value
    
    this_content = Template % {'language' : lang , 'articles' : articles , 'images' : images , 'pages' : pages , 'users' : users , 'activeusers' : activeusers , 'admins' : admins , 'edits' : edits }
    content = content + this_content
    print "Wiki",lang,"got"
content = content + '| 0 }}</onlyinclude>'
print "Finish langs"
site = wikipedia.getSite()
print "Site Got"
page = wikipedia.Page(site, u"karbar"Sefid_Par_BOT/test")
print "Page Got"
page.put(content,u"New test")
print "Finish!"
