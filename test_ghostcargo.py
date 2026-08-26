
from ghostcargo import (
    open_image,
    get_pixel,
    convert_pixel_to_binary,
    replace_lsb,
    binary_to_decimal
)

from PIL import Image


def test_open_image(tmp_path):
    test_image_path = tmp_path / "test.png"

    image = Image.new("RGB", (2, 2), (10, 20, 30))
    image.save(test_image_path)

    result = open_image(test_image_path)

    assert result.size == (2, 2)
    assert result.mode == "RGB"


def test_get_pixel():
    image = Image.new("RGB", (2, 2), (10, 20, 30))

    result = get_pixel(0, 0, image)

    assert result == (10, 20, 30)


def test_convert_pixel_to_binary():
    pixel = (3, 19, 255)

    result = convert_pixel_to_binary(pixel)

    assert result == [
        "00000011",
        "00010011",
        "11111111"
    ]


def test_replace_lsb():
    result = replace_lsb("00000011", "0")

    assert result == "00000010"


def test_binary_to_decimal():
    result = binary_to_decimal("00010010")
    assert result == 18