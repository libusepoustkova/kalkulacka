from PyQt5 import QtWidgets, uic
def main():
    #vytvoreni aplikace a okna
    app=QtWidgets.QApplication([])
    window=QtWidgets.QDialog()
    #nacteni ovladatek
    with open('kalkulacka.ui',encoding='UTF-8') as f: #f je soubor, with samo zajisti zavreni souboru)
        uic.loadUi(f,window)

    sb_operand1=window.findChild(QtWidgets.QDoubleSpinBox,'sb_operand1')
    cb_operator=window.findChild(QtWidgets.QComboBox,'cb_operator')
    sb_operand2=window.findChild(QtWidgets.QDoubleSpinBox,'sb_operand2')
    sb_result=window.findChild(QtWidgets.QDoubleSpinBox,'sb_result')
    sb_operand2.setValue(123)

    def calculate():
        operand1=sb_operand1.value()
        operand2=sb_operand2.value()
        operator=cb_operator.currentText()
        try:
            if operator=='+':
                result=operand1+operand2
            elif operator=='-':
                result=operand1-operand2
            elif operator=='/':
                result=operand1/operand2
            elif operator=='*':
                result=operand1*operand2
            else:
                raise ValueError('bad operator')
        except Exception:
            sb_result.setPrefix('ERR')
            sb_result.setValue(0)
        else:
            sb_result.setPrefix('')
            sb_result.setValue(result)

    sb_operand1.valueChanged.connect(calculate)
    sb_operand2.valueChanged.connect(calculate)
    cb_operator.currentTextChanged.connect(calculate)


    #Spusteni
    window.show()
    return app.exec()
main()