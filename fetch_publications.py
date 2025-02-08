import scholarly
import datetime

# Replace this with your actual Google Scholar ID
SCHOLAR_ID = "tQNSWaAAAAAJ&hl"
OUTPUT_FILE = "publications.md"  # File to update on GitHub

def fetch_publications(scholar_id):
    """Fetches the latest publications from Google Scholar."""
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=["publications"])
    
    publications = []
    for pub in author["publications"]:
        scholarly.fill(pub)  # Fetch full details
        title = pub["bib"]["title"]
        link = pub["pub_url"] if "pub_url" in pub else "#"
        year = pub["bib"].get("pub_year", "N/A")
        publications.append(f"- **{title}** ({year}) [Link]({link})")
    
    return publications

def update_markdown(publications):
    """Updates the publications markdown file."""
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# My Research Publications\n\n")
        f.write("## Latest Papers\n")
        f.write("\n".join(publications))
        f.write(f"\n\n_Updated: {datetime.datetime.now().strftime('%Y-%m-%d')}_")

if __name__ == "__main__":
    publications = fetch_publications(SCHOLAR_ID)
    update_markdown(publications)
    print(f"Updated {OUTPUT_FILE} with {len(publications)} publications.")
