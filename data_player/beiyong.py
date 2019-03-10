
#######------------------------   For csv file   ------------------------------
<TriplesMapGeonames>
a rr:TriplesMap;

# Define the data source (file location)
rml:logicalSource [
    rml:source "/Users/gabriellapascha/Documents/DKE/Building and Mining Knowledge Graphs/um-kg-course-master/countryInfo.csv";
rml:referenceFormulation ql:CSV
];

# Define the subject of the generated statements
rr:subjectMap [ rr:template "http://geonames.org/country/{ISO3}" ;
rr:class gn:Country ];

# Map the country name to rdfs:label
rr:predicateObjectMap [
rr:predicate rdfs:label ;
rr:objectMap [ rml:reference "Country" ]
] ;

rr:predicateObjectMap [
rr:predicate gn:country_key ;
rr:objectMap [ rml:reference "ISO3" ]
] ;

# Define the object of the population property as an integer
rr:predicateObjectMap [
rr:predicate gn:population ;
rr:objectMap [ rml:reference "Population" ; rr:datatype xsd:integer ]
] ;

rr:predicateObjectMap [
rr:predicate gn:area ;
rr:objectMap [ rml:reference "Area" ; rr:datatype xsd:integer ]
] ;

# Generate a URI for the continent object
rr:predicateObjectMap [
rr:predicate gn:continent ;
rr:objectMap [ rr:template "http://geonames.org/continent/{Continent}" ]
] .



#######------------------------   XML   ------------------------------

# Generates GDP entries yearly for each country from WorldBank data
<TriplesMapGdpEntries>
 a rr:TriplesMap;

rml:logicalSource [
rml:source "/Users/gabriellapascha/Documents/DKE/Building and Mining Knowledge Graphs/um-kg-course-master/gdp_worldbank-full.xml";
rml:referenceFormulation ql:XPath ;
rml:iterator "/Root/data/record"
];

# Generate a URI for each GDP yearly entry for each country
rr:subjectMap [ rr:template "http://worldbank.org/country/{country/@key}/gdp/{year}" ;
rr:class wd:GdpEntry ];

# Link to the country
rr:predicateObjectMap [
rr:predicate wd:country ;
rr:objectMap [ rml:reference "country" ]
];


rr:predicateObjectMap [
rr:predicate wd:country_key ;
rr:objectMap [ rml:reference "country/@key" ]
];

rr:predicateObjectMap [
rr:predicate wd:year ;
rr:objectMap [ rml:reference "year"; rr:datatype xsd:integer]
];

rr:predicateObjectMap [
rr:predicate wd:gdp ;
rr:objectMap [ rml:reference "value" ; rr:datatype xsd:double]
]


.