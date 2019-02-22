import mmlibrary as mm
import sys
import pandas as pd
import pickle
import datetime
import json
import zipfile
from collections import OrderedDict

# mm.parseArguments(sys.argv) #point to address - remove this on mmlibrary/cloud
def predict(args):
    newdata_humidity = pd.DataFrame(mm.getArgument(args, "Humidity"))
    newdata_air_pressure = pd.DataFrame(mm.getArgument(args, "Air_Pressure"))

    lastdate_str = newdata_humidity.iloc[-1,0]
    lastdate_date = datetime.datetime.strptime(lastdate_str,"%Y-%m-%d %H:%M:%S")

    newdate = []

    for i in range(12):
        nextdate = lastdate_date + datetime.timedelta(minutes=5)
        newdate.append(nextdate)
        lastdate_date = nextdate

    # Separate the independent variables
    humidity = newdata_humidity[['Humidity']]
    air_pressure = newdata_air_pressure[['Air_Pressure']]

    # Load the models
    modelBinary = mm.getModel()
    # Extract and read the binaries files
    with zipfile.ZipFile(modelBinary) as zipper:
        with zipper.open('MM Model Binary Temperature.pckl', 'r') as LnRg_File:
            LnRg_Model = pickle.load(LnRg_File)
            LnRg_File.close()
        with zipper.open('MM Model Binary Humidity.pckl', 'r') as LnRg_File_Humidity:
            LnRg_Model_Humidity = pickle.load(LnRg_File_Humidity)
            LnRg_File_Humidity.close()
        with zipper.open('MM Model Binary Air Pressure.pckl', 'r') as LnRg_File_Air_Pressure:
            LnRg_Model_Air_Pressure = pickle.load(LnRg_File_Air_Pressure)
            LnRg_File_Air_Pressure.close()

    # Create the predicted values
    predicted_values_Humidity = LnRg_Model_Humidity.predict(humidity)
    prediction_series_Humidity = list(pd.Series(predicted_values_Humidity))

    predicted_values_Air_Pressure = LnRg_Model_Air_Pressure.predict(air_pressure)
    prediction_series_Air_Pressure = list(pd.Series(predicted_values_Air_Pressure))

    newpred = [('Date_Time', newdate), ('Humidity', prediction_series_Humidity), ('Air_Pressure', prediction_series_Air_Pressure)]
    newpred = pd.DataFrame.from_dict(OrderedDict(newpred))

    newpred_x = newpred[['Humidity','Air_Pressure']]

    predicted_values = LnRg_Model.predict(newpred_x)
    prediction_series = list(pd.Series(predicted_values))
    predictions = pd.DataFrame({'Date_Time': newdate, 'Predicted_Temperature': prediction_series})

    stingdate = predictions['Date_Time'].dt.strftime("%Y-%m-%d %H:%M:%S")
    predictions = pd.DataFrame({'Date_Time': stingdate, 'Predicted_Temperature': prediction_series})

    score = predictions.to_dict(orient='records')

    mm.returnScore(score)
