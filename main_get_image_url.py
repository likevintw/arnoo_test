
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
    structure.export_image_url(handler)


REMOVE_KEYWORDS = ["aws", "txt", "NG","xlsx","git"]

def run_package_positive():
    get_image_url(
        input_folder_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_package",
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "Positive"],
        replace_remove="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_package/",
        replace_add="http://192.168.5.130/upload/Package/",
        export_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/package_positive.txt")


def run_package_negative():
    get_image_url(
        input_folder_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_package",
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "Negative"],
        replace_remove="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_package/",
        replace_add="http://192.168.5.130/upload/Package/",
        export_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/package_negative.txt")


def run_human_positive():
    get_image_url(
        input_folder_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_human",
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "positive"],
        replace_remove="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_human/",
        replace_add="http://192.168.5.130/upload/Human/Human/",
        export_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/human_positive.txt")


def run_human_negative():
    get_image_url(
        input_folder_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_human",
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "negative"],
        replace_remove="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_human/",
        replace_add="http://192.168.5.130/upload/Human/Human/",
        export_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/human_negative.txt")


def run_pet_positive():
    get_image_url(
        input_folder_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_pet",
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "posi"],
        replace_remove="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_pet/",
        replace_add="http://192.168.5.130/upload/Pet/Pet/",
        export_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/pet_positive.txt")


def run_pet_negative():
    get_image_url(
        input_folder_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_pet",
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "negative"],
        replace_remove="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_pet/",
        replace_add="http://192.168.5.130/upload/Pet/Pet/",
        export_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/pet_negative.txt")
def run_vehicle_positive():
    get_image_url(
        input_folder_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_vehicle",
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "positive"],
        replace_remove="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_vehicle/",
        replace_add="http://192.168.5.130/upload/Vehicle/",
        export_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/vehicle_positive.txt")

def run_vehicle_negative():
    get_image_url(
        input_folder_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_vehicle",
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "negative"],
        replace_remove="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/arnoo_test_vehicle/",
        replace_add="http://192.168.5.130/upload/Vehicle/",
        export_file_path="/mnt/c/Users/LDS/Desktop/workingspace/leedarson_workingspace/temp/arnoo_image_url/vehicle_negative.txt")

if __name__ == '__main__':
    run_package_positive()
    run_package_negative()
    run_human_positive()
    run_human_negative()
    run_pet_positive()
    run_pet_negative()
    run_vehicle_positive()
    run_vehicle_negative()
