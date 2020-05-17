import pandas as pd

import sqlalchemy

from sqlalchemy import create_engine, func

from sqlalchemy.orm import Session

from flask import Flask, jsonify

# set up connection

engine = create_engine("sqlite:///Resources/hawaii.sqlite",connect_args={"check_same_thread": False})

session = Session(engine)

conn = engine.connect()

# Create data frames

Measure_df = pd.read_sql("select * from measurement", conn)


Station_df = pd.read_sql("select * from station", conn)

#conn.close()

Combine_df = pd.merge(Measure_df, Station_df, how = 'left', on = 'station')

# Convert to list of dictionaries

prcp_df = Measure_df[['date','prcp']]

stat_df = Station_df[['station']]

Active_df = Measure_df.loc[(Measure_df['station'] == 'USC00519281') & (Measure_df['date']  <= '2017-08-23') & (Measure_df['date']  >= '2016-08-23')]

Active_df = Active_df[['date','tobs']]

P = list(prcp_df.T.to_dict().values())

S = stat_df.values.tolist()

A = list(Active_df.T.to_dict().values())


app = Flask(__name__)

@app.route("/")

def welcome():
    
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precpitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

@app.route("/api/v1.0/precpitation")

def precp():

    return jsonify(P)


@app.route("/api/v1.0/stations")

def station():

    return jsonify(S)

@app.route("/api/v1.0/tobs")

def temp():

    return jsonify(A)

@app.route("/api/v1.0/<start>")

def cal_temp(start):

    q = "select min(tobs) as Tmin, avg(tobs) as Tavg, max(tobs) as Tmax from measurement where date = :start"

    df = pd.read_sql_query(q, conn, params = {"start":start})

    return jsonify(list(df.T.to_dict().values()))



@app.route("/api/v1.0/<start>/<end>")

def cal_temp2(start,end):
    
    q = "select min(tobs) as Tmin, avg(tobs) as Tavg, max(tobs) as Tmax from measurement where date >= :start and date <= :end"

    df = pd.read_sql_query(q, conn, params = {"start":start, "end":end})
    
    return jsonify(list(df.T.to_dict().values()))

    
    
if __name__ == "__main__":
    
    app.run(debug=True)



