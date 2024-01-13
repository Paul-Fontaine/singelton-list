from vectorsingleton import VectorSingleton
from PySide6.QtWidgets import QWidget, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout, QInputDialog


class VectorManagementWindow(QWidget):
    def __init__(self, parent: QWidget):
        QWidget.__init__(self, parent=parent)
        vlayout = QVBoxLayout(self)

        self.__data: VectorSingleton = VectorSingleton.get_instance()
        self.__list = QListWidget()

        # buttons
        self.__button_remove = QPushButton("remove", self)
        # !!! auto-completion will put parenthesis at self.__remove, but they must be removed
        # else the callback won't be connected to the button and this line will execute the callback instead
        self.__button_remove.clicked.connect(self.__remove)
        self.__button_add = QPushButton("add", self)
        self.__button_add.clicked.connect(self.__add)
        self.__button_update = QPushButton("update", self)
        self.__button_update.clicked.connect(self.__update)

        # buttons horizontal layout
        hlayout = QHBoxLayout(self)
        hlayout.addWidget(self.__button_remove)
        hlayout.addWidget(self.__button_add)
        hlayout.addWidget(self.__button_update)

        # Window vertical layout
        vlayout.addWidget(self.__list)
        vlayout.addLayout(hlayout)

    def __remove(self):
        current_item_index = self.__list.currentRow()
        VectorSingleton.get_instance().pop(current_item_index)
        self.__update()

    def __add(self):
        # a dialog box pops with an input and a button "ok" and a button "cancel"
        # new_item store the text of the input
        # ok, a bool, store the button used to exit the dialog box : true with "ok", false with "cancel"
        new_item, ok = QInputDialog.getText(self, "add", "name of item to add : ", text=str(len(VectorSingleton.get_instance())))
        if ok:
            VectorSingleton.get_instance().append(new_item)
            self.__update()

    def __update(self):
        self.__list.clear()
        self.__list.addItems(VectorSingleton.get_instance())
