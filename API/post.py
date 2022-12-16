import requests
from Test import test_stub, pretty_format


def post_pdfs():
    url: str = "http://127.0.0.1:8000/apiv1/document"
    papers: list = [
        "../Examples/A_treatment_recommender_clinical_decision_support_.pdf",
        "../Examples/PBRNet-TIP.pdf",
        "../Examples/Naive-Bayes.pdf"
    ]
    for paper in papers:
        pdf = open(paper, "rb")
        res = requests.post(url, files={"PDF": pdf}, data={"Title": pretty_format(paper), "Abstract": "Abstract"})
        if res.ok:
            print("Success")
        else:
            print("Failure")



def main():
    url: str = "http://127.0.0.1:8000/apiv1/train/0.1"
    pdf = open("../Examples/Jaccard-Index.pdf", "rb")
    res = requests.post(url, files={"file": pdf})

    if res.ok:
        j = res.json()
        print(j["Jaccard"])
        print("=====================================")
        print(j["Abstract"])
    else:
        print("Failure")


if __name__ == "__main__":
    test_stub()
