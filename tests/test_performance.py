from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"


def test_script_is_deferred_and_images_have_dimensions():
    soup = BeautifulSoup(HTML.read_text(encoding="utf-8"), "html.parser")

    script = soup.find("script")
    assert script is not None
    assert script.get("defer") is not None

    for image in soup.find_all("img"):
        assert image.get("width") is not None
        assert image.get("height") is not None

    lazy_image = soup.find("img", loading="lazy")
    assert lazy_image is not None
