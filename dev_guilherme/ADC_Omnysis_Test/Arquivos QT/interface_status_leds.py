# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_status_leds.ui'
#
# Created: Thu Jan 26 16:53:35 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(755, 682)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 20, 341, 311))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(60, 185, 91, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 65, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.kled_ger_sin_clk = KLed(self.frame)
        self.kled_ger_sin_clk.setGeometry(QtCore.QRect(20, 100, 28, 28))
        self.kled_ger_sin_clk.setState(KLed.Off)
        self.kled_ger_sin_clk.setObjectName(_fromUtf8("kled_ger_sin_clk"))
        self.kled_switch = KLed(self.frame)
        self.kled_switch.setGeometry(QtCore.QRect(20, 180, 28, 28))
        self.kled_switch.setState(KLed.Off)
        self.kled_switch.setObjectName(_fromUtf8("kled_switch"))
        self.kled_crate = KLed(self.frame)
        self.kled_crate.setGeometry(QtCore.QRect(20, 60, 28, 28))
        self.kled_crate.setState(KLed.Off)
        self.kled_crate.setObjectName(_fromUtf8("kled_crate"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 145, 251, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.kled_ger_sin_in = KLed(self.frame)
        self.kled_ger_sin_in.setGeometry(QtCore.QRect(20, 140, 28, 28))
        self.kled_ger_sin_in.setState(KLed.Off)
        self.kled_ger_sin_in.setObjectName(_fromUtf8("kled_ger_sin_in"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 105, 201, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 20, 341, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_11 = QtGui.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(60, 265, 171, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.kled_data_acquisition = KLed(self.frame)
        self.kled_data_acquisition.setGeometry(QtCore.QRect(20, 260, 28, 28))
        self.kled_data_acquisition.setState(KLed.Off)
        self.kled_data_acquisition.setObjectName(_fromUtf8("kled_data_acquisition"))
        self.label_14 = QtGui.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(60, 225, 171, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.kled_fpga = KLed(self.frame)
        self.kled_fpga.setGeometry(QtCore.QRect(20, 220, 28, 28))
        self.kled_fpga.setState(KLed.Off)
        self.kled_fpga.setObjectName(_fromUtf8("kled_fpga"))
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(380, 20, 341, 321))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(60, 186, 101, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(60, 66, 51, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.kled_sfdr = KLed(self.frame_2)
        self.kled_sfdr.setGeometry(QtCore.QRect(20, 100, 31, 31))
        self.kled_sfdr.setState(KLed.Off)
        self.kled_sfdr.setObjectName(_fromUtf8("kled_sfdr"))
        self.kled_crosstalk = KLed(self.frame_2)
        self.kled_crosstalk.setGeometry(QtCore.QRect(20, 180, 31, 31))
        self.kled_crosstalk.setState(KLed.Off)
        self.kled_crosstalk.setObjectName(_fromUtf8("kled_crosstalk"))
        self.kled_snr = KLed(self.frame_2)
        self.kled_snr.setGeometry(QtCore.QRect(20, 60, 31, 31))
        self.kled_snr.setState(KLed.Off)
        self.kled_snr.setObjectName(_fromUtf8("kled_snr"))
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(60, 150, 251, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.kled_enob = KLed(self.frame_2)
        self.kled_enob.setGeometry(QtCore.QRect(20, 140, 31, 31))
        self.kled_enob.setState(KLed.Off)
        self.kled_enob.setObjectName(_fromUtf8("kled_enob"))
        self.label_9 = QtGui.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(60, 105, 201, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(0, 20, 341, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.kled_dif_amp = KLed(self.frame_2)
        self.kled_dif_amp.setGeometry(QtCore.QRect(20, 220, 31, 31))
        self.kled_dif_amp.setState(KLed.Off)
        self.kled_dif_amp.setObjectName(_fromUtf8("kled_dif_amp"))
        self.label_12 = QtGui.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(60, 225, 141, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.kled_missing_codes = KLed(self.frame_2)
        self.kled_missing_codes.setGeometry(QtCore.QRect(20, 260, 31, 31))
        self.kled_missing_codes.setState(KLed.Off)
        self.kled_missing_codes.setObjectName(_fromUtf8("kled_missing_codes"))
        self.label_13 = QtGui.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(60, 270, 141, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.frame_3 = QtGui.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(20, 350, 341, 261))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_20 = QtGui.QLabel(self.frame_3)
        self.label_20.setGeometry(QtCore.QRect(60, 175, 111, 21))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.frame_3)
        self.label_21.setGeometry(QtCore.QRect(60, 55, 51, 21))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.kled_ad9510 = KLed(self.frame_3)
        self.kled_ad9510.setGeometry(QtCore.QRect(20, 90, 28, 28))
        self.kled_ad9510.setState(KLed.Off)
        self.kled_ad9510.setObjectName(_fromUtf8("kled_ad9510"))
        self.kled_ics854s01i = KLed(self.frame_3)
        self.kled_ics854s01i.setGeometry(QtCore.QRect(20, 170, 28, 28))
        self.kled_ics854s01i.setState(KLed.Off)
        self.kled_ics854s01i.setObjectName(_fromUtf8("kled_ics854s01i"))
        self.kled_si571 = KLed(self.frame_3)
        self.kled_si571.setGeometry(QtCore.QRect(20, 50, 28, 28))
        self.kled_si571.setState(KLed.Off)
        self.kled_si571.setObjectName(_fromUtf8("kled_si571"))
        self.label_22 = QtGui.QLabel(self.frame_3)
        self.label_22.setGeometry(QtCore.QRect(60, 135, 251, 21))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.kled_eeprom = KLed(self.frame_3)
        self.kled_eeprom.setGeometry(QtCore.QRect(20, 130, 28, 28))
        self.kled_eeprom.setState(KLed.Off)
        self.kled_eeprom.setObjectName(_fromUtf8("kled_eeprom"))
        self.label_23 = QtGui.QLabel(self.frame_3)
        self.label_23.setGeometry(QtCore.QRect(60, 95, 201, 21))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.frame_3)
        self.label_24.setGeometry(QtCore.QRect(0, 20, 341, 20))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.kled_sensor_temperatura = KLed(self.frame_3)
        self.kled_sensor_temperatura.setGeometry(QtCore.QRect(20, 210, 28, 28))
        self.kled_sensor_temperatura.setState(KLed.Off)
        self.kled_sensor_temperatura.setObjectName(_fromUtf8("kled_sensor_temperatura"))
        self.label_25 = QtGui.QLabel(self.frame_3)
        self.label_25.setGeometry(QtCore.QRect(60, 215, 181, 21))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.frame_4 = QtGui.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(380, 360, 341, 251))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.label_27 = QtGui.QLabel(self.frame_4)
        self.label_27.setGeometry(QtCore.QRect(60, 45, 51, 21))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.kled_statusFAIL = KLed(self.frame_4)
        self.kled_statusFAIL.setGeometry(QtCore.QRect(20, 80, 28, 28))
        self.kled_statusFAIL.setColor(QtGui.QColor(255, 0, 0))
        self.kled_statusFAIL.setObjectName(_fromUtf8("kled_statusFAIL"))
        self.kled_statusOK = KLed(self.frame_4)
        self.kled_statusOK.setGeometry(QtCore.QRect(20, 40, 28, 28))
        self.kled_statusOK.setObjectName(_fromUtf8("kled_statusOK"))
        self.label_28 = QtGui.QLabel(self.frame_4)
        self.label_28.setGeometry(QtCore.QRect(60, 165, 251, 21))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.kled_statusNotUsed = KLed(self.frame_4)
        self.kled_statusNotUsed.setGeometry(QtCore.QRect(20, 160, 28, 28))
        self.kled_statusNotUsed.setColor(QtGui.QColor(0, 0, 255))
        self.kled_statusNotUsed.setObjectName(_fromUtf8("kled_statusNotUsed"))
        self.label_29 = QtGui.QLabel(self.frame_4)
        self.label_29.setGeometry(QtCore.QRect(60, 85, 201, 21))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(self.frame_4)
        self.label_30.setGeometry(QtCore.QRect(0, 20, 341, 20))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.kled_statusNaoAvaliado = KLed(self.frame_4)
        self.kled_statusNaoAvaliado.setGeometry(QtCore.QRect(20, 200, 28, 28))
        self.kled_statusNaoAvaliado.setState(KLed.Off)
        self.kled_statusNaoAvaliado.setObjectName(_fromUtf8("kled_statusNaoAvaliado"))
        self.label_31 = QtGui.QLabel(self.frame_4)
        self.label_31.setGeometry(QtCore.QRect(60, 205, 251, 21))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.kled_statusExecutando = KLed(self.frame_4)
        self.kled_statusExecutando.setGeometry(QtCore.QRect(20, 120, 28, 28))
        self.kled_statusExecutando.setColor(QtGui.QColor(255, 255, 0))
        self.kled_statusExecutando.setObjectName(_fromUtf8("kled_statusExecutando"))
        self.label_32 = QtGui.QLabel(self.frame_4)
        self.label_32.setGeometry(QtCore.QRect(60, 126, 201, 20))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.OK_Button = QtGui.QPushButton(Dialog)
        self.OK_Button.setGeometry(QtCore.QRect(620, 640, 87, 27))
        self.OK_Button.setObjectName(_fromUtf8("OK_Button"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(220, 640, 311, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Status", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>Switch</p></body></html>", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>CRATE</p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>Gerador de Sinais (Input Signal)</p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>Gerador de Sinais (Clock)</p></body></html>", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">COMUNICAÇÃO/AQUISIÇÃO DE DADOS</span></p></body></html>", None))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p>Aquisição de Dados</p></body></html>", None))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p>Gravação da FPGA</p></body></html>", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p>CROSSTALK</p></body></html>", None))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p>SNR</p></body></html>", None))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p>ENOB</p></body></html>", None))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p>SFDR</p></body></html>", None))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">TESTES DE PERFOMANCE</span></p></body></html>", None))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p>DIF. AMPLITUDES</p></body></html>", None))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p>MISSING CODES</p></body></html>", None))
        self.label_20.setText(_translate("Dialog", "<html><head/><body><p>ICS854S01I</p></body></html>", None))
        self.label_21.setText(_translate("Dialog", "<html><head/><body><p>Si571</p></body></html>", None))
        self.label_22.setText(_translate("Dialog", "<html><head/><body><p>EEPROM</p></body></html>", None))
        self.label_23.setText(_translate("Dialog", "<html><head/><body><p>AD9510</p></body></html>", None))
        self.label_24.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">TESTES DE COMPONENTES</span></p></body></html>", None))
        self.label_25.setText(_translate("Dialog", "<html><head/><body><p>Sensor de Temperatura</p></body></html>", None))
        self.label_27.setText(_translate("Dialog", "<html><head/><body><p>OK</p></body></html>", None))
        self.label_28.setText(_translate("Dialog", "<html><head/><body><p>Não será executado</p></body></html>", None))
        self.label_29.setText(_translate("Dialog", "<html><head/><body><p>Falhou</p></body></html>", None))
        self.label_30.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">LEGENDA</span></p></body></html>", None))
        self.label_31.setText(_translate("Dialog", "<html><head/><body><p>Status ainda não avaliado</p></body></html>", None))
        self.label_32.setText(_translate("Dialog", "<html><head/><body><p>Em execução</p></body></html>", None))
        self.OK_Button.setText(_translate("Dialog", "OK", None))

from PyKDE4.kdeui import KLed

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

