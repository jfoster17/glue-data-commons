from glue.config import menubar_plugin

from .qt.data_commons import DataCommonsDialog

@menubar_plugin("Get Data Commons Data")
def data_commons_plugin(session, data_collection):
    DataCommonsDialog.get_pandas_table(data_collection,
                                       default=None, parent=None)
    return
