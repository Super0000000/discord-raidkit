# Form implementation generated from reading ui file 'InvokeNukeArgs.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgInvokeNukeArgs(object):
    def setupUi(self, dlgInvokeNukeArgs):
        dlgInvokeNukeArgs.setObjectName("dlgInvokeNukeArgs")
        dlgInvokeNukeArgs.resize(320, 200)
        dlgInvokeNukeArgs.setMinimumSize(QtCore.QSize(320, 200))
        dlgInvokeNukeArgs.setMaximumSize(QtCore.QSize(320, 200))
        self.btnBox = QtWidgets.QDialogButtonBox(parent=dlgInvokeNukeArgs)
        self.btnBox.setGeometry(QtCore.QRect(10, 160, 301, 32))
        self.btnBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.btnBox.setObjectName("btnBox")
        self.leMemberID = QtWidgets.QLineEdit(parent=dlgInvokeNukeArgs)
        self.leMemberID.setGeometry(QtCore.QRect(20, 100, 280, 20))
        self.leMemberID.setObjectName("leMemberID")
        self.lblMemberID = QtWidgets.QLabel(parent=dlgInvokeNukeArgs)
        self.lblMemberID.setGeometry(QtCore.QRect(20, 30, 281, 16))
        self.lblMemberID.setObjectName("lblMemberID")
        self.lblMemberID2 = QtWidgets.QLabel(parent=dlgInvokeNukeArgs)
        self.lblMemberID2.setGeometry(QtCore.QRect(20, 45, 281, 16))
        self.lblMemberID2.setObjectName("lblMemberID2")
        self.lblNotRequired = QtWidgets.QLabel(parent=dlgInvokeNukeArgs)
        self.lblNotRequired.setGeometry(QtCore.QRect(20, 80, 271, 21))
        self.lblNotRequired.setObjectName("lblNotRequired")

        self.retranslateUi(dlgInvokeNukeArgs)
        self.btnBox.accepted.connect(dlgInvokeNukeArgs.accept) # type: ignore
        self.btnBox.rejected.connect(dlgInvokeNukeArgs.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dlgInvokeNukeArgs)

    def retranslateUi(self, dlgInvokeNukeArgs):
        _translate = QtCore.QCoreApplication.translate
        dlgInvokeNukeArgs.setWindowTitle(_translate("dlgInvokeNukeArgs", "Nuke Arguments"))
        self.lblMemberID.setText(_translate("dlgInvokeNukeArgs", "Enter the member id of the member"))
        self.lblMemberID2.setText(_translate("dlgInvokeNukeArgs", "to exclude from the nuke"))
        self.lblNotRequired.setText(_translate("dlgInvokeNukeArgs", "(This field is not required)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgInvokeNukeArgs = QtWidgets.QDialog()
    ui = Ui_dlgInvokeNukeArgs()
    ui.setupUi(dlgInvokeNukeArgs)
    dlgInvokeNukeArgs.show()
    sys.exit(app.exec())