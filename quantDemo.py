#-*- coding:utf-8 -*-
import ConfigParser
import numpy as np
from quantsLib import *
import time
__author__ = 'Justin'

class strategyAnalysis():
 
    def spreadTrading(self,commodityCode,startDate,endDate,sigmaMultiplier):
        t0=time.time()
        data=dataOperation().spreadPrice(commodityCode,startDate,endDate)
        dataOperation().writeOutSpread(data,sigmaMultiplier)
        print 'SpreadTrading test for commodity finished and the total time assumed is %s' %(time.time()-t0)
    
    def volBacktest(self,commodityCode,startDate,endDate):
        t0=time.time()
        rawData=dataOperation().volPrice(commodityCode,startDate,endDate)
        strategy().writeoutVol(rawData,commodityCode)
        print 'volBacktest for commodity finished and the total time assumed is %s' %(time.time()-t0)    
    
if __name__=='__main__':
    config = ConfigParser.ConfigParser()
    config.readfp(open('data.ini'))        
    startDate=config.get("Date","startDate")
    endDate=config.get("Date","endDate") 
    commodityCode=config.get("Data","commodity").split(",")
    sigmaMultiplier=config.get("Assumption","sigmaMultiplier").split(",")
    
    strategyAnalysis().spreadTrading(commodityCode,startDate,endDate,sigmaMultiplier)
    #strategyAnalysis().volBacktest(commodityCode,startDate,endDate)
    
    
    
    
    