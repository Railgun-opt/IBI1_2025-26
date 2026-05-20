"""
Practical 14 - Gene Ontology XML Parser
Uses both DOM and SAX to find the GO term with the most <is_a> elements
in each of the three ontologies: molecular_function, biological_process, cellular_component.
Also times both approaches and compares performance.
"""

import xml.dom.minidom as minidom
import xml.sax
from datetime import datetime


# ─── DOM approach ──────────────────────────────────────────────

def run_dom(filepath):
    """Parse the GO xml file using DOM and return results for each ontology."""

    start = datetime.now()

    doc = minidom.parse(filepath)
    terms = doc.getElementsByTagName("term")

    # keep track of the best (most is_a elements) term per ontology
    results = {
        "molecular_function": {"id": "", "name": "", "count": 0},
        "biological_process": {"id": "", "name": "", "count": 0},
        "cellular_component": {"id": "", "name": "", "count": 0},
    }

    for term in terms:
        # grab the namespace to figure out which ontology this term belongs to
        ns_nodes = term.getElementsByTagName("namespace")
        if not ns_nodes:
            continue
        namespace = ns_nodes[0].firstChild.nodeValue.strip()

        # only care about the three main ontologies
        if namespace not in results:
            continue

        # count how many <is_a> elements this term has
        is_a_count = len(term.getElementsByTagName("is_a"))

        # update if this term beats the current record for its ontology
        if is_a_count > results[namespace]["count"]:
            id_nodes = term.getElementsByTagName("id")
            name_nodes = term.getElementsByTagName("name")
            results[namespace]["id"] = id_nodes[0].firstChild.nodeValue.strip() if id_nodes else "N/A"
            results[namespace]["name"] = name_nodes[0].firstChild.nodeValue.strip() if name_nodes else "N/A"
            results[namespace]["count"] = is_a_count

    elapsed = datetime.now() - start
    return results, elapsed


# ─── SAX approach ──────────────────────────────────────────────

class GOTermHandler(xml.sax.ContentHandler):
    """
    SAX handler that watches for <term> blocks and tracks which GO term
    has the most <is_a> elements in each of the three ontologies.
    """

    def __init__(self):
        super().__init__()
        self.current_tag = ""

        # per-term state — reset every time we enter a new <term>
        self.cur_id = ""
        self.cur_name = ""
        self.cur_namespace = ""
        self.cur_is_a_count = 0

        # best result per ontology
        self.results = {
            "molecular_function": {"id": "", "name": "", "count": 0},
            "biological_process": {"id": "", "name": "", "count": 0},
            "cellular_component": {"id": "", "name": "", "count": 0},
        }

    def startElement(self, tag, attrs):
        self.current_tag = tag

        # hitting a new <term> means we should reset the per-term state
        if tag == "term":
            self.cur_id = ""
            self.cur_name = ""
            self.cur_namespace = ""
            self.cur_is_a_count = 0

        # every <is_a> tag we encounter is one more parent reference
        if tag == "is_a":
            self.cur_is_a_count += 1

    def characters(self, content):
        text = content.strip()
        if not text:
            return

        # accumulate text — characters() may fire more than once per element
        # so we concatenate instead of overwriting
        if self.current_tag == "id":
            self.cur_id += text
        elif self.current_tag == "name":
            self.cur_name += text
        elif self.current_tag == "namespace":
            self.cur_namespace += text

    def endElement(self, tag):
        # when </term> closes, we have all the info for one GO term
        if tag == "term":
            ns = self.cur_namespace
            if ns in self.results and self.cur_is_a_count > self.results[ns]["count"]:
                self.results[ns]["id"] = self.cur_id
                self.results[ns]["name"] = self.cur_name
                self.results[ns]["count"] = self.cur_is_a_count

        self.current_tag = ""


def run_sax(filepath):
    """Parse the GO xml file using SAX and return results for each ontology."""

    start = datetime.now()

    parser = xml.sax.make_parser()
    handler = GOTermHandler()
    parser.setContentHandler(handler)
    parser.parse(filepath)

    elapsed = datetime.now() - start
    return handler.results, elapsed


# ─── main ──────────────────────────────────────────────────────

if __name__ == "__main__":
    filepath = "go_obo.xml"

    # --- DOM ---
    dom_results, dom_time = run_dom(filepath)

    print("=" * 55)
    print("DOM results")
    print("=" * 55)
    for ontology in ["molecular_function", "biological_process", "cellular_component"]:
        r = dom_results[ontology]
        print(f"\n  {ontology}:")
        print(f"    GO ID:   {r['id']}")
        print(f"    Name:    {r['name']}")
        print(f"    is_a #:  {r['count']}")
    print(f"\n  Time: {dom_time.total_seconds():.4f}s")

    # --- SAX ---
    sax_results, sax_time = run_sax(filepath)

    print("\n" + "=" * 55)
    print("SAX results")
    print("=" * 55)
    for ontology in ["molecular_function", "biological_process", "cellular_component"]:
        r = sax_results[ontology]
        print(f"\n  {ontology}:")
        print(f"    GO ID:   {r['id']}")
        print(f"    Name:    {r['name']}")
        print(f"    is_a #:  {r['count']}")
    print(f"\n  Time: {sax_time.total_seconds():.4f}s")

    # --- comparison ---
    print("\n" + "=" * 55)
    print("Comparison")
    print("=" * 55)
    print(f"  DOM took {dom_time.total_seconds():.4f}s")
    print(f"  SAX took {sax_time.total_seconds():.4f}s")
    if sax_time < dom_time:
        print("  -> SAX was faster")
    else:
        print("  -> DOM was faster")

    # sanity check — both methods should give the same answer
    match = True
    for ontology in ["molecular_function", "biological_process", "cellular_component"]:
        if dom_results[ontology]["id"] != sax_results[ontology]["id"]:
            print(f"  WARNING: mismatch for {ontology}!")
            match = False
    if match:
        print("  Both methods returned identical results.")
