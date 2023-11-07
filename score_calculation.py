class Katsayilar:
    # TYT
    TR_KATSAYI = 3.3
    SOS_KATSAYI = 3.4
    MAT1_KATSAYI = 3.3
    FEN_KATSAYI = 3.4

    # ESIT AGIRLIK
    EDB_KATSAYI = 3
    TARIH1_KATSAYI = 2.802
    COG1_KATSAYI = 3.33

    # SOZEL
    TARIH2_KATSAYI = 2.91
    COG2_KATSAYI = 2.91
    FELSEFE_KATSAYI = 3
    DINKLTR_KATSAYI = 3.33

    # SAYISAL
    MAT2_KATSAYI = 3
    FIZIK_KATSAYI = 2.87
    KIMYA_KATSAYI = 3.07
    BIYO_KATSAYI = 3.07

    # AYT PUANLARI ICIN KULLANILACAK TYT KATSAYILARI
    TYT_TRKATSAYI = 1.32
    TYT_SOSKATSAYI = 1.36
    TYT_MAT1KATSAYI = 1.32
    TYT_FENKATSAYI = 1.36


class PuanHesaplari(Katsayilar):
    OSYM_TABANPUAN = 100

    def __init__(self, obp, tr_net, sosyal_net, mat1_net, fen_net, mat2_net, fizik_net, kimya_net, biyo_net,
                 edb_net, tarih1_net, cog1_net, tarih2_net, cog2_net, felsefe_net, din_net, dil_net):
        self.BASARI_PUANI = obp
        self.tr_net = tr_net
        self.sosyal_net = sosyal_net
        self.mat1_net = mat1_net
        self.fen_net = fen_net
        self.mat2_net = mat2_net
        self.fizik_net = fizik_net
        self.kimya_net = kimya_net
        self.biyo_net = biyo_net
        self.edb_net = edb_net
        self.tarih1_net = tarih1_net
        self.cog1_net = cog1_net
        self.tarih2_net = tarih2_net
        self.cog2_net = cog2_net
        self.felsefe_net = felsefe_net
        self.din_net = din_net
        self.dil_net = dil_net

    def validate_inputs(self):
        if not (0 <= self.tr_net <= 40 and 0 <= self.sosyal_net <= 20 and 0 <= self.mat1_net <= 40 and 0 <= self.fen_net <= 40):
            raise ValueError("TYT bölümündeki netler hatalı.")
        if not (0 <= self.mat2_net <= 40 and 0 <= self.fizik_net <= 14 and 0 <= self.kimya_net <= 13 and 0 <= self.biyo_net <= 13):
            raise ValueError("SAY bölümündeki netler hatalı.")
        if not (0 <= self.edb_net <= 20 and 0 <= self.tarih1_net <= 10 and 0 <= self.cog1_net <= 6):
            raise ValueError("EA bölümündeki netler hatalı.")
        if not (0 <= self.tarih2_net <= 11 and 0 <= self.cog2_net <= 11 and 0 <= self.felsefe_net <= 12 and 0 <= self.din_net <= 6):
            raise ValueError("SOZ bölümündeki netler hatalı.")
        if not (0 <= self.dil_net <= 80):
            raise ValueError("DİL bölümündeki netler hatalı.")

    def tyt_puan_hesapla(self):
        tyt_puan = (self.tr_net * self.TR_KATSAYI + self.sosyal_net * self.SOS_KATSAYI +
                    self.mat1_net * self.MAT1_KATSAYI + self.fen_net * self.FEN_KATSAYI)
        tyt_ham_puan_sonucu = tyt_puan + self.OSYM_TABANPUAN
        tyt_yer_puan_sonucu = tyt_puan + self.OSYM_TABANPUAN + self.BASARI_PUANI
        return tyt_ham_puan_sonucu, tyt_yer_puan_sonucu

    def tyt_puani_al(self):
        return (self.tr_net * self.TYT_TRKATSAYI + self.sosyal_net * self.TYT_SOSKATSAYI +
                self.mat1_net * self.TYT_MAT1KATSAYI + self.fen_net * self.TYT_FENKATSAYI)

    def say_puan_hesapla(self):
        say_puan = (self.mat2_net * self.MAT2_KATSAYI + self.fizik_net * self.FIZIK_KATSAYI +
                    self.kimya_net * self.KIMYA_KATSAYI + self.biyo_net * self.BIYO_KATSAYI)
        say_ham_puan_sonucu = say_puan + self.tyt_puani_al() + self.OSYM_TABANPUAN
        say_yer_puan_sonucu = say_puan + self.tyt_puani_al() + self.OSYM_TABANPUAN + self.BASARI_PUANI
        return say_ham_puan_sonucu, say_yer_puan_sonucu

    def e_agirlik_puan_hesapla(self):
        e_agirlik_puan = (self.mat2_net * self.MAT2_KATSAYI + self.edb_net * self.EDB_KATSAYI +
                          self.tarih1_net * self.TARIH1_KATSAYI + self.cog1_net * self.COG1_KATSAYI)
        e_agirlik_puan_sonucu = e_agirlik_puan + self.tyt_puani_al() + self.OSYM_TABANPUAN
        e_agirlik_yer_puan_sonucu = e_agirlik_puan + self.tyt_puani_al() + self.OSYM_TABANPUAN + self.BASARI_PUANI
        return e_agirlik_puan_sonucu, e_agirlik_yer_puan_sonucu

    def sozel_puan_hesapla(self):
        e_a = self.edb_net * self.EDB_KATSAYI + self.tarih1_net * self.TARIH1_KATSAYI + self.cog1_net * self.COG1_KATSAYI
        sozel_puan = (e_a + self.tarih2_net * self.TARIH2_KATSAYI + self.cog2_net * self.COG2_KATSAYI +
                      self.felsefe_net * self.FELSEFE_KATSAYI + self.din_net * self.DINKLTR_KATSAYI)
        sozel_ham_puan_sonucu = sozel_puan + self.tyt_puani_al() + self.OSYM_TABANPUAN
        sozel_yer_puan_sonucu = sozel_puan + self.tyt_puani_al() + self.OSYM_TABANPUAN + self.BASARI_PUANI
        return sozel_ham_puan_sonucu, sozel_yer_puan_sonucu

    def dil_puan_hesapla(self):
        dil_puan = self.dil_net * 3
        if self.dil_net > 0:
            dil_ham_puan_sonucu = dil_puan + self.tyt_puani_al() + self.OSYM_TABANPUAN
            dil_yer_puan_sonucu = dil_puan + self.tyt_puani_al() + self.OSYM_TABANPUAN + self.BASARI_PUANI
            return dil_ham_puan_sonucu, dil_yer_puan_sonucu
        else:
            return None, None