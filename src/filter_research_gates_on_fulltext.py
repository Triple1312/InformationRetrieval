import json
from parsel import Selector
from playwright.sync_api import sync_playwright


def filter_on_fulltext(pubs: [json]):
    publications = json.loads(pubs)
    # print(publications)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=50)
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36")

        filtered: [json] = []
        # publications_json = json.load(publications)
        for publication in publications:
            # print("pub", publication)
            link = publication["link"]
            page.goto(f"{link}")
            selector = Selector(text=page.content())
            aS = selector.xpath('//a').getall()
            # print (aS)
            for a in aS:
                aSelector = Selector(text=a)
                but_list = aSelector.xpath('//span[contains(., "Download full-text")]').getall()

                if not len(but_list) == 0:
                    link = aSelector.xpath('//a/@href').getall()[0]
                    if link.startswith("https://"):
                        filtered.append({"publication": publication, "link": link})
                        print(link)
                        break
        return filtered



j = [
  {
    "title": "A Comparison Of Physicochemical Properties Of Hamburger Steaks Made With Pork, Beef And Venison",
    "link": "https://www.researchgate.net/publication/365283276_A_comparison_of_physicochemical_properties_of_hamburger_steaks_made_with_pork_beef_and_venison?_sg=HpCF1rQ2ozI8zJVB7Q-BPz14q_dFVM1th8CYeSpd3akRjxZQVicqCuB8Qt4ys0Pv0vMmCO40JGQdIAs",
    "source_link": "https://www.researchgate.netNone",
    "publication_type": "Article",
    "publication_date": "Oct 2022",
    "publication_doi": "DOI: 10.11002/kjfp.2022.29.6.943",
    "publication_isbn": "ISBN: 1738-7248",
    "authors": [
      "Nan-Hee Lee",
      "Ung-Kyu Choi"
    ]
  },
  {
    "title": "Effects Of Incorporating Conjugated Linoleic Acid Into Hamburger Patties And Whey Protein Isolate Based Edible Film Formulation On Lipid Oxidation And Microbial Growth In Hamburger Patties",
    "link": "https://www.researchgate.net/publication/362594357_Effects_of_incorporating_conjugated_linoleic_acid_into_hamburger_patties_and_whey_protein_isolate_based_edible_film_formulation_on_lipid_oxidation_and_microbial_growth_in_hamburger_patties?_sg=B7MQRVaGNNs_UwsWG_E-_TYAAU_1Tx4IYp9MJOzJHc1DjnjVPYpaOA0abrn_3QaqMctk10R5ejiUAOs",
    "source_link": "https://www.researchgate.netNone",
    "publication_type": "Article",
    "publication_date": "Aug 2022",
    "publication_doi": "DOI: 10.1111/jfpp.16984",
    "publication_isbn": "ISBN: 0145-8892",
    "authors": [
      "Ayşenur Tan",
      "Betül Ağaç",
      "Damla Bilecen Şen",
      "Birol Kılıç"
    ]
  },
  {
    "title": "Promoting Students� Reading Achievement Using Hamburger Strategy",
    "link": "https://www.researchgate.net/publication/359657324_Promoting_Students_Reading_Achievement_Using_Hamburger_Strategy?_sg=cHyz3jMu6ZtYXUzmxAdlQAml8rrg52GkRXBgMbTfn1J1-1l-ntEzyo0uQHMHdX1gAXApLcFyA5BySX0",
    "source_link": "https://www.researchgate.netNone",
    "publication_type": "Article",
    "publication_date": "Dec 2021",
    "publication_doi": "DOI: 10.32663/edu-ling.v5i1.2553",
    "publication_isbn": "ISBN: 2614-7343",
    "authors": [
      "Arief Pamuji",
      "Dewi Sartika"
    ]
  },
  {
    "title": "The Strong Truncated Hamburger Moment Problem With And Without Gaps",
    "link": "https://www.researchgate.net/publication/362337692_The_strong_truncated_Hamburger_moment_problem_with_and_without_gaps?_sg=L7dcwbL1jalXtUtw8ShXqt0Bl7k4D4J1IFRTBl-8h3tudKSXQ1INXnbgrYzsAPzlRbJd349-pEZJ2Mc",
    "source_link": "https://www.researchgate.netNone",
    "publication_type": "Article",
    "publication_date": "Jul 2022",
    "publication_doi": "DOI: 10.1016/j.jmaa.2022.126563",
    "publication_isbn": "ISBN: 1096-0813",
    "authors": [
      "Aljaž Zalar"
    ]
  },
  {
    "title": "Physicochemical And Sensory Properties Of Hamburger Steak Made With Venison",
    "link": "https://www.researchgate.net/publication/357740369_Physicochemical_and_sensory_properties_of_hamburger_steak_made_with_venison?_sg=zbIJZMrdlRzZrOuCULxeC3LicVpPO9XL8MBk3Gs4BhmbHVVxROt4EFmnSZh_BnpKJZORWBXNmChEivs",
    "source_link": "https://www.researchgate.netNone",
    "publication_type": "Article",
    "publication_date": "Dec 2021",
    "publication_doi": "DOI: 10.11002/kjfp.2021.28.7.908",
    "publication_isbn": "ISBN: 1738-7248",
    "authors": [
      "Nan-Hee Lee",
      "Ung-Kyu Choi"
    ]
  },
  {
    "title": "The Weyl Matrix Balls Corresponding To The Matricial Truncated Hamburger Moment Problem",
    "link": "https://www.researchgate.net/publication/361212445_The_Weyl_matrix_balls_corresponding_to_the_matricial_truncated_Hamburger_moment_problem?_sg=YQzptHDfGrfjYNZhs9lOl75Jaap8wYbkI_OSVYnA3Uc3k4xhIxD5LkIfQA_F6kS4gnryu6XoJFpz9og",
    "source_link": "https://www.researchgate.netNone",
    "publication_type": "Article",
    "publication_date": "Jun 2022",
    "publication_doi": "DOI: 10.1016/j.laa.2022.06.003",
    "publication_isbn": "ISBN: 0024-3795",
    "authors": [
      "Bernd Fritzsche",
      "Bernd Kirstein",
      "Susanne Kley",
      "Conrad Mädler"
    ]
  },
  {
    "title": "Antibiotic Resistance In The Pathogenic Foodborne Bacteria Isolated From Raw Kebab And Hamburger: Phenotypic And Genotypic Study",
    "link": "https://www.researchgate.net/publication/355143403_Antibiotic_resistance_in_the_pathogenic_foodborne_bacteria_isolated_from_raw_kebab_and_hamburger_phenotypic_and_genotypic_study?_sg=peNlgoPFS90OxD53mwWqKhrEPCeyzF4XQWC1urLTWvndinnIqfag3DEr1WFPVPD_bK6rQfhCmIezziI",
    "source_link": "https://www.researchgate.netNone",
    "publication_type": "Article",
    "publication_date": "Oct 2021",
    "publication_doi": "DOI: 10.1186/s12866-021-02326-8",
    "publication_isbn": "ISBN: 1471-2180",
    "authors": [
      "Maryam Rajaei",
      "Mir-Hassan Moosavy",
      "Sahar Nouri Gharajalar",
      "Seyed Amin Khatibi"
    ]
  },
  {
    "title": "Protein Quality And Sensory Perception Of Hamburgers Based On Quinoa, Lupin And Corn",
    "link": "https://www.researchgate.net/publication/364971023_Protein_Quality_and_Sensory_Perception_of_Hamburgers_Based_on_Quinoa_Lupin_and_Corn?_sg=8rNdjxxrNtm0Atpx2AsxEQjfpSaG51IFMcePO9KvFN4Dhdnn2O4Hk86ecQeBQqVq3lfv0ldDq_H36aM",
    "source_link": "https://www.researchgate.netNone",
    "publication_type": "Article",
    "publication_date": "Oct 2022",
    "publication_doi": "DOI: 10.3390/foods11213405",
    "publication_isbn": "ISBN: 2304-8158",
    "authors": [
      "Raquel Chilón-Llico",
      "Lilia Siguas-Cruzado",
      "Carmen R. Apaza-Humerez",
      "Wilter C. Morales-García",
      "Reynaldo J. Silva-Paz"
    ]
  },
]

# filter_on_fulltext(j)
