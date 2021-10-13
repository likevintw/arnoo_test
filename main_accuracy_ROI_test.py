from logging import Handler
from file_handler import file_handler
import request_handler.arnoo_request_handler as arnoo_request_handler
import json


def export_request_information(
    image_folder_path,
    image_path_keep_keyword,
    image_path_remove_keyword,
    image_path_replace,
    information_export_path
):
    # get image url
    image_url_handler = file_handler.create_file_handler(
        input_folder_path=image_folder_path,
        search_level=5
    )
    image_url_handler.run_path_algorithm(image_url_handler.search_level)
    # image path remove keyword
    for i in image_path_remove_keyword:
        image_url_handler.file_path_list = image_url_handler.remove_pathlist_keyword(
            path_list=image_url_handler.file_path_list,
            keyword=i)
    # image path keep keyword
    for i in image_path_keep_keyword:
        image_url_handler.file_path_list = image_url_handler.keep_pathlist_keyword(
            path_list=image_url_handler.file_path_list,
            keyword=i)
    # get dictionary
    image_path_dict = image_url_handler.create_file_dictionary(
        image_url_handler.file_path_list,
        image_path_replace)

    # image_url_handler.show_image_dictionary(image_path_dict)
    url_data = image_url_handler.get_image_url_and_ROI_points(image_path_dict)
    image_url_handler.show_image_dictionary(url_data)
    image_url_handler.export_json(information_export_path, url_data)


def export_all_project_request_information():
    # pet
    export_request_information(
        image_folder_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_pet",
        image_path_keep_keyword=[".jpg", "positive"],
        image_path_remove_keyword=["aws"],
        image_path_replace=[
            "/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_pet/",
            "http://192.168.5.130/upload/Pet/Pet/"],
        information_export_path="./ROI_data/pet.txt"
    )


# def run_all_project_request():
#     # human
#     run_accuracy_test(
#         project_name="human",
#         ai_id=["3126a0df-bbe8-4e80-b1f2-e7ff9c8dcff6"],
#         service_url="http://test-agent.arnoo.com/aims",
#         ROI_json_data="./ROI_data/human.txt")

#     # package
#     run_accuracy_test(
#         project_name="package",
#         ai_id=["b23301a7-f523-4dac-8574-10522dba21b0"],
#         service_url="http://test-agent.arnoo.com/aims",
#         ROI_json_data="./ROI_data/package.txt")

#     # vehicle
#     run_accuracy_test(
#         project_name="vehicle",
#         ai_id=["e99505d2-a8ab-4551-9168-e256c26dc787"],
#         service_url="http://test-agent.arnoo.com/aims",
#         ROI_json_data="./ROI_data/vehicle.txt")


def run_human_case():
    handler = arnoo_request_handler.create_arnoo_test_handler_20210914(
        project="human",
        ai_id=["3126a0df-bbe8-4e80-b1f2-e7ff9c8dcff6"],
        service_url="http://test-agent.arnoo.com/aims",
        ROI_json_path="./ROI_data/human.txt"
    )
    structure = arnoo_request_handler.ArnooRequestStructure()
    structure.run_arnoo_accuracy_ROI_test(handler)


def run_pet_case():
    handler = arnoo_request_handler.create_arnoo_test_handler_20210914(
        project="pet",
        ai_id=["2a96965c-b2f6-4850-a046-71fc952dee9e"],
        service_url="http://test-agent.arnoo.com/aims",
        ROI_json_path="./ROI_data/pet.txt"
    )
    structure = arnoo_request_handler.ArnooRequestStructure()
    structure.run_arnoo_accuracy_ROI_test(handler)


def run_package_case():
    handler = arnoo_request_handler.create_arnoo_test_handler_20210914(
        project="package",
        ai_id=["b23301a7-f523-4dac-8574-10522dba21b0"],
        service_url="http://test-agent.arnoo.com/aims",
        ROI_json_path="./ROI_data/package.txt"
    )
    structure = arnoo_request_handler.ArnooRequestStructure()
    structure.run_arnoo_accuracy_ROI_test(handler)


def run_vehicle_case():
    handler = arnoo_request_handler.create_arnoo_test_handler_20210914(
        project="vehicle",
        ai_id=["e99505d2-a8ab-4551-9168-e256c26dc787"],
        service_url="http://test-agent.arnoo.com/aims",
        ROI_json_path="./ROI_data/vehicle.txt"
    )
    structure = arnoo_request_handler.ArnooRequestStructure()
    structure.run_arnoo_accuracy_ROI_test(handler)


def run_test_case():
    handler = arnoo_request_handler.create_arnoo_test_handler_20210914(
        project="vehicle",
        ai_id=["e99505d2-a8ab-4551-9168-e256c26dc787"],
        service_url="http://172.25.11.91:6001/aims",
        ROI_json_path="./ROI_data/vehicle.txt"
    )
    structure = arnoo_request_handler.ArnooRequestStructure()
    structure.run_arnoo_accuracy_ROI_test(handler)


if __name__ == '__main__':
    run_human_case()
    run_pet_case()
    run_package_case()
    run_vehicle_case()
    # run_test_case()
