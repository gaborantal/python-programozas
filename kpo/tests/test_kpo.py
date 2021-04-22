from kpo import kpo
from io import StringIO
import mock
import unittest


class TestKoPapirOllo(unittest.TestCase):
    def setUp(self):
        self.game = kpo.KoPapirOllo("VALAMI")

    def test_nev(self):
        game = kpo.KoPapirOllo("KORTE")
        self.assertEqual(game.nev, "KORTE", "Egyszerű név teszt")
        game = kpo.KoPapirOllo("\t KORTE \t")
        self.assertEqual(game.nev, "KORTE", "Egyszerű név teszt")

    def test_init(self):
        self.assertEqual(self.game.nev, "VALAMI", "Nem megfelelő név")
        self.assertEqual(self.game.gyozelem, 0, "Nem megfelelő gyozelem")
        self.assertEqual(self.game.vereseg, 0, "Nem megfelelő vereseg")
        self.assertEqual(self.game.dontetlen, 0, "Nem megfelelő dontetlen")

    def test_gep_valaszt(self):
        self.assertIn(self.game.gep_valaszt(), ["ko", "papir", "ollo"])

    def test_felhasznalo_valasztasa_ko(self):
        with mock.patch("builtins.input") as mock_input:
            for test_ko in ["ko", "kő", "k", "K", "KŐ", "KO", "Kő", "kŐ", "kO"]:
                mock_input.return_value = test_ko
                self.assertEqual(self.game.jatekos_valaszt(), "ko", "Kő választás")

    @mock.patch("builtins.input")
    def test_felhasznalo_valasztasa_ollo(self, mock_input):
        for test_ollo in ["olló", "oLLó", "O"]:
            mock_input.return_value = test_ollo
            self.assertEqual(self.game.jatekos_valaszt(), "ollo", "Olló választás")

    @mock.patch("builtins.input", side_effect=["buzoganyKARDAKARMI!", "papir"])
    def test_felhasznalo_valasztasa_rossz_input(self, mock_input):
        valasztas = self.game.jatekos_valaszt()
        self.assertEqual(valasztas, "papir", "Papír választás")
        self.assertEqual(mock_input.call_count, 2, "Nem lett meghívva kétszer az input")

    def test_gep_valaszt_called(self):
        with mock.patch('random.choice') as mock_choice:
            gep_valasztasa = self.game.gep_valaszt()
            mock_choice.assert_called_once()

    @mock.patch("builtins.input")
    def test_jatszunk_meg_true(self, inp):
        inp.return_value = "igen"
        self.assertTrue(self.game.jatszunk_meg())
        self.assertIs(self.game.jatszunk_meg(), True)

    @mock.patch("builtins.input", return_value="nem")
    def test_jatszunk_meg_false(self, inp):
        inp.return_value = "nem"
        self.assertIs(self.game.jatszunk_meg(), False)
        inp.assert_called_once()

    @mock.patch("kpo.kpo.KoPapirOllo.jatekos_valaszt", return_value="ko")
    @mock.patch("kpo.kpo.KoPapirOllo.gep_valaszt", return_value="ko")
    def test_jatek_dontetlen(self, gep, jatekos):
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            self.game.jatek()
            self.assertIn("Döntetlen", fake_out.getvalue())

    def test_akarmi(self):
        # self.assertIs(self.game.akarmi(), False)
        self.assertIsNone(self.game.akarmi())

    def test_akarmi2(self):
        with mock.MagicMock() as mock_obj:
            self.game.akarmi2(mock_obj)
            mock_obj.__len__.assert_called_once()
            mock_obj.__str__.assert_called()
            mock_obj.gyakorlas.assert_called_once()


if __name__ == '__main__':
    unittest.main()
