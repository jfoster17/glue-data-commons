import os
import numpy as np
from qtpy import QtWidgets
from echo.qt import autoconnect_callbacks_to_qt

from glue.core.subset import MultiOrState
from glue.utils.qt import load_ui

from ..state import DataCommonsState
import datacommons_pandas as dcp

__all__ = ['DataCommonsDialog']


class DataCommonsDialog(QtWidgets.QDialog):

    def __init__(self, collect, default=None, parent=None):

        super(DataCommonsDialog, self).__init__(parent=parent)

        self.state = DataCommonsState(collect)

        self.ui = load_ui('data_commons.ui', self,
                          directory=os.path.dirname(__file__))
        self._connections = autoconnect_callbacks_to_qt(self.state, self.ui)

        self._collect = collect

        i#f default is not None:
         #   self.state.data = default

        self.ui.button_ok.clicked.connect(self.accept)
        self.ui.button_cancel.clicked.connect(self.reject)

    def _apply(self):
        """
        """
        USA = 'country/USA'
        if self.state.places == 'us_states':
            states = dcp.get_places_in([USA], 'State')[USA]
            places = states
        elif self.state.places == 'us_counties':
            counties = dcp.get_places_in([USA], 'County')[USA]
            places = counties
        elif self.state.places == 'us_cities':
            cities = dcp.get_places_in([USA], 'City')[USA]
            places = cities
            
        stats_vars = [self.state.var1,self.state.var2,self.state.var3]
        df = dcp.dc.build_multivariate_dataframe(places, stats_vars)
        def add_name_col(df):
            # Add a new column called name, where each value is the name for the place dcid in the index.
            df['name'] = df.index.map(dcp.get_property_values(df.index, 'name'))
            # Keep just the first name, instead of a list of all names.
            df['name'] = df['name'].str[0]
        add_name_col(df)
        self.data_collection[self.state.places] = df


    @classmethod
    def get_pandas_table(cls, collect, default=None, parent=None):
        self = cls(collect, parent=parent, default=default)
        value = self.exec_()

        if value == QtWidgets.QDialog.Accepted:
            self._apply()
