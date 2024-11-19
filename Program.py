import tkinter as tk
from tkinter import ttk, messagebox
import json

class DersTakipUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Ders Takip Uygulaması")
        self.ders_durumlari = self.load_ders_durumlari()

        self.create_widgets()

    def load_ders_durumlari(self):
        try:
            with open("ders_durumlari.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "Diferansiyel Denklemler": [False, False, False, False, False, False, False, False, False, False, False, False, False, False],
                "Mekanik Titreşim": [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
            }

    def save_ders_durumlari(self):
        with open("ders_durumlari.json", "w") as f:
            json.dump(self.ders_durumlari, f)

    def create_widgets(self):
        # Ana ekranı oluşturma
        self.clear_frame()
        self.giris_frame = tk.Frame(self.root)
        self.giris_frame.pack(pady=20)

        self.giris_label = tk.Label(self.giris_frame, text="Ders Takip Uygulaması'na Hoş Geldiniz!", font=("Helvetica", 16))
        self.giris_label.pack(pady=10)

        self.ders_goster_button = tk.Button(self.giris_frame, text="Derslerin Yüzde Kaç Bittiğini Göster", command=self.show_ders_durumlari, width=30, height=2)
        self.ders_goster_button.pack(pady=10)

        self.ders_guncelle_button = tk.Button(self.giris_frame, text="Ders Durumlarını Güncelle", command=self.guncelleme_ekrani, width=30, height=2)
        self.ders_guncelle_button.pack(pady=10)

    def show_ders_durumlari(self):
        # Ders Durumlarını Gösterme Ekranı
        self.clear_frame()
        self.durum_frame = tk.Frame(self.root)
        self.durum_frame.pack(pady=20)

        self.durum_label = tk.Label(self.durum_frame, text="Derslerin Tamamlanma Durumları", font=("Helvetica", 16))
        self.durum_label.pack(pady=10)

        for ders, durumlar in self.ders_durumlari.items():
            tamamlanan = sum(durumlar)
            toplam = len(durumlar)
            yuzde = (tamamlanan / toplam) * 100
            durum_text = f"{ders}: % {yuzde:.2f} tamamlandı"
            tk.Label(self.durum_frame, text=durum_text).pack()

        self.geri_button = tk.Button(self.durum_frame, text="Geri Dön", command=self.create_widgets)
        self.geri_button.pack(pady=10)

    def guncelleme_ekrani(self):
        # Güncelleme Ekranı
        self.clear_frame()
        self.guncelleme_frame = tk.Frame(self.root)
        self.guncelleme_frame.pack(pady=20)

        self.guncelleme_label = tk.Label(self.guncelleme_frame, text="Ders Durumlarını Güncelle", font=("Helvetica", 16))
        self.guncelleme_label.pack(pady=10)

        self.ders_var = tk.StringVar()
        self.ders_secimi = ttk.Combobox(self.guncelleme_frame, textvariable=self.ders_var)
        self.ders_secimi['values'] = list(self.ders_durumlari.keys())
        self.ders_secimi.pack(pady=10)

        self.hafta_var = tk.StringVar()
        self.hafta_secimi = ttk.Combobox(self.guncelleme_frame, textvariable=self.hafta_var)
        self.hafta_secimi['values'] = [f"Hafta {i+1}" for i in range(14)]
        self.hafta_secimi.pack(pady=10)

        self.bitti_button = tk.Button(self.guncelleme_frame, text="Bitti Olarak İşaretle", command=self.isaretle, width=30, height=2)
        self.bitti_button.pack(pady=10)

        self.geri_button = tk.Button(self.guncelleme_frame, text="Geri Dön", command=self.create_widgets)
        self.geri_button.pack(pady=10)

    def isaretle(self):
        ders = self.ders_var.get()
        hafta = self.hafta_var.get()
        if ders and hafta:
            hafta_index = int(hafta.split()[1]) - 1
            self.ders_durumlari[ders][hafta_index] = True
            self.save_ders_durumlari()
            messagebox.showinfo("Başarılı", f"{ders} - {hafta} bitti olarak işaretlendi.")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DersTakipUygulamasi(root)
    root.mainloop()
