import unicodedata
str_test = u"Vous êtes le Père Noël ? s'étonna le petit garçon."
unicodedata.normalize('NFKD', str_test)
           .encode('ascii', 'ignore')
