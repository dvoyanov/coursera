from bs4 import BeautifulSoup
import os


def get_href_page_names(page_name, wiki_path):
    try:
        with open(os.path.join(wiki_path, page_name)) as file:
            html = file.read()
            soup = BeautifulSoup(html, 'html.parser')
            raw_a = soup.find_all('a', href=True)
            pages_names = [
                x['href'].split('/')[-1]
                for x in raw_a
                if x['href'].startswith('/wiki')
            ]
            return pages_names
    except FileNotFoundError:
        return []


def bfs_paths(start, goal, wiki_path):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(get_href_page_names(vertex, wiki_path)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(start, goal, wiki_path):
    try:
        return next(bfs_paths(start, goal, wiki_path))
    except StopIteration:
        return None

