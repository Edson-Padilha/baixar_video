import sys
from PySide6 import QtCore, QtGui, QtWidgets
from pytube import YouTube

def download_video(url, output_path="S:\RH\Videos"):
    try:
        print("Downloading video...")
        yt = YouTube(url)
        
        # Seleciona a melhor resolução disponível
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
    
        video_stream.download(output_path)
        print("Download concluído!")         
                
    except Exception as e:
        # Create a QMessageBox for error notification
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Erro durante o download")
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setText("Ocorreu um erro durante o download.")
        msg_box.setInformativeText(f"Erro: {str(e)}")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Title window
        self.setWindowTitle("Baixe seu Video - S:\RH\Videos")

        # Window size
        self.resize(700,200)

        # Horizontal layout
        main_layout = QtWidgets.QHBoxLayout()

        # Define background color
        self.setStyleSheet("background-color: Darkgray;")

        # Create widgets
        self.url_label = QtWidgets.QLabel("URL:")
        self.url_edit = QtWidgets.QLineEdit()
        self.clear_button = QtWidgets.QPushButton("Limpar")
        self.send_button = QtWidgets.QPushButton("Baixar")

        # Font
        font = QtGui.QFont()
        font.setPointSize(12)
        #font.setBold(True)

        self.url_label.setFont(font)
        self.url_edit.setFont(font)
        self.clear_button.setFont(font)
        self.send_button.setFont(font)

        # Add to layout
        main_layout.addWidget(self.url_label)
        main_layout.addWidget(self.url_edit)
        main_layout.addWidget(self.clear_button)
        main_layout.addWidget(self.send_button)     
        
        self.url_edit.setStyleSheet("height: 25px;")
        self.url_edit.setPlaceholderText("https://www.youtube.com/meu_video")

        # Define background color lineEdit
        self.url_edit.setStyleSheet("background-color: white;")

        # Connections 
        self.clear_button.clicked.connect(self.clear_url)
        self.send_button.clicked.connect(self.send_url)
        self.url_edit.textChanged.connect(self.on_edit_changed)

        # Central widget
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
    
    # Limpando campo
    def clear_url(self):
        self.url_edit.setText("")

    def on_edit_changed(self):
        text = self.url_edit.text()
        self.url_edit.setText(text.strip())

    def send_url(self):
        # Obter URL
        url = self.url_edit.text()

        if len(url) == 0:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText("Favor informar URL")
            msg_box.exec_()
            return
        # (Adicione aqui o código para processar a URL)
        download_video(url)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
