
import request_handler.request_handler as request_handler
import request_handler.arnoo_request_handler as arnoo_request_handler
import os
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
AI_ID_LIST = [
    "3126a0df-bbe8-4e80-b1f2-e7ff9c8dcff6",
    "640d3f58-5d67-43b6-8864-63753f4934a2",
    "2a96965c-b2f6-4850-a046-71fc952dee9e",
    "b23301a7-f523-4dac-8574-10522dba21b0",
    "e99505d2-a8ab-4551-9168-e256c26dc787"]
IMAGE_URL = {
    "flame": "http://192.168.5.130/upload/flame1.jpg",
    "human": "http://192.168.5.130/upload/human1.jpg",
    "pet": "http://192.168.5.130/upload/pet1.jpg",
    "package": "http://192.168.5.130/upload/package1.jpg",
    "vehicle": ""
}


def run_arnoo_accuracy_test(
    project_name,
        service_url,
        ai_id,
        image_url_file_path,
        result_file_path,
        monitor):

    # if os.path.isdir(result_file_path):
    #     sys.exit("{} is not a direct".format(result_file_path))

    handler = arnoo_request_handler.create_arnoo_accuracy_tester_updated(
        project_name,
        service_url,
        ai_id,
        image_url_file_path,
        result_file_path,
        monitor)

    structure = arnoo_request_handler.ArnooRequestStructure()
    structure.run_arnoo_accuracy_test(handler)

def run_package_positive():
    run_arnoo_accuracy_test(
        project_name="package_positive",
        service_url=ARNOO_URL,
        ai_id=AI_ID["package"],
        image_url_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/package_positive.txt",
        result_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_accuracy_result",
        monitor=True)

def run_package_negative():
    run_arnoo_accuracy_test(
        project_name="package_negative",
        service_url=ARNOO_URL,
        ai_id=AI_ID["package"],
        image_url_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/package_negative.txt",
        result_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_accuracy_result",
        monitor=True)

def run_pet_positive():
    run_arnoo_accuracy_test(
        project_name="pet_positive",
        service_url=ARNOO_URL,
        ai_id=AI_ID["pet"],
        image_url_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/pet_positive.txt",
        result_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_accuracy_result",
        monitor=True)

def run_pet_negative():
    run_arnoo_accuracy_test(
        project_name="pet_negative",
        service_url=ARNOO_URL,
        ai_id=AI_ID["pet"],
        image_url_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/pet_negative.txt",
        result_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_accuracy_result",
        monitor=True)

def run_human_positive():
    run_arnoo_accuracy_test(
        project_name="human_positive",
        service_url=ARNOO_URL,
        ai_id=AI_ID["human"],
        image_url_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/human_positive.txt",
        result_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_accuracy_result",
        monitor=True)

def run_human_negative():
    run_arnoo_accuracy_test(
        project_name="human_negative",
        service_url=ARNOO_URL,
        ai_id=AI_ID["human"],
        image_url_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/human_negative.txt",
        result_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_accuracy_result",
        monitor=True)

def run_vehicle_positive():
    run_arnoo_accuracy_test(
        project_name="vehicle_positive",
        service_url=ARNOO_URL,
        ai_id=AI_ID["vehicle"],
        image_url_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/vehicle_positive.txt",
        result_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_accuracy_result",
        monitor=True)
        
def run_vehicle_negative():
    run_arnoo_accuracy_test(
        project_name="vehicle_negative",
        service_url=ARNOO_URL,
        ai_id=AI_ID["vehicle"],
        image_url_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/vehicle_negative.txt",
        result_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_accuracy_result",
        monitor=True)

if __name__ == '__main__':

    # Package 
    run_package_positive()
    run_package_negative()

    # Pet 
    run_pet_positive()
    run_pet_negative()

    # Human 
    run_human_positive()
    run_human_negative()

    # vehicle
    run_vehicle_positive()
    run_vehicle_negative()
