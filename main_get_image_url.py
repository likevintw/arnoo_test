
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


REMOVE_KEYWORDS = ["aws", "txt", "NG", "xlsx", "git"]


def run_package_positive():
    path = "../input/package"
    get_image_url(
        input_folder_path=path,
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "Positive"],
        replace_remove=path,
        replace_add="http://192.168.5.130/upload/Package/",
        export_file_path="../output/image_url/package_positive.txt")


def run_package_negative():
    path = "../input/package"
    get_image_url(
        input_folder_path=path,
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "Negative"],
        replace_remove=path,
        replace_add="http://192.168.5.130/upload/Package/",
        export_file_path="../output/image_url/package_negative.txt")


def run_human_positive():
    path = "../input/human"
    get_image_url(
        input_folder_path=path,
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "positive"],
        replace_remove=path,
        replace_add="http://192.168.5.130/upload/Human/Human/",
        export_file_path="../output/image_url/human_positive.txt")


def run_human_negative():
    path = "../input/human"
    get_image_url(
        input_folder_path=path,
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "negative"],
        replace_remove=path,
        replace_add="http://192.168.5.130/upload/Human/Human/",
        export_file_path="../output/image_url/human_negative.txt")


def run_pet_positive():
    path = "../input/pet"
    get_image_url(
        input_folder_path=path,
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "posi"],
        replace_remove=path,
        replace_add="http://192.168.5.130/upload/Pet/Pet/",
        export_file_path="../output/image_url/pet_positive.txt")


def run_pet_negative():
    path = "../input/pet"
    get_image_url(
        input_folder_path=path,
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "negative"],
        replace_remove=path,
        replace_add="http://192.168.5.130/upload/Pet/Pet/",
        export_file_path="../output/image_url/pet_negative.txt")


def run_vehicle_positive():
    path = "../input/vehicle"
    get_image_url(
        input_folder_path=path,
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "positive"],
        replace_remove=path,
        replace_add="http://192.168.5.130/upload/Vehicle/",
        export_file_path="../output/image_url/vehicle_positive.txt")


def run_vehicle_negative():
    path = "../input/vehicle"
    get_image_url(
        input_folder_path=path,
        path_remoeve_keywords=REMOVE_KEYWORDS,
        path_keep_keywords=["jpg", "negative"],
        replace_remove=path,
        replace_add="http://192.168.5.130/upload/Vehicle/",
        export_file_path="../output/image_url/vehicle_negative.txt")


if __name__ == '__main__':
    run_human_positive()
    run_human_negative()
    run_pet_positive()
    run_pet_negative()
    run_vehicle_positive()
    run_vehicle_negative()
    run_package_positive()
    run_package_negative()
