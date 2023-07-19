from constants import list_his, list_irm, list_name
from functions import create_table, plot

table_day_plot = create_table(list_his, list_irm, list_name)
plot(table_day_plot)
