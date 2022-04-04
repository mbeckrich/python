# squirrel fur color (Primary Fur Color) and count
# how many of each color
# create new dataframe, csv with this data
import pandas

squirrel_data = pandas.read_csv("./day-25/squirrel-census/Squirrel_Census.csv")
SQUIRREL_COLORS = squirrel_data["Primary Fur Color"]
SQUIRREL_COUNT = squirrel_data["Unique Squirrel ID"].count()

# Number of each color and total
squirrel_frame = pandas.DataFrame(SQUIRREL_COLORS.value_counts())
squirrel_frame.loc["Total"] = SQUIRREL_COUNT

squirrel_frame.to_csv("./day-25/squirrel-census/squirrel_colors.csv")
