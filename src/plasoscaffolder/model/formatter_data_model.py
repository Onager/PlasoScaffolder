# -*- coding: utf-8 -*-
"""The Formatter Data model class."""
from plasoscaffolder.model import base_data_model
from plasoscaffolder.model import sql_query_model


class FormatterDataModel(base_data_model.BaseDataModel):
  """Class for the data for the formatter template."""

  def __init__(self,
               plugin_name: str,
               queries: [sql_query_model.SQLQueryModel]):
    """Initialises the formatter data model.

    Args:
      plugin_name (str): the name of the plugin
      queries (sql_query_model.SQLQueryModel): the queries
    """
    super().__init__(plugin_name)
    self.queries = queries
