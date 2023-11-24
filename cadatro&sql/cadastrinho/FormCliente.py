import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QLabel, QMessageBox, QPushButton

class FormularioCliente(QWidget):
    def __init__(self):
        super().__init__()
        
        # Define os widgets do formulário
        self.nome_edit = QLineEdit()
        self.cpf_edit = QLineEdit()
        self.endereco_edit = QLineEdit()
        self.telefone_edit = QLineEdit()
        self.cadastrar_button = QPushButton()
        
        # Define os eventos do formulário
        self.cadastrar_button.clicked.connect(self.cadastrar)
        

        # Layout dos widgets
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Nome:"))
        layout.addWidget(self.nome_edit)
        layout.addWidget(QLabel("CPF:"))
        layout.addWidget(self.cpf_edit)
        layout.addWidget(QLabel("Endereço:"))
        layout.addWidget(self.endereco_edit)
        layout.addWidget(QLabel("Telefone:"))
        layout.addWidget(self.telefone_edit)
        layout.addWidget(self.cadastrar_button)

        self.setLayout(layout)

    def cadastrar(self):
        # Salva os dados do formulário
        nome = self.nome_edit.text()
        cpf = self.cpf_edit.text()
        endereco = self.endereco_edit.text()
        telefone = self.telefone_edit.text()

        # Mostra uma mensagem de confirmação
        msg = f"Cliente cadastrado com sucesso: {nome} - {cpf}"
        self.show_message(msg)

    def show_message(self, msg):
        # Mostra uma mensagem na tela
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Mensagem")
        msg_box.setText(msg)
        msg_box.exec()

if __name__ == "__main__":
    # Cria uma instância do aplicativo
    app = QApplication(sys.argv)

    # Cria uma instância do formulário
    formulario = FormularioCliente()

    # Exibe o formulário
    formulario.show()

    # Executa o aplicativo
    sys.exit(app.exec())
