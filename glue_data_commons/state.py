from glue.core.state_objects import State
from echo import SelectionCallbackProperty
from glue.core.data_combo_helper import DataCollectionComboHelper, ComponentIDComboHelper, ComboHelper

__all__ = ['DataCommonsState']


class DataCommonsState(State):

    places = SelectionCallbackProperty()
    var1 = SelectionCallbackProperty()
    var2 = SelectionCallbackProperty()
    var3 = SelectionCallbackProperty()

    def __init__(self, data_collection):

        super(DataCommonsState, self).__init__()

        self.data_collection = data_collection
                                                              
        self.places_helper = ComboHelper(self, 'places_att')
        self.var1_helper   = ComboHelper(self, 'var1_att')
        self.var2_helper   = ComboHelper(self, 'var2_att')
        self.var3_helper   = ComboHelper(self, 'var3_att')
        
        #def display_func_label(subset_group):
        #    return subset_group.label

        #self.add_callback('data', self._on_data_change)
        #self._on_data_change()

        stat_vars_list = ['Count_Person','Median_Age_Person','UnemploymentRate_Person']
        self.places_helper.choices = ['us_states','us_counties','us_cities']
        self.var1_helper.choices = stat_vars_list
        self.var2_helper.choices = stat_vars_list
        self.var3_helper.choices = stat_vars_list

        try:
            self.places_helper.selection = self.places_helper.choices[0]
            self.var1_helper.selection = self.var1_helper.choices[0]
            self.var2_helper.selection = self.var2_helper.choices[1]
            self.var3_helper.selection = self.var3_helper.choices[2]
            
        except IndexError:
            pass

        #self.subset1_helper.display = display_func_label
        #self.subset2_helper.display = display_func_label

    #def _on_data_change(self, *args, **kwargs):
    #    self.exp_att_helper.set_multiple_data([] if self.data is None else [self.data])
    #    self.gene_att_helper.set_multiple_data([] if self.data is None else [self.data])
