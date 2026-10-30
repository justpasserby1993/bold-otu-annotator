# bold-otu-annotator
A lightweight tool to retrieve taxonomic annotations (Kingdom-Phylum-Class-Order-Family-Genus-Species) for OTUs from BOLD Systems for metabarcoding (DNA metabarcoding) data.

# bold-otu-annotator
> Automatically fetch taxonomic information (Kingdom, Phylum, Class, Order, Family, Genus, Species) of OTUs from BOLD Systems for DNA metabarcoding data.

## 📖 About
This tool is designed for **DNA metabarcoding / macrobarcoding OTU analysis**.
Given a list of OTU sequences or BOLD IDs, it queries the BOLD Systems database in batch and retrieves full taxonomic ranks (Kingdom-Phylum-Class-Order-Family-Genus-Species) for each OTU, outputting a clean annotation table for downstream ecology analysis.

### What this tool does
- Batch query OTU against BOLD Systems
- Extract full taxonomic ranks (界门纲目科属种 / taxonomic ranks)
- Export annotation result as CSV/TSV for QIIME2, R, Python downstream analysis
- Handle failed queries, empty hits and duplicate OTUs gracefully
- Rate-limit request to avoid overwhelming BOLD API

### What this tool NOT do
- It **does not** perform sequence clustering to generate OTUs (use VSEARCH, USEARCH, QIIME2 for OTU clustering)
- It **does not** do sequence alignment / local blast
- Annotation quality fully depends on BOLD public records

## 🧬 Background
BOLD (Barcode of Life Data Systems) is the core public reference database for COI and other barcode markers for animal/plant/fungal DNA barcoding.
For metabarcoding studies, after OTU clustering, researchers usually need to assign taxonomy for each OTU. This script automates the lookup workflow instead of manual web searching.

## ✨ Features
- Simple input: OTU list / fasta / sequence table
- Output: CSV table with columns: `otu_id, kingdom, phylum, class, order, family, genus, species, bold_id, match_score, note`
- Retry & sleep control for BOLD API
- Skip repeated OTUs to reduce redundant requests
- Log file for tracking failed queries

## 📋 Requirements
- Python >=3.8
- `requests`
- `pandas`
- `biopython` (optional, for FASTA parsing)

```bash
pip install requests pandas biopython
