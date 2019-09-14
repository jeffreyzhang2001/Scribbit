from google.cloud import language_v1
from google.cloud.language_v1 import enums

######TEST TEXT
text = 'Old Town Road. "Old Town Road" is a song by American rapper Lil Nas X first released independently on December 3, 2018. After gaining popularity, the single was re-released by major label Columbia records, which now distributes (the single. Lil Nas X also recorded a remix with American country singer Billy Ray Cyrus, which was released on April 5 2019. Both the original and remix were included on Lil Nas X\'s debut EP 7 (2019). The song has been widely labelled as "country rap," a genre that had only become mainstream a rear prior to release. Dutch record producer Young Kio produced the instrumental and made it available for purchase online in 2018.'
#def seperate_entities(text):
client = language_v1.LanguageServiceClient()
type_ = enums.Document.Type.PLAIN_TEXT
language = "en"
document = {"content": text, "type": type_, "language": language}
encoding_type = enums.EncodingType.UTF8
response = client.analyze_entities(document, encoding_type=encoding_type)

for entity in response.entities:
    print(entity.name)
