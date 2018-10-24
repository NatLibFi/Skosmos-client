# Skosmos-client

This is a Python 3.x client library for accessing
[Skosmos](http://skosmos.org) REST API endpoints such as the [Finto
API](http://api.finto.fi). The API can be used to get information about
vocabularies, look up and search for concepts and to retrieve information
about individual concepts.

## Installation

The easiest way to install is via pip:

    pip3 install skosmos-client

## Dependencies

The library depends on the
[requests](http://docs.python-requests.org/en/master/#) module which is used
for HTTP/REST access. If you install this via pip, the dependencies will be
handled automatically.

## How to use

The client library comes with examples demonstrating its usage. You can invoke
the example simply by running the [skosmos_client.py](skosmos_client.py) script.

In your own code, you can use the SkosmosClient class like this:

    from skosmos_client import SkosmosClient

    # then you can create your own client
    skosmos = SkosmosClient()

## Example invocation

Here is the output from a typical example session:

    $ ./skosmos_client.py
    Demonstrating usage of SkosmosClient

    * Creating a SkosmosClient object
    Now we have a SkosmosClient object: SkosmosClient(api_base='http://api.finto.fi/rest/v1/')

    * Finding the available vocabularies
    Vocabulary id: afo              title: AFO - Natural resource and environment ontology
    Vocabulary id: allars           title: Allärs - General thesaurus in Swedish
    Vocabulary id: cn               title: Finnish Corporate Names
    Vocabulary id: ic               title: Iconclass
    Vocabulary id: iptc             title: IPTC NewsCodes
    Vocabulary id: juho             title: JUHO - Julkishallinnon ontologia
    Vocabulary id: jupo             title: JUPO - Finnish Ontology for Public Administration Services
    Vocabulary id: kassu            title: Kassu - Finnish Names of Plants
    Vocabulary id: kauno            title: KAUNO - ontology for fiction
    Vocabulary id: keko             title: KEKO - Ontology for Education for Sustainable Development
    Vocabulary id: kito             title: KITO - Kirjallisuudentutkimuksen ontologia
    Vocabulary id: koko             title: KOKO Ontology
    Vocabulary id: kto              title: KTO - Kielitieteen ontologia
    Vocabulary id: kulo             title: KULO - Kulttuurien tutkimuksen ontologia
    Vocabulary id: lapponica        title: Lapponica
    Vocabulary id: lexvo            title: Lexvo - ISO 639-3 language codes
    Vocabulary id: liiko            title: LIIKO - Liikenteen ontologia
    Vocabulary id: liito            title: LIITO - Liiketoimintaontologia
    Vocabulary id: maotao           title: MAO/TAO - Ontology for Museum Domain and Applied Arts
    Vocabulary id: mesh             title: Medical Subject Headings
    Vocabulary id: mts              title: Metatietosanasto
    Vocabulary id: musa             title: MUSA/CILLA - Finnish Music Thesaurus
    Vocabulary id: muso             title: MUSO - Ontology for Music
    Vocabulary id: oiko             title: OIKO - Oikeushallinnon ontologia
    Vocabulary id: okm-tieteenala   title: Korkeakoulujen tutkimustiedonkeruussa käytettävä tieteenalaluokitus
    Vocabulary id: ponduskategorier title: Pondus categories
    Vocabulary id: pto              title: PTO - Finnish Geospatial Domain Ontology
    Vocabulary id: ptvl             title: Julkisten palvelujen luokitus
    Vocabulary id: puho             title: PUHO - Puolustushallinnon ontologia
    Vocabulary id: seko             title: SEKO - Suomalainen esityskokoonpanosanasto
    Vocabulary id: slm              title: Suomalainen lajityyppi- ja muotosanasto
    Vocabulary id: tero             title: TERO - Finnish Ontology of Health and Welfare
    Vocabulary id: tsr              title: TSR ontology
    Vocabulary id: tt               title: Tietotermit
    Vocabulary id: ucum             title: UCUM - The Unified Code for Units of Measure
    Vocabulary id: valo             title: VALO - The Finnish Ontology of Photography
    Vocabulary id: ysa              title: YSA - General Finnish thesaurus
    Vocabulary id: yse              title: YSAn ja YSOn käsite-ehdotukset
    Vocabulary id: yso              title: YSO - General Finnish ontology
    Vocabulary id: yso-paikat       title: YSO places

    * Searching for concepts globally in all vocabularies
    {'prefLabel': 'Stockholm', 'lang': 'en', 'uri': 'http://www.yso.fi/onto/yso/p105464', 'type': ['skos:Concept'], 'vocab': 'yso-paikat'}
    {'prefLabel': 'Stockholm archipelago', 'lang': 'en', 'uri': 'http://www.yso.fi/onto/yso/p108598', 'type': ['skos:Concept'], 'vocab': 'yso-paikat'}
    {'lang': 'en', 'uri': 'http://urn.fi/URN:NBN:fi:au:cn:61010A', 'vocab': 'cn', 'type': ['skos:Concept', 'http://rdaregistry.info/Elements/c/C10005'], 'altLabel': 'Stockholm County Council'}
    {'lang': 'en', 'uri': 'http://urn.fi/URN:NBN:fi:au:cn:29584A', 'vocab': 'cn', 'type': ['skos:Concept', 'http://rdaregistry.info/Elements/c/C10005'], 'altLabel': 'Stockholm International Peace Research Institute'}
    {'lang': 'en', 'uri': 'http://urn.fi/URN:NBN:fi:au:cn:195071A', 'vocab': 'cn', 'type': ['skos:Concept', 'http://rdaregistry.info/Elements/c/C10005'], 'altLabel': 'Stockholm School of Economics'}

    * Searching for concepts within a single vocabulary
    {'prefLabel': 'cosmologists', 'uri': 'http://www.yso.fi/onto/yso/p27082', 'localname': 'p27082', 'hiddenLabel': 'cosmologist', 'lang': 'en', 'type': ['skos:Concept', 'http://www.yso.fi/onto/yso-meta/Concept'], 'vocab': 'yso'}
    {'prefLabel': 'cosmologists', 'uri': 'http://www.yso.fi/onto/yso/p27082', 'localname': 'p27082', 'lang': 'en', 'type': ['skos:Concept', 'http://www.yso.fi/onto/yso-meta/Concept'], 'vocab': 'yso'}
    {'prefLabel': 'cosmology', 'uri': 'http://www.yso.fi/onto/yso/p7160', 'localname': 'p7160', 'lang': 'en', 'type': ['skos:Concept', 'http://www.yso.fi/onto/yso-meta/Concept'], 'vocab': 'yso'}

    * Looking up all information about a particular concept
    Got 168 triples of data
    <http://www.yso.fi/onto/tero/p127> has label "theories"@en
    <http://www.yso.fi/onto/tero/p352> has label "sciences"@en
    <http://www.yso.fi/onto/yso/p20188> has label "astrophysics"@en
    <http://www.yso.fi/onto/yso/p4403> has label "universe"@en
    <http://www.yso.fi/onto/yso/p26588> has label "06 Astronomy. Space Research"@en
    <http://www.yso.fi/onto/yso/p352> has label "sciences (branches of science)"@en
    <http://www.yso.fi/onto/yso/p28351> has label "cosmography"@en
    <http://www.yso.fi/onto/yso/p127> has label "theories (formulations)"@en
    <http://www.yso.fi/onto/yso/p21501> has label "big bang"@en
    <http://www.yso.fi/onto/yso/p7160> has label "cosmology"@en
    <http://www.yso.fi/onto/yso/p127> has label "theories"@en
    <http://www.yso.fi/onto/yso/NY144307> has label "big bang"@en
    <http://www.yso.fi/onto/yso/p2872> has label "origin of universe"@en
    <http://www.yso.fi/onto/yso/p2872> has label "origin of the universe"@en
    <http://www.yso.fi/onto/yso/p352> has label "sciences"@en
    <http://www.yso.fi/onto/yso/p26545> has label "02 Philosophy"@en

    * Looking up information about types within a vocabulary
    {'uri': 'http://www.w3.org/2004/02/skos/core#Concept', 'label': 'Concept'}
    {'uri': 'http://www.w3.org/2004/02/skos/core#Collection', 'label': 'Collection'}
    {'uri': 'http://purl.org/iso25964/skos-thes#ConceptGroup', 'label': 'Concept group'}
    {'uri': 'http://purl.org/iso25964/skos-thes#ThesaurusArray', 'label': 'Array of sibling concepts'}
    {'uri': 'http://www.yso.fi/onto/yso-meta/Concept', 'label': 'General concept', 'superclass': 'http://www.w3.org/2004/02/skos/core#Concept'}
    {'uri': 'http://www.yso.fi/onto/yso-meta/Individual', 'label': 'Individual concept', 'superclass': 'http://www.w3.org/2004/02/skos/core#Concept'}
    {'uri': 'http://www.yso.fi/onto/yso-meta/Hierarchy', 'label': 'Hierarchical concept', 'superclass': 'http://www.w3.org/2004/02/skos/core#Concept'}

    * Looking up information about a particular vocabulary
    conceptschemes      : [{'title': 'YSO - General Finnish ontology', 'subject': {'prefLabel': 'general concepts', 'uri': 'http://www.yso.fi/onto/yso/p19469'}, 'label': 'YSO - General Finnish ontology', 'uri': 'http://www.yso.fi/onto/yso/', 'type': 'skos:ConceptScheme'}, {'uri': 'http://www.yso.fi/onto/yso/aggregateconceptscheme', 'type': 'skos:ConceptScheme'}, {'uri': 'http://www.yso.fi/onto/yso/deprecatedconceptscheme', 'type': 'skos:ConceptScheme'}]
    defaultLanguage     : fi
    id                  : yso
    languages           : ['en', 'fi', 'sv']
    title               : YSO - General Finnish ontology

    * Looking up top level concepts for a vocabulary
    {'uri': 'http://www.yso.fi/onto/yso/p15238', 'topConceptOf': 'http://www.yso.fi/onto/yso/', 'label': 'events and action', 'hasChildren': True}
    {'uri': 'http://www.yso.fi/onto/yso/p8691', 'topConceptOf': 'http://www.yso.fi/onto/yso/', 'label': 'properties', 'hasChildren': True}
    {'uri': 'http://www.yso.fi/onto/yso/p4762', 'topConceptOf': 'http://www.yso.fi/onto/yso/', 'label': 'objects', 'hasChildren': True}

    * Looking up a concept by its label
    [{'prefLabel': 'cosmology', 'uri': 'http://www.yso.fi/onto/yso/p7160', 'localname': 'p7160', 'lang': 'en', 'type': ['skos:Concept', 'http://www.yso.fi/onto/yso-meta/Concept'], 'vocab': 'yso'}]

    * Looking up the thematic groups of a vocabulary
    {'prefLabel': '00 General Terms', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26556'}
    {'prefLabel': '02 Philosophy', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26545'}
    {'prefLabel': '04 Mathematics. Statistics', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26574'}
    {'prefLabel': '06 Astronomy. Space Research', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26588'}
    {'prefLabel': '07 Physics', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26565'}
    {'prefLabel': '09 Chemistry', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26531'}
    {'prefLabel': '11 Geography. Cartography. Geodesy. Geology. Palaeontology', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26535'}
    {'prefLabel': '13 Hydrology', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26580'}
    {'prefLabel': '14 Climatology. Meteorology', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26587'}
    {'prefLabel': '15 Biology. Microbiology. Genetics. Anthropology', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26579'}
    {'prefLabel': '16 Botany', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26533'}
    {'prefLabel': '17 Zoology', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26529'}
    {'prefLabel': '18 Nature Protection. Environmental Conservation. Environment. Waste', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26560'}
    {'prefLabel': '19 Energy. Fuels', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26566'}
    {'prefLabel': '21 Forestry. Silviculture', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26537'}
    {'prefLabel': '22 Agriculture. Farming. Horticulture. Animal Husbandry', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26528'}
    {'prefLabel': '23 Fishery. Hunting', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26561'}
    {'prefLabel': '24 Nutrition. Restaurant Sector. Food Sector. Accommodation Sector. Domestic economy', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26555'}
    {'prefLabel': '26 Textile Industry. Clothing Industry. Footwear Industry. Leather Industry. Fur Industry', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26578'}
    {'prefLabel': '28 Forest Industry. Pulp and Paper Industry. Paper Industry. Wood Industry', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26585'}
    {'prefLabel': '30 Chemicals Industry. Ceramics Industry. Glass Industry. Plastic Industry. Rubber Industry', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26530'}
    {'prefLabel': '32 Mining Industry. Extractive Industry', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26567'}
    {'prefLabel': '34 Metal Industry. Metallurgy. Mechanical Engineering Industry. Precision Engineering Industry', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26576'}
    {'prefLabel': '37 Construction. Building Industry. Housing Construction. Earth Construction. Hydraulic Engineering. Road Construction', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26568'}
    {'prefLabel': '39 Traffic. Transport. Mail. Packaging Industry', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26577'}
    {'prefLabel': '41 Electrical Engineering. Electronics', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26536'}
    {'prefLabel': '43 Information Technology. Data processing', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26553'}
    {'prefLabel': '45 Communications Technology. Telecommunications Technology. Sound Engineering', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26542'}
    {'prefLabel': '48 Medicine. Anatomy. Physiology. Pathology.  Psychiatry. Dentistry. Veterinary Medicine. Pharmacy. Beauty Care. Treatments', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26550'}
    {'prefLabel': '49 Fire Protection. Rescue Services. Accident Prevention. Safety Engineering', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26548'}
    {'prefLabel': '50 Folklore. Cultural Anthropology. Occultism', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26532'}
    {'prefLabel': '51 Archaeology', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26593'}
    {'prefLabel': '52 History', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26540'}
    {'prefLabel': '53 Religion. Theology. Religious Studies', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26551'}
    {'prefLabel': '55 Psychology', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26543'}
    {'prefLabel': '56 Science. Research', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26544'}
    {'prefLabel': '57 Upbringing. Teaching. Education', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26554'}
    {'prefLabel': '60 Sosiology. Social Psychology', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26562'}
    {'prefLabel': '61 Demography', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26570'}
    {'prefLabel': '62 Community Planning. Regional Planning', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26526'}
    {'prefLabel': '65 Political Science. Politics. International Politics', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26541'}
    {'prefLabel': '67 Warfare. Military Technology. Defence. Weapons', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26575'}
    {'prefLabel': '69 Justice. Legislation', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26559'}
    {'prefLabel': '71 Administration. Organisational Research. Public Administration', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26524'}
    {'prefLabel': '73 Social Policy. Social Development Policy. Social Security.  Health Care. Housing', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26549'}
    {'prefLabel': '75 Economics. National Economy. Business Economics. Commerce', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26538'}
    {'prefLabel': '78 Work. Occupational Safety. Occupational Health', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26525'}
    {'prefLabel': '80 Communication. Mass Communication. Advertising', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26547'}
    {'prefLabel': '81 Libraries. Archives. Information Services. Museums. Exhibitions', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26572'}
    {'prefLabel': '82 Publishing. Printing', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26563'}
    {'prefLabel': '85 Linguistics', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26557'}
    {'prefLabel': '87 Literature', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26564'}
    {'prefLabel': '89 Music', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26571'}
    {'prefLabel': '90 Art in general. Art periods and genres. Art History', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26581'}
    {'prefLabel': '91 Architecture', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26552'}
    {'prefLabel': '92 Visual Arts. Painting. Graphic Arts. Sculpture', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26569'}
    {'prefLabel': '94 Applied Arts. Interior Art', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26586'}
    {'prefLabel': '95 Theatre. Dance', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26582'}
    {'prefLabel': '96 Photography. Film', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26534'}
    {'prefLabel': '97 Exercise. Training. Sports', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26546'}
    {'prefLabel': '98 Free Time. Hobbies. Travel. Handicrafts', 'hasMembers': True, 'uri': 'http://www.yso.fi/onto/yso/p26527'}


## License

The code is published under the [Apache 2.0](LICENSE.txt) license.
