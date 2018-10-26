#!/usr/bin/env python3
"""Module for accessing Skosmos REST API"""

import requests
import rdflib
from rdflib.namespace import SKOS

# Default API base URL
API_BASE = 'http://api.finto.fi/rest/v1/'


class SkosmosConcept:
    """Class for representing and providing operations for a single concept
    from a Skosmos API."""
    
    def __init__(self, api_base, vocid, uri):
        self.api_base = api_base
        self.vocid = vocid
        self.uri = uri
    
    def label(self, lang=None):
        payload = {'uri': self.uri}
        if lang is not None:
            payload['lang'] = lang
        req = requests.get(self.api_base + self.vocid + '/label', params=payload)
        req.raise_for_status()
        data = req.json()
        return data['prefLabel']
    
    def broader(self, lang=None):
        payload = {'uri': self.uri}
        if lang is not None:
            payload['lang'] = lang
        req = requests.get(self.api_base + self.vocid + '/broader', params=payload)
        req.raise_for_status()
        data = req.json()
        return data['broader']
    
    def broaderTransitive(self, lang=None):
        payload = {'uri': self.uri}
        if lang is not None:
            payload['lang'] = lang
        req = requests.get(self.api_base + self.vocid + '/broaderTransitive', params=payload)
        req.raise_for_status()
        data = req.json()
        return data['broaderTransitive']
    
    def narrower(self, lang=None):
        payload = {'uri': self.uri}
        if lang is not None:
            payload['lang'] = lang
        req = requests.get(self.api_base + self.vocid + '/narrower', params=payload)
        req.raise_for_status()
        data = req.json()
        return data['narrower']

    def narrowerTransitive(self, lang=None):
        payload = {'uri': self.uri}
        if lang is not None:
            payload['lang'] = lang
        req = requests.get(self.api_base + self.vocid + '/narrowerTransitive', params=payload)
        req.raise_for_status()
        data = req.json()
        return data['narrowerTransitive']

    def related(self, lang=None):
        payload = {'uri': self.uri}
        if lang is not None:
            payload['lang'] = lang
        req = requests.get(self.api_base + self.vocid + '/related', params=payload)
        req.raise_for_status()
        data = req.json()
        return data['related']
    
    


class SkosmosClient:
    """Client class for accessing Skosmos REST API operations"""

    def __init__(self, api_base=API_BASE):
        self.api_base = api_base

    def vocabularies(self, lang):
        """Get a list of vocabularies available on the API endpoint.
        Vocabulary titles will be returned in the given language."""

        payload = {'lang': lang}
        req = requests.get(self.api_base + 'vocabularies', params=payload)
        req.raise_for_status()
        return req.json()['vocabularies']

    def search(self, query, lang=None, labellang=None, vocabs=None,
               type_=None, parent=None, group=None, maxhits=100, offset=0,
               fields=None, unique=False):
        """Search for concepts either within specified vocabularies or
        globally in all vocabularies."""

        payload = {'query': query,
                   'maxhits': maxhits,
                   'offset': offset,
                   'unique': unique}

        if lang is not None:
            payload['lang'] = lang
        if labellang is not None:
            payload['labellang'] = lang
        if vocabs is not None:
            if isinstance(vocabs, str):
                payload['vocab'] = vocabs
            else:  # a sequence such as a list?
                payload['vocab'] = ' '.join(vocabs)
        if type_ is not None:
            payload['type'] = type_
        if parent is not None:
            payload['parent'] = parent
        if group is not None:
            payload['group'] = group

        req = requests.get(self.api_base + 'search', params=payload)
        req.raise_for_status()
        return req.json()['results']

    def data(self, uri, vocid=None):
        """Return all information about a particular URI. If a vocabulary ID
        is given, look up the information from that vocabulary; otherwise,
        let Skosmos decide. The data is returned as an rdflib Graph."""

        payload = {'uri': uri, 'format': 'application/rdf+xml'}

        if vocid is not None:
            url = self.api_base + vocid + '/data'
        else:
            url = self.api_base + 'data'

        req = requests.get(url, params=payload)
        req.raise_for_status()
        graph = rdflib.Graph()
        graph.parse(data=req.content)
        return graph

    def types(self, lang, vocid=None):
        """Return information about concept and collection types available
        on the API endpoint, either from within a given vocabulary or
        globally. Type labels will be returned in the given language."""

        if vocid is not None:
            url = self.api_base + vocid + '/types'
        else:
            url = self.api_base + 'types'
        payload = {'lang': lang}
        req = requests.get(url, params=payload)
        req.raise_for_status()
        return req.json()['types']

    def get_vocabulary(self, vocid, lang=None):
        """Get information about a vocabulary by vocabulary ID. Labels will
        be returned in the given language."""

        payload = {}
        if lang is not None:
            payload['lang'] = lang
        req = requests.get(self.api_base + vocid + '/', params=payload)
        if req.status_code == 404:
            raise ValueError(req.text)
        req.raise_for_status()
        return req.json()

    def top_concepts(self, vocid, lang=None, scheme=None):
        """Get the top concepts of a vocabulary. Labels will be returned in
        the given language. An optional concept scheme URI can be specified
        to retrieve the top concepts within that scheme."""

        payload = {}
        if lang is not None:
            payload['lang'] = lang
        if scheme is not None:
            payload['scheme'] = scheme
        req = requests.get(self.api_base + vocid +
                           '/topConcepts', params=payload)
        if req.status_code == 404:
            raise ValueError(req.text)
        req.raise_for_status()
        return req.json()['topconcepts']

    def lookup(self, vocid, label, lang=None):
        """Return information about a concept by its label. The results
        will be returned as a list, with the best match first. If a language
        is given, restrict matching to labels in that language."""

        payload = {'label': label}
        if lang is not None:
            payload['lang'] = lang

        req = requests.get(self.api_base + vocid + '/lookup', params=payload)
        if req.status_code == 404:
            raise ValueError(req.text)
        req.raise_for_status()
        return req.json()['result']

    def groups(self, vocid, lang=None):
        """Get the thematic groups of a vocabulary. Labels will be returned
        in the given language."""

        payload = {}
        if lang is not None:
            payload['lang'] = lang
        req = requests.get(self.api_base + vocid + '/groups', params=payload)
        if req.status_code == 404:
            raise ValueError(req.text)
        req.raise_for_status()
        return req.json()['groups']
    
    def get_concept(self, vocid, uri):
        """get a Concept for performing concept-specific operations"""
        return SkosmosConcept(self.api_base, vocid, uri)

    def __str__(self):
        """Return a string representation of this object"""
        return "SkosmosClient(api_base='{}')".format(self.api_base)


if __name__ == '__main__':
    print("Demonstrating usage of SkosmosClient")

    print()

    print("* Creating a SkosmosClient object")
    skosmos = SkosmosClient()
    print("Now we have a SkosmosClient object:", skosmos)
    print()
    print("* Finding the available vocabularies")
    for vocab in skosmos.vocabularies(lang='en'):
        print("Vocabulary id: {:<16} title: {}".format(
            vocab['id'], vocab['title']))

    print()

    print("* Searching for concepts globally in all vocabularies")
    for result in skosmos.search("Stockholm*", lang="en"):
        print(result)

    print()

    print("* Searching for concepts within a single vocabulary")
    for result in skosmos.search("cosmolog*", vocabs="yso", lang="en"):
        print(result)

    print()
    print("* Looking up all information about a particular concept")
    graph = skosmos.data('http://www.yso.fi/onto/yso/p7160')
    print("Got {} triples of data".format(len(graph)))
    # Let's look at the preferred labels within that graph
    for uri, label in graph.subject_objects(SKOS.prefLabel):
        if label.language == 'en':
            print('<{}> has label "{}"@{}'.format(uri, label, label.language))

    print()
    print("* Looking up information about types within a vocabulary")
    for typeinfo in skosmos.types('en', vocid='yso'):
        print(typeinfo)

    print()
    print("* Looking up information about a particular vocabulary")
    yso = skosmos.get_vocabulary('yso', lang='en')
    for key, val in sorted(yso.items()):
        if key in ('@context', 'uri'):
            continue
        print("{:<20}: {}".format(key, val))

    print()
    print("* Looking up top level concepts for a vocabulary")
    for top_concept in skosmos.top_concepts('yso', lang='en'):
        print(top_concept)

    print()
    print("* Looking up a concept by its label")
    lookup_results = skosmos.lookup('yso', 'cosmology', lang='en')
    print(lookup_results)

    print()
    print("* Looking up the thematic groups of a vocabulary")
    for group in skosmos.groups('yso', lang='en'):
        print(group)
    
    print()
    print("* Performing operations on single concepts")
    prams = skosmos.get_concept('yso', 'http://www.yso.fi/onto/yso/p12345')
    print("YSO concept 'prams' label in the default language:", prams.label())
    print("YSO concept 'prams' label in English:", prams.label('en'))
    print("Broader concepts of 'prams' in YSO:")
    for bc in prams.broader('en'):
        print(bc)
    print("Transitive broader concepts of 'prams' in YSO:")
    for btc in prams.broaderTransitive('en'):
        print(btc)

    print("Narrower concepts of 'Hanko' in YSO places:")
    hanko = skosmos.get_concept('yso-paikat', 'http://www.yso.fi/onto/yso/p94126')
    for nc in hanko.narrower():
        print(nc)
    print("Related concepts of 'prams' in YSO:")
    for rc in prams.related('en'):
        print(rc)
