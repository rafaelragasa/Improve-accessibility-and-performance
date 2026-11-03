from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"


def test_document_has_language_and_title():
    soup = BeautifulSoup(HTML.read_text(encoding="utf-8"), "html.parser")

    assert soup.html is not None
    assert soup.html.get("lang") == "en"
    assert soup.title is not None
    assert soup.title.string.strip() == "Web Systems and Technologies - Weeks 16-17 Laboratory"


def test_images_have_alt_text_and_main_landmarks():
    soup = BeautifulSoup(HTML.read_text(encoding="utf-8"), "html.parser")

    images = soup.find_all("img")
    assert len(images) >= 2
    for image in images:
        assert image.get("alt")

    assert soup.find("main") is not None
    assert soup.find("h1") is not None
    headings = [tag.name for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])]
    assert headings

    button = soup.find("button")
    assert button is not None
    assert button.get_text(strip=True)


def test_controls_avoid_fake_div_buttons():
    soup = BeautifulSoup(HTML.read_text(encoding="utf-8"), "html.parser")
    assert soup.find("button") is not None
    assert soup.find("div", class_="fake-button") is None
