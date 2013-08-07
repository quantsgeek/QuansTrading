#-*- coding:utf-8 -*-
import pymongo
import datetime
import ConfigParser
import numpy as np
from quantsLib import *
import datetime
import time
__author__ = 'Justin'

def retrieveData():
	
    #insert into the database
    t0=time.time()
    connection=pymongo.Connection('localhost',27017)
    db=connection.lowFrequencyData
    res=db.Close.find({"name": "IF.CFE"}).sort("date",-1)
    print [x for x in res]
    print 'lowtime%s'%(time.time()-t0)

if __name__=='__main__':
	
    #configuring para
    config = ConfigParser.ConfigParser()
    config.readfp(open('data.ini'))        
    startDate=config.get("Date","startDate")
    endDate=config.get("Date","endDate") 
    commodityCode=config.get("Data","commodity").split(",")

    #retrieve the data
    #[Data,name,Date]=dataOperation().spreadPrice(commodityCode,startDate,endDate)
    
    #insert to database
    
    #dataOperation().lowFrequencyData(Data,name,Date)
    #dataOperation().highFrequencyData(Data,name,Date)
    #print 'finish'
    
    retrieveData()