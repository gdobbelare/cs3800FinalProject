import multiprocessing
import time

import requests

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://github.com/gdobbelare/cs3800FinalProject",
        "https://ostechnix.com/unixbench-benchmark-suite-unix-like-systems/",
    ] * 80
    startTime = time.time()
    download_all_sites(sites)
    print("----%s seconds ---" % (time.time() - startTime))