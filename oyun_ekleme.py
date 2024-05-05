import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QCheckBox
)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class MessageBox(QMessageBox):
    def __init__(self, parent=None):
        super(MessageBox, self).__init__(parent)
        self.setStyleSheet("QMessageBox { background-color: #7FDBFF; }")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.favorite_games = [] 
        self.collection = {}  
        self.star_count = 0  
        self.star_labels = []  
        self.star_checkboxes = []  
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Oyun Koleksiyonu Yönetimi')
        self.setStyleSheet("background-color: #001f3f; color: black;")

        self.player_info_label = QLabel("Oyuncu Bilgileri:\nMaruf Korkutata\nFavori Oyunlar:", self)
        self.player_info_label.setStyleSheet("font-weight: bold; color: #0074D9;")
        self.player_info_label.setGeometry(10, 10, 400, 50)

        self.favorite_games_list = QListWidget(self)
        self.favorite_games_list.setGeometry(10, 70, 200, 300)
        self.favorite_games_list.setStyleSheet("background-color: #7FDBFF; color: black;")
        self.favorite_games_list.setFocusPolicy(Qt.NoFocus)

        self.collection_label = QLabel("Koleksiyonum:", self)
        self.collection_label.setStyleSheet("font-weight: bold; color: #0074D9;")
        self.collection_label.setGeometry(10, 390, 200, 30)

        self.collection_list = QListWidget(self)
        self.collection_list.setGeometry(10, 430, 200, 150)
        self.collection_list.setStyleSheet("background-color: #7FDBFF; color: black;")
        self.collection_list.setFocusPolicy(Qt.NoFocus)

        self.game_name_label = QLabel("Oyun Adı:", self)
        self.game_name_label.setGeometry(250, 50, 80, 30)
        self.game_name_label.setStyleSheet("color: #0074D9;")

        self.game_name_input = QLineEdit(self)
        self.game_name_input.setGeometry(340, 50, 200, 30)
        self.game_name_input.setStyleSheet("background-color: #7FDBFF; color: black;")

        self.game_type_label = QLabel("Oyun Türü:", self)
        self.game_type_label.setGeometry(250, 100, 80, 30)
        self.game_type_label.setStyleSheet("color: #0074D9;")

        self.game_type_input = QLineEdit(self)
        self.game_type_input.setGeometry(340, 100, 200, 30)
        self.game_type_input.setStyleSheet("background-color: #7FDBFF; color: black;")

        self.game_platform_label = QLabel("Oyun Platformu:", self)
        self.game_platform_label.setGeometry(250, 150, 100, 30)
        self.game_platform_label.setStyleSheet("color: #0074D9;")

        self.game_platform_input = QLineEdit(self)
        self.game_platform_input.setGeometry(340, 150, 200, 30)
        self.game_platform_input.setStyleSheet("background-color: #7FDBFF; color: black;")

        self.star_labels = [QLabel(str(i), self) for i in range(1, 6)]
        for i, label in enumerate(self.star_labels):
            label.setGeometry(250 + i * 40, 200, 30, 30)
            label.setStyleSheet("color: #0074D9;")

        self.star_checkboxes = [QCheckBox("", self) for _ in range(5)]
        for i, checkbox in enumerate(self.star_checkboxes):
            checkbox.setGeometry(270 + i * 40, 240, 20, 20)
            checkbox.stateChanged.connect(self.update_stars)
            checkbox.setFocusPolicy(Qt.NoFocus)
            checkbox.setStyleSheet("color: #0074D9;")

        self.add_game_button = QPushButton("Oyunu Ekle", self)
        self.add_game_button.setGeometry(250, 280, 100, 30)
        self.add_game_button.clicked.connect(self.add_game)
        self.add_game_button.setStyleSheet("background-color: #7FDBFF; color: black;")

        self.add_favorite_button = QPushButton("Favoriye Ekle", self)
        self.add_favorite_button.setGeometry(370, 280, 100, 30)
        self.add_favorite_button.clicked.connect(self.add_favorite_game)
        self.add_favorite_button.setStyleSheet("background-color: #7FDBFF; color: black;")

        self.remove_game_button = QPushButton("Koleksiyondan Çıkar", self)
        self.remove_game_button.setGeometry(490, 280, 150, 30)
        self.remove_game_button.clicked.connect(self.remove_game)
        self.remove_game_button.setStyleSheet("background-color: #7FDBFF; color: black;")

        self.remove_favorite_button = QPushButton("Favorilerden Çıkar", self)
        self.remove_favorite_button.setGeometry(650, 280, 150, 30)
        self.remove_favorite_button.clicked.connect(self.remove_favorite_game)
        self.remove_favorite_button.setStyleSheet("background-color: #7FDBFF; color: black;")

        self.search_game_label = QLabel("Oyun Arama:", self)
        self.search_game_label.setGeometry(250, 350, 80, 30)
        self.search_game_label.setStyleSheet("color: #0074D9;")

        self.search_game_input = QLineEdit(self)
        self.search_game_input.setGeometry(340, 350, 200, 30)
        self.search_game_input.setStyleSheet("background-color: #7FDBFF; color: black;")

        self.search_game_button = QPushButton("Ara", self)
        self.search_game_button.setGeometry(550, 350, 100, 30)
        self.search_game_button.clicked.connect(self.search_game)
        self.search_game_button.setStyleSheet("background-color: #7FDBFF; color: black;")

    def update_stars(self):
        checked_count = sum(checkbox.isChecked() for checkbox in self.star_checkboxes)  

        for i, checkbox in enumerate(self.star_checkboxes):
            if checkbox.isChecked():
                self.star_count = i + 1
                break
        else:
            self.star_count = 0

        
        for i in range(5):
            if i >= self.star_count:
                self.star_checkboxes[i].setChecked(False)

    def add_game(self):
        game_name = self.game_name_input.text()
        game_type = self.game_type_input.text()
        game_platform = self.game_platform_input.text()

        if game_name and self.star_count > 0:
            if game_name not in self.collection:
                self.collection[game_name] = (game_type, game_platform, self.star_count)
                self.update_collection_list()
                self.clear_game_inputs()  
                MessageBox.information(self, "Bilgi", "Oyun eklendi!")
            else:
                MessageBox.warning(self, "Uyarı", "Bu oyun zaten koleksiyonda!")
        else:
            MessageBox.warning(self, "Uyarı", "Oyun adı boş olamaz ve en az bir yıldız seçilmelidir!")

    def add_favorite_game(self):
        selected_item = self.collection_list.currentItem()
        if selected_item:
            game_info = selected_item.text().split(" - ")
            game_name = game_info[0]
            if game_name not in [game[0] for game in self.favorite_games]:
                self.favorite_games.append((game_info[0], game_info[1], game_info[2], game_info[3]))
                self.update_favorite_games_list()
                MessageBox.information(self, "Bilgi", "Oyun favorilere eklendi!")
            else:
                MessageBox.warning(self, "Uyarı", "Bu oyun zaten favorilerde!")
        else:
            MessageBox.warning(self, "Uyarı", "Favoriye eklemek için bir oyun seçiniz!")

    def remove_game(self):
        selected_item = self.collection_list.currentItem()
        if selected_item:
            game_info = selected_item.text().split(" - ")
            game_name = game_info[0]
            if game_name in self.collection:
                del self.collection[game_name]
                self.update_collection_list()
                self.update_favorite_games_list()
                MessageBox.information(self, "Bilgi", "Oyun koleksiyondan çıkarıldı!")
            else:
                MessageBox.warning(self, "Uyarı", "Koleksiyondan çıkarmak için bir oyun seçiniz!")
        else:
            MessageBox.warning(self, "Uyarı", "Koleksiyondan çıkarmak için bir oyun seçiniz!")

    def remove_favorite_game(self):
        selected_item = self.favorite_games_list.currentItem()
        if selected_item:
            game_info = selected_item.text().split(" - ")
            game_name = game_info[0]
            for game in self.favorite_games:
                if game[0] == game_name:
                    self.favorite_games.remove(game)
                    self.update_favorite_games_list()
                    MessageBox.information(self, "Bilgi", "Oyun favorilerden çıkarıldı!")
                    break
        else:
            MessageBox.warning(self, "Uyarı", "Favorilerden çıkarmak için bir oyun seçiniz!")

    def search_game(self):
        game_name = self.search_game_input.text()
        if game_name:
            if game_name in self.collection:
                MessageBox.information(self, "Bilgi", "Bu oyuna sahipsiniz!")
            else:
                MessageBox.information(self, "Bilgi", "Bu oyuna sahip değilsiniz!")
        else:
            MessageBox.warning(self, "Uyarı", "Aramak için bir oyun adı giriniz!")

    def update_collection_list(self):
        self.collection_list.clear()
        for game, info in self.collection.items():
            self.collection_list.addItem(f"{game} - {info[0]} - {info[1]} - {info[2]}★")

    def update_favorite_games_list(self):
        self.favorite_games_list.clear()
        for game in self.favorite_games:
            self.favorite_games_list.addItem(f"{game[0]} - {game[1]} - {game[2]} - {game[3]}★")

    def clear_game_inputs(self):
        self.game_name_input.clear()
        self.game_type_input.clear()
        self.game_platform_input.clear()
        for checkbox in self.star_checkboxes:
            checkbox.setChecked(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())