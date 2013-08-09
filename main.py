content = '<!-- If you want to add a new language, ask for it in the talk pages, not here directly. --><onlyinclude>{{#switch:{{{1}}}\n'
Template = '| %(language)s = {{#switch:{{{2}}}\n  | NUMBEROFARTICLES | ARTICLES = %(articles)s\n		| NUMBEROFFILES | FILES = %(images)s\n	| NUMBEROFPAGES | PAGES = %(pages)s\n	| NUMBEROFUSERS | USERS = %(users)s\n	| NUMBEROFACTIVEUSERS | ACTIVEUSERS = %(activeusers)s\n	| NUMBEROFADMINS | ADMINS = %(admins)s\n	| NUMBEROFEDITS | EDITS = %(edits)s\n	| 0 }}\n'
  
from urllib import urlopen
from xml.dom import minidom
import wikipedia
langs = ["en" , "nl" , "de" , "fr" , "sv" , "it" , "es" , "ru" , "pl" , "ja" , "vi" , "pt" , "zh" , "ceb" , "war" , "uk" , "ca" , "no" , "fi" , "fa" , "cs" , "ko" , "hu" , "ar" , "ro" , "ms" , "sr" , "tr" , "id" , "kk" , "sk" , "eo" , "da" , "lt" , "eu" , "bg" , "he" , "hr" , "sl" , "uz" , "vo" , "et" , "hi" , "nn" , "gl" , "simple" , "az" , "la" , "el" , "sh" , "oc" , "th" , "ka" , "mk" , "new" , "hy" , "pms" , "be" , "tl" , "ta" , "ht" , "te" , "tt" , "cy" , "be-x-old" , "sq" , "lv" , "bs" , "br" , "jv" , "mg" , "mr" , "lb" , "is" , "ml" , "my" , "ba" , "yo" , "an" , "lmo" , "fy" , "af" , "bn" , "pnb" , "sw" , "bpy" , "io" , "zh-yue" , "ur" , "ky" , "ne" , "scn" , "gu" , "ga" , "nds" , "ku" , "cv" , "ast" , "qu" , "su" , "sco" , "als" , "ia" , "nap" , "bug" , "bat-smg" , "kn" , "map-bms" , "wa" , "am" , "gd" , "ckb" , "hif" , "zh-min-nan" , "tg" , "arz" , "mzn" , "yi" , "vec" , "mn" , "sah" , "nah" , "sa" , "roa-tara" , "os" , "si" , "pam" , "bar" , "hsb" , "se" , "li" , "pa" , "mi" , "co" , "fo" , "ilo" , "gan" , "
bo" , "glk" , "rue" , "frr" , "bcl" , "min" , "nds-nl" , "fiu-vro" , "mrj" , "tk" , "ps" , "vls" , "xmf" , "gv" , "diq" , "or" , "kv" , "pag" , "km" , "zea" , "mhr" , "dv" , "nrm" , "csb" , "vep" , "vep" , "rm" , "koi" , "udm" , "ce" , "lad" , "lij" , "wuu" , "fur" , "sc" , "zh-classical" , "stq" , "ug" , "mt" , "ay" , "so" , "pi" , "hak" , "bh" , "ksh" , "nov" , "kw" , "ang" , "gn" , "pcd" , "nv" , "as" , "ext" , "frp" , "eml" , "gag" , "ace" , "szl" , "ie" , "ln" , "pfl" , "krc" , "xal" , "haw" , "pdc" , "rw" , "crh" , "to" , "dsb" , "lez" , "arc" , "kl" , "myv" , "kab" , "sn" , "bjn" , "pap" , "tpi" , "lbe" , "wo" , "mwl" , "jbo" , "mdf" , "kbd" , "cbk-zam" , "av" , "srn" , "lo" , "ty" , "kg" , "ab" , "tet" , "ltg" , "na" , "ig" , "bxr" , "nso" , "za" , "kaa" , "zu" , "chy" , "rmy" , "cu" , "tn" , "chr" , "roa-rup" , "cdo" , "bi" , "got" , "sm" , "mo" , "bm" , "iu" , "pih" , "pnt" , "ss" , "sd" , "ki" , "ee" , "ha" , "om" , "fj" , "ti" , "ts" , "ks" , "ve" , "sg" , "rn" , "st" , "cr" , "dz" , "ak" , "tum" 
, "ik" , "ff" , "lg" , "ny" , "ch" , "tw" , "xh" , "ng" , "ii" , "cho" , "mh" , "aa" , "kj" , "ho" , "mus" , "kr" , "hz"]
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
