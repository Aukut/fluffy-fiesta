import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
from cryptography.fernet import Fernet

class EncryptionDecryptionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Encryption and Decryption App")
        self.setGeometry(200, 200, 400, 150)
        
        self.layout = QVBoxLayout()
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        
        self.encrypt_button = QPushButton("Encrypt Data", self)
        self.decrypt_button = QPushButton("Decrypt Data", self)
        
        self.encrypt_button.clicked.connect(self.encrypt_data)
        self.decrypt_button.clicked.connect(self.decrypt_data)
        
        self.layout.addWidget(self.encrypt_button)
        self.layout.addWidget(self.decrypt_button)
        
    def encrypt_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Encrypt")
        if file_path:
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            
            with open(file_path, 'rb') as file:
                data = file.read()
                encrypted_data = cipher_suite.encrypt(data)
            
            encrypted_file_path, _ = QFileDialog.getSaveFileName(self, "Save Encrypted File")
            if encrypted_file_path:
                with open(encrypted_file_path, 'wb') as file:
                    file.write(encrypted_data)
                QMessageBox.information(self, "Encryption Successful", "Data encrypted successfully!")
    
    def decrypt_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Decrypt")
        if file_path:
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            
            with open(file_path, 'rb') as file:
                encrypted_data = file.read()
                decrypted_data = cipher_suite.decrypt(encrypted_data)
            
            decrypted_file_path, _ = QFileDialog.getSaveFileName(self, "Save Decrypted File")
            if decrypted_file_path:
                with open(decrypted_file_path, 'wb') as file:
                    file.write(decrypted_data)
                QMessageBox.information(self, "Decryption Successful", "Data decrypted successfully!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EncryptionDecryptionApp()
    window.show()
    sys.exit(app.exec_())
