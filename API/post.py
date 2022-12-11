import requests


def main():
    url: str = "http://127.0.0.1:8000/apiv1/predict"
    pdf = open("../Examples/PBRNet-TIP.pdf", "rb")

    res = requests.post(url, files={"PDF": pdf})

    if res.ok:
        j = res.json()
        print(j["Abstract"])
    else:
        print("Failure")


if __name__ == "__main__":
    main()
