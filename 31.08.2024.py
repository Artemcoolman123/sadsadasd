from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QFormLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLablet, QSpinBox

# Theme

app = QApplication([])
btn_menu = QPushButton('Меню')
btn_sleep = QPushButton('Відпочити')
Box_time = QSpinBox()
Box_time.setValue(30)
btn_ok = QPushButton('Відповісти')
question = QLablet('###')

# Button

RadioButton = QGroupBox('Варіанти відповідей')
RadioGroup = QButtonGroup()
rdbtn_1 = QRadioButton("Answer1")
rdbtn_2 = QRadioButton("Answer2")
rdbtn_3 = QRadioButton("Answer3")
rdbtn_4 = QRadioButton("Answer4")
RatioGroup.addButton(rdbtn_1)
RatioGroup.addButton(rdbtn_2)
RatioGroup.addButton(rdbtn_3)
RatioGroup.addButton(rdbtn_4)

# паенелька з результагтом
answerGroupBox = QGroupBox('Результат тесту')
Lb_result = QLablet('#')
Lb_true_ans = QLablet('#')

# Розміщення

ans1_layout = QHBoxLayout()
ans2_layout = QVBoxLayout()
ans3_layout = QHBoxLayout()

ans2_layout.addWidget(rdbtn_1)
ans2_layout.addWidget(rdbtn_2)

ans3_layout.addWidget(rdbtn_3)
ans3_layout.addWidget(rdbtn_4)

ans1_layout.addLayout(ans2_layout)
ans1_layout.addLayout(ans3_layout)


