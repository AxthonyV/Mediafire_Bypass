import hashlib as h, requests as r, gazpacho as g, re as e, argparse as ap, os, time as tm, threading as th, colorama as c

c.init(autoreset=True)

class O:
    P, S, V, L, Y, R, B, U = c.Fore.MAGENTA, c.Style.RESET_ALL, c.Fore.LIGHTMAGENTA_EX, c.Fore.LIGHTGREEN_EX, c.Fore.YELLOW, c.Fore.LIGHTRED_EX, c.Style.BRIGHT, c.Style.BRIGHT + c.Fore.BLACK + c.Back.WHITE

A = r"""
⠤⠤⠤⠤⠤⠤⢤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠤⠶⠶⠶⠦⠤⠤⠤⠤⠤⢤⣤⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠄⢂⣠⣭⣭⣕⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠤⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉
⠀⠀⢀⠜⣳⣾⡿⠛⣿⣿⣿⣦⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣍⣀⣦⠦⠄⣀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⣄⣽⣿⠋⠀⡰⢿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠛⠛⡿⠿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣁⣂⣤⡄⠀⠀⠀⠀⠀⠀
⢳⣶⣼⣿⠃⠀⢀⠧⠤⢜⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⡇⠀⣀⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠁⠐⠀⣀⠀⠀
⠀⠙⠻⣿⠀⠀⠀⠀⠀⠀⢹⣿⣿⡝⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠋⠀⠀⠀⠀⠠⠃⠁⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⡿⠋⠀⠀
⠀⠀⠀⠙⡄⠀⠀⠀⠀⠀⢸⣿⣿⡃⢼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⡏⠉⠉⠻⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠀⠀⠰⡒⠊⠻⠿⠋⠐⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣇⡀⠀⠑⢄⠀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢖⠠⠤⠤⠔⠙⠻⠿⠋⠱⡑⢄⠀⢠⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠒⠒⠻⠶⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠡⢀⡵⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠦⣀⠀⠀⠀⠀⠀⢀⣤⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠙⠛⠓⠒⠲⠿⢍⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

U = "-_. "
CR = "-"

def hf(fn: str):
    hasher = h.sha256()
    with open(fn, "rb") as f:
        for chunk in iter(lambda: f.read(1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def n(fn: str):
    return "".join([
        char if (char.isalnum() or char in U) else
        CR
        for char in fn])

def sa():
    print(O.V + A + O.S)

def si(fn, st):
    print(
        f"{O.L}Downloading {O.B}{fn}{O.S} - {st}"
    )

def d(fi: dict, event: th.Event = None, limiter: th.BoundedSemaphore = None):
    if limiter:
        limiter.acquire()
    if event and event.is_set():
        limiter.release()
        return

    fl = fi["links"]["normal_download"]

    try:
        hc = g.get(fl)
    except r.exceptions.RequestException:
        si(fi["filename"], f"{O.R}Failed to download{O.S}")
        limiter.release()
        return

    hs = g.Soup(hc)
    try:
        dl = (
            hs.find("div", {"class": "download_link"})
            .find("a", {"class": "input popsok"})
            .attrs["href"]
        )
    except Exception:
        si(fi["filename"], f"{O.R}Failed to retrieve download link{O.S}")
        if limiter:
            limiter.release()
        return

    file_name = n(fi["filename"])

    if os.path.exists(file_name) and hf(file_name) == fi["hash"]:
        si(file_name, f"{O.Y}Already downloaded, skipping{O.S}")
        if limiter:
            limiter.release()
        return
    elif os.path.exists(file_name):
        si(file_name, f"{O.Y}Already exists but corrupted, redownloading{O.S}")

    si(file_name, f"{O.V}Starting download{O.S}")

    if event and event.is_set():
        limiter.release()
        return

    try:
        with r.get(dl, stream=True) as response:
            response.raise_for_status()
            with open(file_name, "wb") as file:
                for chunk in response.iter_content(chunk_size=4096):
                    if event and event.is_set():
                        break
                    if chunk:
                        file.write(chunk)

    except r.exceptions.RequestException:
        si(file_name, f"{O.R}Failed to download{O.S}")
        os.remove(file_name)
        limiter.release()
        return

    if event and event.is_set():
        os.remove(file_name)
        print(
            f"{O.Y}Deleted partially downloaded {O.B}{file_name}{O.S}"
        )
        limiter.release()
        return

    si(file_name, f"{O.L}Downloaded successfully{O.S}")
    if limiter:
        limiter.release()

def ff(f_key, f_name, n_threads, first=False):
    if first:
        f_name = os.path.join(
            f_name,
            n(r.get(
                ge("folder", f_key, info=True)
            ).json()["response"]["folder_info"]["name"]),
        )

    if not os.path.exists(f_name):
        os.makedirs(f_name)
    os.chdir(f_name)

    df(f_key, n_threads)

    f_content = r.get(
        ge("folders", f_key)
    ).json()["response"]["folder_content"]

    if "folders" in f_content:
        for folder in f_content["folders"]:
            ff(folder["folderkey"], folder["name"], n_threads)
            os.chdir("..")

def ge(f_or_f, f_key, chunk=1, info=False):
    return (
        f"https://www.mediafire.com/api/1.4/folder"
        f"/{'get_info' if info else 'get_content'}.php?r=utga&content_type={f_or_f}"
        f"&filter=all&order_by=name&order_direction=asc&chunk={chunk}"
        f"&version=1.5&folder_key={f_key}&response_format=json"
    )

def gie(f_key: str):
    return f"https://www.mediafire.com/api/file/get_info.php?quick_key={f_key}&response_format=json"

def df(f_key, n_threads):
    data = []
    chunk = 1
    more_chunks = True

    try:
        while more_chunks:
            response_json = r.get(
                ge("files", f_key, chunk=chunk)
            ).json()
            more_chunks = response_json["response"]["folder_content"]["more_chunks"] == "yes"
            data += response_json["response"]["folder_content"]["files"]
            chunk += 1

    except KeyError:
        print("Invalid link")
        return

    event = th.Event()

    thread_limiter = th.BoundedSemaphore(n_threads)

    all_threads = []

    for file in data:
        all_threads.append(
            th.Thread(
                target=d,
                args=(
                    file,
                    event,
                    thread_limiter,
                ),
            )
        )

    for thread in all_threads:
        thread.start()

    try:
        while True:
            if all(not t.is_alive() for t in all_threads):
                break
            tm.sleep(0.01)
    except KeyboardInterrupt:
        print(f"{O.Y}Closing all threads{O.S}")
        event.set()
        for thread in all_threads:
            thread.join()
        print(f"{O.Y}{O.B}Download interrupted{O.S}")
        exit(0)

    f_info = r.get(
        ge("folder", f_key, info=True)
    ).json()["response"]["folder_info"]
    f_name = n(f_info["name"])
    n_files = f_info["file_count"]
    si(f_name, f"{O.V}({n_files}){O.S}")

def gf(f_key: str, o_path: str = None):
    f_data = r.get(gie(f_key)).json()["response"]["file_info"]
    if o_path:
        os.chdir(o_path)
    d(f_data)

def main():
    sa()

    parser = ap.ArgumentParser(
        "MediaFire_MDownloader", usage="python mediafire.py <mediafire_url>"
    )
    parser.add_argument(
        "mediafire_url", help="The url of the file or folder to be downloaded"
    )
    parser.add_argument(
        "-o",
        "--output",
        help="The path of the desired output folder",
        required=False,
        default=".",
    )
    parser.add_argument(
        "-t",
        "--threads",
        help="Number of threads to use",
        type=int,
        default=10,
        required=False,
    )

    args = parser.parse_args()

    folder_or_file = e.findall(
        r"mediafire\.com/(folder|file)\/([a-zA-Z0-9]+)", args.mediafire_url
    )

    if not folder_or_file:
        print(f"{O.R}Invalid link{O.S}")
        exit(1)

    f_type, f_key = folder_or_file[0]

    if f_type == "file":
        gf(f_key, args.output)
    elif f_type == "folder":
        ff(f_key, args.output, args.threads, first=True)
    else:
        print(f"{O.R}Invalid link{O.S}")
        exit(1)

    print(f"{O.L}{O.B}All downloads completed{O.S}")
    exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
