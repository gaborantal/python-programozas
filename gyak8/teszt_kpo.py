import kpo
from io import StringIO
import mock
import unittest


class TestKoPapirOllo(unittest.TestCase):
    def setUp(self):
        self.game = kpo.KoPapirOllo("VALAMI")

    def test_init(self):
        self.assertEqual(self.game.nev, "VALAMI", "Nem megfelelő név")
        self.assertEqual(self.game.gyozelem, 0, "Nem megfelelő gyozelem")
        self.assertEqual(self.game.vereseg, 0, "Nem megfelelő vereseg")
        self.assertEqual(self.game.dontetlen, 0, "Nem megfelelő dontetlen")

    def test_gep_valaszt(self):
        self.assertIn(self.game.gep_valaszt(), ["ko", "papir", "ollo"])

    def test_gep_valaszt_called(self):
        with mock.patch('random.choice') as mock_choice:
            gep_valasztasa = self.game.gep_valaszt()
            mock_choice.assert_called_once()

    @mock.patch("builtins.input")
    def test_jatszunk_meg_true(self, inp):
        inp.return_value = "igen"
        self.assertIs(self.game.jatszunk_meg(), True)

    @mock.patch("builtins.input", return_value="nem")
    def test_jatszunk_meg_false(self, inp):
        inp.return_value = "nem"
        self.assertIs(self.game.jatszunk_meg(), False)
        inp.assert_called_once()

    @mock.patch("kpo.KoPapirOllo.jatekos_valaszt", return_value="ko")
    @mock.patch("kpo.KoPapirOllo.gep_valaszt", return_value="ko")
    def test_jatek_dontetlen(self, gep, jatekos):
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            self.game.jatek()
            self.assertIn("Döntetlen", fake_out.getvalue())

    def test_akarmi(self):
        self.assertFalse(self.game.akarmi())
        self.assertIs(self.game.akarmi(), False)

    def test_akarmi2(self):
        with mock.MagicMock() as mock_obj:
            self.game.akarmi2(mock_obj)
            mock_obj.__len__.assert_called_once()
            mock_obj.__str__.assert_called()


if __name__ == '__main__':
    unittest.main()
