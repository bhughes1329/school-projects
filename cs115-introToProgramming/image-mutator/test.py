import unittest
import hw4

class TestHW4(unittest.TestCase):
    def assert_images_almost_equal(self, left_arr, right_arr, delta=2):
        flat_left = sum(left_arr, [])
        flat_right = sum(right_arr, [])
        self.assertEqual(len(flat_left), len(flat_right))
        list(map(lambda pair: self.assertAlmostEqual(pair[0], pair[1], delta=delta),
                 zip(flat_right, flat_right)))

    def test_rgb_to_grayscale_two_pixels(self):
        img = [
            [(255, 0, 0),],
            [(0, 0, 255),]
        ]
        expected = [
            [76],
            [29]
        ]
        hw4.rgb_to_grayscale(img)
        self.assert_images_almost_equal(img, expected)

    def test_rgb_to_grayscale_are_numbers_correct(self):
        img = [
            [(255, 0, 0), (0, 255, 0)],
            [(0, 0, 255), (255, 255, 255)]
        ]
        expected = [
            [76, 149],
            [29, 255]
        ]
        hw4.rgb_to_grayscale(img)
        self.assert_images_almost_equal(img, expected)

    def test_rgb_to_grayscale_in_correct(self):
        img = [
            [(0, 0, 0), (255, 255, 255)],
            [(30, 60, 90), (180, 200, 220)]
        ]
        hw4.rgb_to_grayscale(img)
        all_in_range = all(map(lambda v: 0 <= v <= 255, sum(img, [])))
        self.assertTrue(all_in_range, "All grayscale values should be in [0, 255]")

    def test_brightness_to_ascii_low_values(self):
        self.assertTrue(all(map(lambda v: hw4.brightness_to_ascii(v) == '@', [0, 10, 25])))

    def test_brightness_to_ascii_mid_values(self):
        values = [(40, '#'), (65, '%'), (100, '*')]
        self.assertTrue(all(map(lambda p: hw4.brightness_to_ascii(p[0]) == p[1], values)))

    def test_brightness_to_ascii_high_values(self):
        values = [(180, ':'), (220, '.'), (250, ' ')]
        self.assertTrue(all(map(lambda p: hw4.brightness_to_ascii(p[0]) == p[1], values)))

    def test_brightness_to_ascii_boundary_values(self):
        boundaries = [
            (25, '@'), (26, '#'),
            (51, '#'), (52, '%'),
            (76, '%'), (77, '*'),
            (102, '*'), (103, '='),
            (230, '.'), (231, ' ')
        ]
        self.assertTrue(all(map(lambda p: hw4.brightness_to_ascii(p[0]) == p[1], boundaries)))


    def test_image_to_ascii_string_all_dark_pixels(self):
        image = [[0, 0], [0, 0]]
        expected = "@@\r\n@@"
        self.assertEqual(hw4.image_to_ascii_string(image), expected)

    def test_image_to_ascii_string_gradient_pixels(self):
        image = [[0, 120], [255, 64]]
        # Assuming brightness_to_ascii is correct. In particular, that 
        # (0)='@', (64)='%', (120)='=', (255)=' '
        expected = "@=\r\n %"
        self.assertEqual(hw4.image_to_ascii_string(image), expected)

    def test_image_to_ascii_string_mixed_values(self):
        image = [[0], [125], [255]]
        expected = "@\r\n=\r\n "
        self.assertEqual(hw4.image_to_ascii_string(image), expected)

    def test_image_to_ascii_string_no_trailing_newline(self):
        image = [[0, 255], [255, 0]]
        expected = "@ \r\n @"
        self.assertEqual(hw4.image_to_ascii_string(image), expected)

    def test_image_to_ascii_string_large_mixed_image(self):
        image = [
            [0, 128, 255, 0],
            [255, 128, 0, 255],
            [128, 255, 0, 128]
        ]
        expected = "@+ @\r\n +@ \r\n+ @+"
        self.assertEqual(hw4.image_to_ascii_string(image), expected)

    def test_erase_simple_2x2(self):
        img = [[10, 200], [255, 50]]
        expected = [[0, 0], [0, 0]]
        hw4.erase(img)
        self.assertEqual(img, expected)

    def test_erase_3x3_contains_a_0(self):
        img = [
            [30, 60, 90],
            [120, 150, 0],
            [210, 0, 255]
        ]
        expected = [[0]*3]*3
        hw4.erase(img)
        self.assertEqual(img, expected)

    def test_lighten_simple_2x2(self):
        img = [[100, 50], [200, 0]]
        expected = [[min(int(100 * 1.3), 255),
                     min(int(50 * 1.3), 255)],
                    [min(int(200 * 1.3), 255),
                     min(int(0 * 1.3), 255)]]
        self.assert_images_almost_equal(img, expected)

    def test_lighten_maxes_at_255(self):
        img = [[230, 255], [250, 100]]
        expected = [[255, 255],
                    [255, min(int(100 * 1.3), 255)]]
        hw4.lighten(img)
        self.assert_images_almost_equal(img, expected)


    def test_darken_simple_2x2(self):
        img = [[100, 50], [200, 0]]
        expected = [[int(100 * 0.7), int(50 * 0.7)],
                    [int(200 * 0.7), int(0 * 0.7)]]
        hw4.darken(img)
        self.assert_images_almost_equal(img, expected)

    def test_darken_floor_at_zero(self):
        img = [[10, 0], [5, 2]]
        expected = [[max(int(10 * 0.7), 0),
                     max(int(0 * 0.7), 0)],
                    [max(int(5 * 0.7), 0),
                     max(int(2 * 0.7), 0)]]
        hw4.darken(img)
        self.assert_images_almost_equal(img, expected)

    def test_invert_boundaries(self):
        img = [[0, 255], [255, 0]]
        expected = [[255, 0], [0, 255]]
        hw4.invert(img)
        self.assertEqual(img, expected)

    def test_invert_midrange(self):
        img = [[100, 128], [200, 50]]
        expected = [[155, 127], [55, 205]]  # 255-i
        hw4.invert(img)
        self.assertEqual(img, expected)



if __name__ == "__main__":
    unittest.main()
