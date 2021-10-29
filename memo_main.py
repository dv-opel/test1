from PyQt5.QtWidgets import QWidget
from memo_card_layout import *
from random import shuffle

CARD_WIDTH = 600
CARD_HEIGHT = 500

frm_question = "Яблоко"
frm_right = "apple"
frm_wrong1 = "bbbbb"
frm_wrong2 = "ccccc"
frm_wrong3 = "ddddd"

# распределение ответов между кнопками
radio_list = [rbtn1, rbtn2, rbtn3, rbtn4]
shuffle(radio_list)
answer = radio_list[0]
wrong_answer1 = radio_list[1]
wrong_answer2 = radio_list[2]
wrong_answer3 = radio_list[3]

def show_data():
    lb_Quation.setText(frm_question)
    lb_Correct.setText(frm_right)
    answer.setText(frm_right)
    wrong_answer1.setText(frm_wrong1)
    wrong_answer2.setText(frm_wrong2)
    wrong_answer3.setText(frm_wrong3)

def chek_result():
    if answer.isChecked():
        lb_Result.setText("Верно")
        show_result()
    if wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked():
        lb_Result.setText("Неверно")
        show_result()

def click_ok():
    if btn_ok.text() == "Ответить":
        chek_result()


# Создание Окна
window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(CARD_WIDTH, CARD_HEIGHT)
window.move(300, 200)

window.setLayout(layout_card)
show_data()
show_questions()
btn_ok.clicked.connect(click_ok)


window.show()
app.exec_()

