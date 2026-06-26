import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.grafo = None
        self._lista = None
        self._A = None
        self._Da = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleCreaGrafo(self,e):
        self._model.prendi_constructors(self._Da, self._A)
        self.grafo = self._model.handle_grafo()
        self._view.txt_result.controls.append(ft.Text(f"numero nodi : {len(self.grafo.nodes)}!"))
        self._view.txt_result.controls.append(ft.Text(f"numero archi : {len(self.grafo.edges)}!"))
        self._view.update_page()


    def handleDettagli(self, e):
        pass

    def handleCerca(self, e):
        pass

    def handleAggiungiElementi(self, dd: ft.Dropdown()):

        anni = self._model.anni

        if dd.label == "Da":
            for a in anni:
                dd.options.append(ft.dropdown.Option(text=a,
                                             data=a,
                                             on_click=self.read_Da))
        elif dd.label == "A":
            for a in anni:
                dd.options.append(ft.dropdown.Option(text=a,
                                                    data=a,
                                                    on_click=self.read_A))

    def read_A(self,e):
        if e.control.data is None:
            self._A = None
        else:
            self._A = e.control.data

    def read_Da(self,e):
        if e.control.data is None:
            self._Da = None
        else:
            self._Da = e.control.data


