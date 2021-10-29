from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, 
    QHBoxLayout, QSpinBox, QGroupBox, QButtonGroup, 
    QRadioButton, 
)
from memo_app import app

# СОЗДАНИЕ ВИДЖЕТОВ
btn_Menu = QPushButton("Меню")
btn_Sleep = QPushButton("Отдохнуть")
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
btn_ok = QPushButton("Ответить")
lb_Quation = QLabel("XXX")

radioGroupBox = QGroupBox("Варианты ответов")
radioGroup = QButtonGroup()
rbtn1 = QRadioButton()
rbtn2 = QRadioButton()
rbtn3 = QRadioButton()
rbtn4 = QRadioButton()
radioGroup.addButton(rbtn1)
radioGroup.addButton(rbtn2)
radioGroup.addButton(rbtn3)
radioGroup.addButton(rbtn4)

ansGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel("верно / неверно")
lb_Correct = QLabel("текст ответа")

# РАЗМЕЩЕНИЕ
# панель вопросов
layout_ans1 = QHBoxLayout()

layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
radioGroupBox.setLayout(layout_ans1)

#панель результатов
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
ansGroupBox.setLayout(layout_res)
ansGroupBox.hide()

# размещение всех элементов в окне
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel("минут"))

layout_line2.addWidget(lb_Quation, alignment=Qt.AlignCenter)

layout_line3.addWidget(radioGroupBox)
layout_line3.addWidget(ansGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_ok, stretch=2)
layout_line4.addStretch(1)

# размещение на вертикальной линии
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    radioGroupBox.hide()
    ansGroupBox.show()
    btn_ok.setText("Следующий вопрос")

def show_questions():
    ansGroupBox.hide()
    radioGroupBox.show()
    btn_ok.setText("Ответить")
    # сброс радиокнопок
    radioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    radioGroup.setExclusive(True)

