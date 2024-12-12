#Crear una aplicación para memorizar información
#jpara isntalar en el env
# en mac 
#/Users/macbookair/Documents/python2023/EscuelaPYthon/.venv/bin/python -m pip install pyqt5      

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(
        self,question,right_answer,
        wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1= wrong1
        self.wrong2= wrong2
        self.wrong3= wrong3

 
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Memory card')
my_win.resize(300,200)
       
RadioGroupBox = QGroupBox('Opciones de respuesta')

rbtn_1 = QRadioButton('Enets')
rbtn_2 = QRadioButton('Pitufos')
rbtn_3 = QRadioButton('chulyms')
rbtn_4 = QRadioButton('aleutas')

answers=[rbtn_1, rbtn_2, rbtn_3, rbtn_4]

RadioGroup=QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()


layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

ansGrupBox = QGroupBox('Resultado de prueba')
label_result= QLabel('¿Es correcto o no?')
label_ansCorrect=QLabel('¡Aqui estara la respuesta!')


layout_ans= QVBoxLayout()
layout_ans.addWidget(label_result)
layout_ans.addWidget(label_ansCorrect, alignment= Qt.AlignHCenter)

ansGrupBox.setLayout(layout_ans)

line_h1 = QHBoxLayout()
line_h2 = QHBoxLayout()
line_h3 = QHBoxLayout()


question = QLabel('¿Qué nacionalidad no existe?')
line_h1.addWidget(question, alignment= Qt.AlignHCenter)


line_h2.addWidget(RadioGroupBox)
line_h2.addWidget(ansGrupBox)
ansGrupBox.hide()


answer = QPushButton('Respuesta')
line_h3.addWidget(answer, alignment= Qt.AlignHCenter)


line_1 = QVBoxLayout()
line_1.addLayout(line_h1)
line_1.addLayout(line_h2)
line_1.addLayout(line_h3)


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    label_ansCorrect.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        label_result.setText('Correcto')
        my_win.score += 1
        show_result()
        
        
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        label_result.setText('Incorrecto')
        show_result()
    
    print('E S T A D I S T I C A S :')
    print('-Preguntas totales:', my_win.total)
    print('-Pregutas correctas:', my_win.score)
    print('-Calificación:',my_win.score/my_win.total*100,'%')


        
def show_result():
    RadioGroupBox.hide()
    ansGrupBox.show()
    answer.setText('Siguiente pregunta')
        
def show_question():
    #activar o mostrar la pregunta 
    RadioGroupBox.show()
    ansGrupBox.hide() #respuesta es bien o mal
    answer.setText('Respuesta')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
        
def star_test():
    #print("You clicked on the button",answer.text())
    
    if answer.text()=='Respuesta':
        check_answer()
        
    elif answer.text()=='Siguiente pregunta':
        next_question()
    
def next_question():
    my_win.total += 1
    q = list_question[randint(0, len(list_question)-1)] #obtener un apregunta al azar
    ask(q)
line_1.setSpacing(40)
my_win.setLayout(line_1)
my_win.show()


#lista de las preguntas
list_question = []
list_question.append(Question('¿Que numero es mayor?','19','17','15','8'))
list_question.append(Question('¿Que idioma se habla en china?','mandarin','ingles','español','chino'))
list_question.append(Question('¿Que se utiliza para hacer un pregunta en lenguaje de progamacion?','input','while','if','print'))
list_question.append(Question('¿Cual es la capital de Colombia?','Bogota','Cali','Lima','Quito'))
list_question.append(Question('¿Cuanto es 2+2*3?','8','12','10','6'))

my_win.score = 0 #respuestas buenas
my_win.total = 0 #preguntas totales

next_question()





answer.clicked.connect(star_test)
app.exec()