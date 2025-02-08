from scholarly import scholarly
import datetime
import time

# Replace with your actual Google Scholar ID
SCHOLAR_ID = "tQNSWaAAAAAJ&hl"  # Replace with your Google Scholar ID
OUTPUT_FILE = "publications.md"

def fetch_publications(scholar_id):
    """Fetches the latest publications from Google Scholar using the Scholar ID."""
    try:
        print("Fetching author details...")
        author = scholarly.search_author_id(scholar_id)  # Fetch author by ID
        author = scholarly.fill(author)  # Fetch full details about the author
        print("Author details fetched. Fetching publications...")

        publications = []
        for pub in author.get("publications", []):
            print(f"Fetching details for publication: {pub['bib'].get('title', 'Untitled')}")
            pub_filled = scholarly.fill(pub)  # Fetch full details for each publication
            title = pub_filled["bib"].get("title", "Untitled")
            year = pub_filled["bib"].get("year", "N/A")
            link = pub_filled.get("pub_url", "#")
            publications.append(f"- **{title}** ({year}) [Link]({link})")
            time.sleep(5)  # Add a delay to avoid being blocked
        
        return publications
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def update_markdown(publications):
    """Updates the publications markdown file."""
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write("# 📚 My Research Publications\n\n")
            f.write("## 📄 Latest Papers\n")
            f.write("\n".join(publications))
            f.write(f"\n\n_Last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_")
    except Exception as e:
        print(f"An error occurred while updating the markdown file: {e}")

if __name__ == "__main__":
    publications = fetch_publications(SCHOLAR_ID)
    if publications:
        update_markdown(publications)
        print(f"Updated {OUTPUT_FILE} with {len(publications)} publications.")
    else:
        print("No publications found or an error occurred.")