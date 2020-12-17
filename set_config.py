from sources.set_config import page_1, page_2, page_3
from sources.load_data import load_config
import yaml


def run_page(page_n, info=None):
    if page_n == 1:
        return page_1.page_1(info)
    if page_n == 2:
        return page_2.page_2(info)
    if page_n == 3:
        return page_3.page_3(info)
    else:
        raise Exception("Wrong page number")


def create_new_config(info, config_name="config.yaml"):
    f = open(config_name, 'w+')
    yaml.safe_dump(info, f, allow_unicode=True, sort_keys=False)


if __name__ == "__main__":
    information = {1: None, 2: None, 3: None}
    actual_page = 1
    try:
        info = load_config("test_config.yaml")
    except:
        info = {1: None, 2: None, 3: None}
    while True:
        try:
            info[actual_page]
        except KeyError:
            info[actual_page] = None
        information[actual_page] = run_page(actual_page, info[actual_page])
        if information[actual_page] == "close":
            exit()
        elif information[actual_page] == "go_back":
            information[actual_page] = None
            actual_page -= 1
        elif actual_page == 3:
            break
        elif information[actual_page] is not None:
            actual_page += 1
        else:
            exit()

    # information = {**information[1], **information[2], **information[3]}
    create_new_config(information, "test_config.yaml")
