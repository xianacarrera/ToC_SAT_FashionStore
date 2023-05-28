import unittest
import main

# Run with option -b to suppress output from main.py

class TestSolver(unittest.TestCase):

    def test_incompatible_garments(self):
        incompatible_garments = [["sandals", "socks"], ["skirt", "pants"], ["dress", "tshirt"], ["sandals", "shoes"]]
        for i, pair in enumerate(incompatible_garments):
            with open('tests/incompatible_garments.txt', 'w') as f:
                s1 = pair[0] + ', white\n'
                s2 = pair[1] + ', black\n'
                f.write(s1)
                f.write(s2)
                f.write('hat, black\n')
                if i != 0 and i != 3:
                    f.write('shoes, white\n')
                f.close()
            self.assertFalse(main.run("tests/incompatible_garments.txt"))     

    def test_shoes_or_sandals(self):
        with open('tests/shoes_or_sandals.txt', 'w') as f:
            f.write('tshirt, white\n')
            f.write('pants, black\n')
            f.write('hat, black\n')
            f.write('socks, white\n')
            f.close()
        self.assertFalse(main.run("tests/shoes_or_sandals.txt"))      

    def test_core_outfit(self):
        # Constraint: Either a dress or (a Tshirt and pants) or (a Tshirt and skirt)
        with open('tests/core_outfit.txt', 'w') as f:
            f.write('shoes, black\n')
            f.write('socks, white\n')
            f.close()
        self.assertFalse(main.run("tests/core_outfit.txt"))
        with open('tests/core_outfit.txt', 'w') as f:
            f.write('dress, black\n')
            f.write('hat, black\n')
            f.write('shoes, black\n')
            f.write('socks, white\n')
            f.close()
        self.assertTrue(main.run("tests/core_outfit.txt"))
        with open('tests/core_outfit.txt', 'w') as f:
            f.write('tshirt, black\n')
            f.write('pants, black\n')
            f.write('shoes, black\n')
            f.write('socks, white\n')
            f.close()
        self.assertTrue(main.run("tests/core_outfit.txt"))
        with open('tests/core_outfit.txt', 'w') as f:
            f.write('tshirt, black\n')
            f.write('skirt, black\n')
            f.write('shoes, black\n')
            f.write('socks, white\n')
            f.close()
        self.assertTrue(main.run("tests/core_outfit.txt"))
    
    def test_shoes_imply_socks(self):
        with open('tests/shoes_imply_socks.txt', 'w') as f:
            f.write('tshirt, white\n')
            f.write('pants, black\n')
            f.write('shoes, black\n')
            f.close()
        self.assertFalse(main.run("tests/shoes_imply_socks.txt"))    

    def test_dress_implies_hat(self):
        with open('tests/dress_implies_hat.txt', 'w') as f:
            f.write('dress, white\n')
            f.write('shoes, black\n')
            f.write('socks, black\n')
            f.close()
        self.assertFalse(main.run("tests/dress_implies_hat.txt"))    

    def def_incompatible_colors(self):
        incompatible_colors = [["blue", "green"], ["pink", "green"], ["green", "red"], ["blue", "red"], ["pink", "red"]]
        for pair in incompatible_colors:
            with open('tests/incompatible_colors.txt', 'w') as f:
                s1 = 'tshirt, ' + pair[0] + '\n'
                s2 = 'pants, ' + pair[1] + '\n'
                f.write(s1)
                f.write(s2)
                f.write('hat, black\n')
                f.write('socks, white\n')
                f.close()
            self.assertFalse(main.run("tests/incompatible_colors.txt"))

    def test_no_monocolor(self):
        with open('tests/no_monocolor.txt', 'w') as f:
            f.write('tshirt, red\n')
            f.write('pants, red\n')
            f.write('sandals, red\n')
            f.close()
        self.assertFalse(main.run("tests/no_monocolor.txt"))

    def test_at_most_three(self):
        with open('tests/at_most_three.txt', 'w') as f:
            f.write('tshirt, blue\n')
            f.write('pants, pink\n')
            f.write('sandals, black\n')
            f.write('hat, white\n')
            f.close()
        self.assertFalse(main.run("tests/at_most_three.txt"))

    def test_no_violet_hat_with_pink_dress(self):
        with open('tests/no_violet_hat_with_pink_dress.txt', 'w') as f:
            f.write('dress, pink\n')
            f.write('hat, violet\n')
            f.write('shoes, black\n')
            f.close()
        self.assertFalse(main.run("tests/no_violet_hat_with_pink_dress.txt"))

    def test_no_violet_dress_with_pink_hat(self):
        with open('tests/no_violet_dress_with_pink_hat.txt', 'w') as f:
            f.write('dress, violet\n')
            f.write('hat, pink\n')
            f.write('shoes, black\n')
            f.close()
        self.assertFalse(main.run("tests/no_violet_dress_with_pink_hat.txt"))


    def test_valid_outfits(self):
        with open('tests/valid_outfits.txt', 'w') as f:
            f.write('tshirt, white\n')
            f.write('hat, blue\n')
            f.write('pants, white\n')
            f.write('sandals, pink\n')
            f.close()
        self.assertTrue(main.run("tests/valid_outfits.txt"))
        with open('tests/valid_outfits.txt', 'w') as f:
            f.write('tshirt, white\n')
            f.write('pants, white\n')
            f.write('sandals, pink\n')
            f.close()
        self.assertTrue(main.run("tests/valid_outfits.txt"))
        with open('tests/valid_outfits.txt', 'w') as f:
            f.write('tshirt, white\n')
            f.write('skirt, pink\n')
            f.write('socks, pink\n')
            f.write('shoes, pink\n')
            f.close()
        self.assertTrue(main.run("tests/valid_outfits.txt"))


if __name__ == '__main__':
    unittest.main()