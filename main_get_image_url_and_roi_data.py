
from file_handler import file_handler


def get_image_url(
        input_folder_path,
        path_remoeve_keywords,
        path_keep_keywords,
        replace_remove,
        replace_add,
        export_file_path):

    handler = file_handler.create_export_image_url_handler(
        input_folder_path,
        path_remoeve_keywords,
        path_keep_keywords,
        replace_remove,
        replace_add,
        export_file_path
    )

    structure = file_handler.FilePathStructure()
    structure.export_image_url_and_ROI_points(handler)


REMOVE_KEYWORDS = ["aws", "jpg", "NG", "xlsx", "git","classes"]


def run_package_positive():
    get_image_url(
        input_folder_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_package",
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["txt", "Positive"],
        replace_remove="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_package/",
        replace_add="http://192.168.5.130/upload/Package/",
        export_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url_and_ROI/package_positive.txt")


def run_human_positive():
    get_image_url(
        input_folder_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_human",
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["txt", "positive"],
        replace_remove="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_human/",
        replace_add="http://192.168.5.130/upload/Human/Human/",
        export_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url_and_ROI/human_positive.txt")


def run_pet_positive():
    get_image_url(
        input_folder_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_pet",
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["txt", "posi"],
        replace_remove="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_pet/",
        replace_add="http://192.168.5.130/upload/Pet/Pet/",
        export_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url_and_ROI/pet_positive.txt")


def run_vehicle_positive():
    get_image_url(
        input_folder_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_vehicle",
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["txt", "positive"],
        replace_remove="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_vehicle/",
        replace_add="http://192.168.5.130/upload/Vehicle/",
        export_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url_and_ROI/vehicle_positive.txt")


if __name__ == '__main__':
    run_package_positive()
    # run_human_positive()
    # run_pet_positive()
    # run_vehicle_positive()
