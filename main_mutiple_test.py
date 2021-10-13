

import request_handler.arnoo_request_handler as arnoo_request_handler
import sys

# python3 -m unittest -v

ARNOO_URL = 'http://test-agent.arnoo.com/aims'
AI_ID = {
    "human": "3126a0df-bbe8-4e80-b1f2-e7ff9c8dcff6",
    "flame": "640d3f58-5d67-43b6-8864-63753f4934a2",
    "pet": "2a96965c-b2f6-4850-a046-71fc952dee9e",
    "package": "b23301a7-f523-4dac-8574-10522dba21b0",
    "vehicle": "e99505d2-a8ab-4551-9168-e256c26dc787"
}
AI_ID_LIST = ["3126a0df-bbe8-4e80-b1f2-e7ff9c8dcff6", "2a96965c-b2f6-4850-a046-71fc952dee9e",
              "b23301a7-f523-4dac-8574-10522dba21b0", "e99505d2-a8ab-4551-9168-e256c26dc787"]
IMAGE_URL = {
    "flame": "http://192.168.5.130/upload/flame1.jpg",
    "human": "http://192.168.5.130/upload/human1.jpg",
    "pet": "http://192.168.5.130/upload/pet1.jpg",
    "package": "http://192.168.5.130/upload/package1.jpg",
    "vehicle": ""
}
THRESHOLD = {"human": 0.50, "pet": 0.5, "vehicle": 0.5}
ROI = {'vehicle': [(54, 104, 568, 403), (423, 132, 501, 159),
                   (458, 128, 530, 157), (0, 142, 56, 183)]}


def run_mutiple_test(algorithm_name, project_name, image_url_list_path):
    structure = arnoo_request_handler.ArnooRequestStructure()

    #
    image_url_list = []
    with open(image_url_list_path, mode='r') as import_file:
        import_data = import_file.readlines()
        for i in import_data:
            image_url_list.append(i.strip('\n'))

    headers = {"Content-Type": "application/json"}
    body = {
        "AI-CLASS-ID": AI_ID_LIST,
        "ID": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "TIMESTAMP": "1606358900",
        "PRIVATE-TOKEN": THRESHOLD,
        "IMAGE":
        {
            "src": "",
            "srcType": "URL",
            "width": 1920,
            "height": 1080,
            "channel": 3,
            "format": "RGB",
            "createTime": "1606358900"
        },
        "ROI": ROI,
        "DEVICE-INFO":
        {
            "id": "3896965f-6f1e-41c6-8640-70d5d42820ce",
            "location": "26.9839048309, 124.9084309890",
        },
    }
    handler = arnoo_request_handler.create_arnoo_accuracy_tester(
        project_name=project_name,
        service_url=ARNOO_URL,
        image_url_list=image_url_list,
        # ai_id=AI_ID[project],
        ai_id=AI_ID_LIST,
        thread_times=1,
        monitor=True,
        headers=headers,
        body=body)

    #
    structure.run_arnoo_mutiple_test(handler)


if __name__ == '__main__':
    run_mutiple_test(
        algorithm_name="mutiple",
        project_name="mutiple",
        image_url_list_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/mutiple.txt")
