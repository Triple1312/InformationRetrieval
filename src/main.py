from filter_research_gates_on_fulltext import filter_on_fulltext
from researchgate_scrape_all_publications import scrape_researchgate_publications

if __name__ == "__main__":
    publications = scrape_researchgate_publications("covid", amount=3)
    print("got publications")
    print(filter_on_fulltext(publications))
