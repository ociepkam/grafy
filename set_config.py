from sources.set_config import page_1, page_2, page_3


def run_page(page_n):
    if page_n == 1:
        return page_1.page_1()
    if page_n == 2:
        return page_2.page_2()
    if page_n == 3:
        return page_3.page_3()
    else:
        raise Exception("Wrong page number")


information = {1: None, 2: None, 3: None}
actual_page = 1
while True:
    information[actual_page] = run_page(actual_page)
    if information[actual_page] == "close":
        information = None
        break
    elif information[actual_page] == "go_back":
        information[actual_page] = None
        actual_page -= 1
    elif actual_page == 3:
        break
    elif information[actual_page] is not None:
        actual_page += 1
    else:
        information = None
        break

print(information)