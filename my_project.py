# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OurSchoolDiary.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 460)
        self.line_1 = QtWidgets.QFrame(Form)
        self.line_1.setGeometry(QtCore.QRect(20, 10, 461, 16))
        self.line_1.setLineWidth(2)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.label_formirovanie = QtWidgets.QLabel(Form)
        self.label_formirovanie.setGeometry(QtCore.QRect(90, 20, 310, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_formirovanie.setFont(font)
        self.label_formirovanie.setObjectName("label_formirovanie")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(20, 420, 460, 20))
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.comboBox_zachto = QtWidgets.QComboBox(Form)
        self.comboBox_zachto.setGeometry(QtCore.QRect(20, 270, 140, 26))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_zachto.setFont(font)
        self.comboBox_zachto.setObjectName("comboBox_zachto")
        self.comboBox_zachto.addItem("")
        self.comboBox_zachto.addItem("")
        self.comboBox_zachto.addItem("")
        self.comboBox_zachto.addItem("")
        self.comboBox_zachto.addItem("")
        self.comboBox_zachto.addItem("")
        self.comboBox_zachto.addItem("")

        self.label_student = QtWidgets.QLabel(Form)
        self.label_student.setGeometry(QtCore.QRect(30, 150, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_student.setFont(font)
        self.label_student.setObjectName("label_student")
        self.comboBox_students = QtWidgets.QComboBox(Form)
        self.comboBox_students.setGeometry(QtCore.QRect(20, 190, 140, 26))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_students.setFont(font)
        self.comboBox_students.setObjectName("comboBox_students")
        self.comboBox_students.addItem("")
        self.comboBox_students.addItem("")
        self.comboBox_students.addItem("")
        self.comboBox_students.addItem("")
        self.comboBox_students.addItem("")
        self.comboBox_students.addItem("")
        self.label_subject = QtWidgets.QLabel(Form)
        self.label_subject.setGeometry(QtCore.QRect(200, 150, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_subject.setFont(font)
        self.label_subject.setObjectName("label_subject")
        self.comboBox_subject = QtWidgets.QComboBox(Form)
        self.comboBox_subject.setGeometry(QtCore.QRect(200, 190, 140, 26))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_subject.setFont(font)
        self.comboBox_subject.setObjectName("comboBox_subject")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.label_zachto = QtWidgets.QLabel(Form)
        self.label_zachto.setGeometry(QtCore.QRect(30, 230, 135, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_zachto.setFont(font)
        self.label_zachto.setObjectName("label_zachto")
        self.dateEdit_3 = QtWidgets.QDateEdit(Form)
        self.dateEdit_3.setGeometry(QtCore.QRect(110, 60, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                      "color: rgb(255, 255, 255);")
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.label_date = QtWidgets.QLabel(Form)
        self.label_date.setGeometry(QtCore.QRect(30, 60, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.label_grade = QtWidgets.QLabel(Form)
        self.label_grade.setGeometry(QtCore.QRect(200, 230, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_grade.setFont(font)
        self.label_grade.setObjectName("label_grade")
        self.comboBox_grade = QtWidgets.QComboBox(Form)
        self.comboBox_grade.setGeometry(QtCore.QRect(200, 270, 140, 26))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_grade.setFont(font)
        self.comboBox_grade.setObjectName("comboBox_grade")
        self.comboBox_grade.addItem("")
        self.comboBox_grade.addItem("")
        self.comboBox_grade.addItem("")
        self.comboBox_grade.addItem("")
        self.comboBox_grade.addItem("")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 60, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(253, 142, 15);")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(20, 300, 461, 16))
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 320, 440, 100))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Our School Diary"))
        self.label_formirovanie.setText(_translate("Form", "???????????????????????? ???????????? ???? ????????????????????????"))
        self.comboBox_zachto.setItemText(0, _translate("Form", "???????????? ???? ??????????"))
        self.comboBox_zachto.setItemText(1, _translate("Form", "???????????????? ????????????"))
        self.comboBox_zachto.setItemText(2, _translate("Form", "?????????????????????????????? ????????????"))
        self.comboBox_zachto.setItemText(3, _translate("Form", "?????????????????????? ????????????"))
        self.comboBox_zachto.setItemText(4, _translate("Form", "????????????"))
        self.comboBox_zachto.setItemText(5, _translate("Form", "?????????????????????? ??????????????"))
        self.comboBox_zachto.setItemText(6, _translate("Form", "??????????????????"))
        self.label_student.setText(_translate("Form", "????????????:"))
        self.comboBox_students.setItemText(0, _translate("Form", "????????"))
        self.comboBox_students.setItemText(1, _translate("Form", "????????"))
        self.comboBox_students.setItemText(2, _translate("Form", "????????????"))
        self.comboBox_students.setItemText(3, _translate("Form", "????????????"))
        self.comboBox_students.setItemText(4, _translate("Form", "????????"))
        self.comboBox_students.setItemText(5, _translate("Form", "????????"))
        self.label_subject.setText(_translate("Form", "??????????????:"))
        self.comboBox_subject.setItemText(0, _translate("Form", "??????????????"))
        self.comboBox_subject.setItemText(1, _translate("Form", "??????????????????"))
        self.comboBox_subject.setItemText(2, _translate("Form", "??????????????????????"))
        self.comboBox_subject.setItemText(3, _translate("Form", "?????????????? ????????"))
        self.comboBox_subject.setItemText(4, _translate("Form", "???????????????????? ????????"))
        self.comboBox_subject.setItemText(5, _translate("Form", "????????????????????"))
        self.comboBox_subject.setItemText(6, _translate("Form", "????????????"))
        self.comboBox_subject.setItemText(7, _translate("Form", "??????????"))
        self.comboBox_subject.setItemText(8, _translate("Form", "??????????????"))
        self.comboBox_subject.setItemText(9, _translate("Form", "????????????????????????????"))
        self.comboBox_subject.setItemText(10, _translate("Form", "??????????????????"))
        self.comboBox_subject.setItemText(11, _translate("Form", "????????????????"))
        self.label_zachto.setText(_translate("Form", "???? ?????? ????????????:"))
        self.label_date.setText(_translate("Form", "????????:"))
        self.label_grade.setText(_translate("Form", "????????????:"))
        self.comboBox_grade.setItemText(0, _translate("Form", "5"))
        self.comboBox_grade.setItemText(1, _translate("Form", "4"))
        self.comboBox_grade.setItemText(2, _translate("Form", "3"))
        self.comboBox_grade.setItemText(3, _translate("Form", "2"))
        self.comboBox_grade.setItemText(4, _translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "???????????????? ?? ????"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
