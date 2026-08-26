import ghostcargo

from PIL import Image


def test_open_image(tmp_path):
    test_image_path = tmp_path / "test.png"

    image = Image.new("RGB", (2, 2), (10, 20, 30))
    image.save(test_image_path)

    result = ghostcargo.open_image(test_image_path)

    assert result.size == (2, 2)
    assert result.mode == "RGB"


def test_get_pixel():
    image = Image.new("RGB", (2, 2), (10, 20, 30))

    result = ghostcargo.get_pixel(0, 0, image)

    assert result == (10, 20, 30)


def test_convert_pixel_to_binary():
    pixel = (3, 19, 255)

    result = ghostcargo.convert_pixel_to_binary(pixel)

    assert result == [
        "00000011",
        "00010011",
        "11111111"
    ]


def test_replace_lsb():
    result = ghostcargo.replace_lsb("00000011", "0")

    assert result == "00000010"


def test_binary_to_decimal():
    result = ghostcargo.binary_to_decimal("00010010")
    assert result == 18

def test_text_to_binary():
    result = ghostcargo.text_to_binary("A")
    assert result == "01000001"


def test_hide_message():
    image = Image.new("RGB", (20, 20), (100, 100, 100))

    result = ghostcargo.hide_message(image, "A")

    assert result is not None

    first_pixel = result.getpixel((0, 0))

    assert first_pixel == (100, 101, 100)