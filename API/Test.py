import requests
import time
import matplotlib.pyplot as plt


def pretty_format(filename) -> str:
    # removes all / and file extensions
    x = filename.split("/")
    x = x[len(x) - 1]
    x = x.split(".")
    x = x[0]
    return x


def test_stub():
    base_url: str = "http://127.0.0.1:8000/apiv1/train/"
    papers: list = [
        "../Examples/A_treatment_recommender_clinical_decision_support_.pdf",
        "../Examples/PBRNet-TIP.pdf",
        "../Examples/Naive-Bayes.pdf"
    ]
    percentages: [float] = [0.5, 0.4, 0.3, 0.2, 0.1, 0.7, 0.5, 0.1, 0.05, 0.01, 0.002]
    result_file = open("results.txt", "w")
    for paper in papers:
        single_result: dict = {}
        result_file.write("Paper: " + paper + "\n")
        jaccards: [float] = []
        for percentage in percentages:
            print("Testing " + paper + " with " + str(percentage))
            url = base_url + str(percentage)
            pdf = open(paper, "rb")
            res = requests.post(url, files={"file": pdf})
            if res.ok:
                j = res.json()
                jaccards.append(j["Jaccard"])
                result_file.write(str(percentage) + ": " + str(j["Jaccard"]) + "\n")
            else:
                print("Failure")
            time.sleep(2)  # prevent spamming the server
        pretty_name = pretty_format(paper)
        plt.figure()
        plt.title(pretty_name)
        plt.xlabel('Percentage')
        plt.ylabel('Jaccard')
        plt.plot(percentages, jaccards)
        plt.show()
        plt.savefig(pretty_name + ".png")

    result_file.close()
