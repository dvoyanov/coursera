from bs4 import BeautifulSoup
import unittest

def parse(path_to_file):
    with open(path_to_file, encoding='utf-8') as html:
        soup = BeautifulSoup(html, 'lxml')
        soup_body_content = soup.find('div', id='bodyContent')
        return [count_img(soup_body_content, 200), count_hx(soup_body_content, ('C', 'E', 'T')),
                max_sequence_links(soup_body_content), count_non_nested_lists(soup_body_content)]

def count_img(soup, width):
    imgs = soup.find_all('img')
    fit_imgs = len(
        [x for x in imgs if x.get('width') and int(x.get('width')) >= 200]
    )
    return fit_imgs

def count_hx(soup, first_letters):
    count = 0
    for hx in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        for find_hx in soup.find_all(hx):
            if find_hx.text[0] in first_letters:
                count += 1
    return count

def max_sequence_links(soup):
    max_count = 0
    all_links = soup.find_all('a')
    for link in all_links:
        current_count = 1
        siblings = link.find_next_siblings()
        for sibling in siblings:
            if sibling.name == 'a':
                current_count += 1
                max_count = max(current_count, max_count)
            else:
                current_count = 0
    return max_count

def count_non_nested_lists(soup):
    count = 0
    all_lists = soup.find_all(['ul', 'ol'])
    for tag in all_lists:
        if not tag.find_parents(['ul', 'ol']):
            count += 1
    return count

class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()