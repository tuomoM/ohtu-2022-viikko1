import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    def test_lisaa_liikaa(self):
        self.varasto.lisaa_varastoon(10+self.varasto.paljonko_mahtuu())
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(),0)    

    def test_vie_tuhkatkin_pesasta(self):
        self.varasto.lisaa_varastoon(10)
        tuhkat =  self.varasto.ota_varastosta(100)
        self.assertAlmostEqual(tuhkat,10)

    def test_luo_uusi_milla_neg_saldo(self):
        self.varasto= Varasto(10,-10)
        self.assertAlmostEqual(self.varasto.saldo,0.0)

    def test_ota_negatiivinen(self):
        nolla = self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(nolla,0)
    
    def test_lisaa_negatiivinen(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.lisaa_varastoon(-10) # -10
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_luo_ylitsevuotava(self):
        self.varasto= Varasto(10,20)
        self.assertAlmostEqual(self.varasto.saldo,10)

    def test_luo_tyhjio(self):
        self.varasto= Varasto(-10)

    def test_tostring_oikein(self):
        oikea = "saldo = 0, vielä tilaa 10"
        self.assertEqual(oikea, str(self.varasto))    