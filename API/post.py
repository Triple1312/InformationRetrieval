import requests


def main():
    url: str = "http://127.0.0.1:8000/apiv1/document"
    pdf = open("../Examples/PBRNet-TIP.pdf", "rb")

    data = {
        "Title": "PBR-Net: Imitating Physically Based Rendering Using Deep Neural Network",
        "Abstract": '''Physically based rendering has been widely used to
generate photo-realistic images, which greatly impacts industry
by providing appealing rendering, such as for entertainment
and augmented reality, and academia by serving large scale
high-fidelity synthetic training data for data hungry methods like
deep learning. However, physically based rendering heavily relies
on ray-tracing, which can be computational expensive in complicated environment and hard to parallelize. In this paper, we propose an end-to-end deep learning based approach to generate
physically based rendering efficiently. Our system consists of two
stacked neural networks, which effectively simulates the physical
behavior of the rendering process and produces photo-realistic
images. The first network, namely shading network, is designed
to predict the optimal shading image from surface normal,
depth and illumination; the second network, namely composition
network, learns to combine the predicted shading image with the
reflectance to generate the final result. Our approach is inspired
by intrinsic image decomposition, and thus it is more physically
reasonable to have shading as intermediate supervision. Extensive
experiments show that our approach is robust to noise thanks to
a modified perceptual loss and even outperforms the physically
based rendering systems in complex scenes given a reasonable
time budget''',
        'csrfmiddlewaretoken': '{{ csrf_token }}',
    }

    res = requests.post(url, files={"PDF": pdf}, data=data)

    if res.ok:
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    main()
