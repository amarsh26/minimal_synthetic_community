/*
A KBase module: minimal_synthetic_community
This sample module contains one small method that filters contigs.
*/

module minimal_synthetic_community {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_minimal_synthetic_community(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
