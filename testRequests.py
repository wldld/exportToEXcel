import requests

if __name__ == '__main__':
    url = 'http://reader.epubee.com/books/8b/8b7037aa18a4fb15c09bf7ea91d2b120.epub'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    response = requests.get(url, stream=True, headers=headers)
    print(response.headers['content-length'])
    with open("E:\\temp\\8b7037aa18a4fb15c09bf7ea91d2b120.epub", "ab") as f:
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
                f.flush()
