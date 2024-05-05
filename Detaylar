import sys: sys modülü, Python yürütücüsüne ve çevresel değişkenlere erişmek için kullanılır.
from PyQt5.QtWidgets import (...): PyQt5 modülünden bazı widget ve diğer öğeleri içeri aktarır. Bunlar arasında QApplication, 
QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, ve QCheckBox bulunur.
from PyQt5.QtGui import QColor: Bu satır, QColor sınıfını içeri aktarır. QColor, renkleri temsil etmek için PyQt5'in grafik arayüz 
modülünde kullanılır.
from PyQt5.QtCore import Qt: Bu satır, PyQt5'in QtCore modülünden Qt öğelerini içeri aktarır. Qt, PyQt5 içinde temel Qt işlevlerine 
erişim sağlar.
---------------------------------------------------
class MessageBox(QMessageBox):
QMessageBox sınıfını temel alan MessageBox adında bir alt sınıf oluşturur.
MessageBox, PyQt5'te mesaj kutularını özelleştirmek için kullanılır.
class MainWindow(QMainWindow):
QMainWindow sınıfını temel alan MainWindow adında bir sınıf oluşturur.
Bu sınıf, uygulamanın ana penceresini oluşturur ve uygulamanın temel işlevlerini yönetir.
Uygulamanın ana ekranını ve tüm arayüz öğelerini burada oluşturur.
Favori oyunlar, koleksiyon ve diğer değişkenler bu sınıf içinde tanımlanır.
def initializeUI(self):
UI'nin (kullanıcı arayüzü) başlatılmasını sağlayan bir yöntemdir.
Ana pencerenin boyutunu, başlığını ve arka plan rengini ayarlar.
Arayüz öğelerini (etiketler, metin girişleri, düğmeler ve listeler) oluşturur ve yerleştirir.
def update_stars(self):
Yıldız sayısını güncelleyen bir yöntemdir.
Kullanıcının seçtiği yıldız sayısını hesaplar.
def add_game(self):
Yeni bir oyun eklemek için kullanılan bir yöntemdir.
Kullanıcının girdiği oyun bilgilerini alır ve koleksiyona ekler.
def add_favorite_game(self):
Favori oyunları eklemek için kullanılan bir yöntemdir.
Kullanıcının koleksiyonda seçtiği bir oyunu favorilere ekler.
def remove_game(self):
Bir oyunu koleksiyondan kaldırmak için kullanılan bir yöntemdir.
Kullanıcının koleksiyonda seçtiği bir oyunu koleksiyondan kaldırır.
def remove_favorite_game(self):
Favori bir oyunu kaldırmak için kullanılan bir yöntemdir.
Kullanıcının favorilerinde seçtiği bir oyunu favorilerden kaldırır.
def search_game(self):
Bir oyunu aramak için kullanılan bir yöntemdir.
Kullanıcının girdiği oyun adını koleksiyonda arar ve sonucu bildirir.
def update_collection_list(self):
Koleksiyon listesini güncelleyen bir yöntemdir.
Koleksiyondaki oyunları listeye ekler.
def update_favorite_games_list(self):
Favori oyunlar listesini güncelleyen bir yöntemdir.
Favori oyunları listeye ekler.
def clear_game_inputs(self):
Oyun giriş alanlarını temizleyen bir yöntemdir.
Kullanıcı girişlerini temizler.
if name == 'main':
Bu koşul, bu betiğin doğrudan çalıştırıldığını belirler.
Uygulamanın ana döngüsünü başlatır.
------------------------------------------------
Başlangıçta temel bir kullanıcı arayüzü oluşturduk.
Kullanıcının oyunları ekleyebileceği, favorilere ekleyebileceği,
koleksiyondan çıkarabileceği ve oyunları arayabileceği işlevler ekledik.
Oyunları ve favori oyunları listelemek için QListWidget kullanıldı.
Oyunları eklemek, favorilere eklemek ve koleksiyondan çıkarmak için butonlar eklendi.
Favorilere ekleme ve koleksiyondan çıkarma işlemleri için hata kontrolü eklendi.
Oyun arama işlevi eklendi.
Oyunların derecesini belirtmek için yıldız özelliği eklendi.
Renkler ve stil ayarları yapıldı.
Kullanıcı bilgileri ve oyun bilgileri giriş alanları düzenlendi.
Butonların düzeni ve görünümü ayarlandı.
İşlem sonucunda kullanıcıya geri bildirim sağlandı.
Bilgilendirme ve uyarı mesajları eklendi.
Oyun Ekleme
Yeni bir oyun ekleyerek koleksiyonunuzu genişletebilirsiniz.
Favorilere Ekleme
Favori oyunlarınızı seçerek onları favorilere ekleyebilirsiniz.
Koleksiyondan Çıkarma
Koleksiyondaki oyunları seçerek onları koleksiyondan çıkarabilirsiniz.
Favorilerden Çıkarma
Favorilerdeki oyunları seçerek onları favorilerden çıkarabilirsiniz.
Oyun Arama
Oyun adını girerek oyunlar arasında arama yapabilirsiniz.
