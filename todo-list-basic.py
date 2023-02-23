from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QCheckBox
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("To-Do List")
        self.setMinimumSize(400, 300)

        # Create widgets
        self.item_list = QListWidget()
        self.item_input = QLineEdit()
        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete")
        self.check_button = QPushButton("Check")
        self.uncheck_button = QPushButton("Uncheck")

        # Create layouts
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        button_layout = QHBoxLayout()

        # Add widgets to layouts
        input_layout.addWidget(QLabel("New item:"))
        input_layout.addWidget(self.item_input)
        input_layout.addWidget(self.add_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.check_button)
        button_layout.addWidget(self.uncheck_button)
        main_layout.addWidget(self.item_list)
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)

        # Set main layout for window
        self.setLayout(main_layout)

        # Connect signals and slots
        self.add_button.clicked.connect(self.add_item)
        self.delete_button.clicked.connect(self.delete_item)
        self.check_button.clicked.connect(self.check_item)
        self.uncheck_button.clicked.connect(self.uncheck_item)

    def add_item(self):
        # Get item text from input field
        item_text = self.item_input.text()

        # Add item to list
        item = QListWidgetItem(item_text)
        self.item_list.addItem(item)

        # Clear input field
        self.item_input.clear()

    def delete_item(self):
        # Get currently selected item
        current_item = self.item_list.currentItem()

        # Remove selected item from list
        self.item_list.takeItem(self.item_list.row(current_item))

    def check_item(self):
        # Get currently selected item
        current_item = self.item_list.currentItem()

        # Set item check state to checked
        current_item.setCheckState(2)

    def uncheck_item(self):
        # Get currently selected item
        current_item = self.item_list.currentItem()

        # Set item check state to unchecked
        current_item.setCheckState(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
