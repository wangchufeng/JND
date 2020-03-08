import json

class DataConfig:
    m_mapUserIdReader = {}
    def loadData(self):
        with open('../pilot_study/data/new_bartestData.json') as json_file: 
            self.m_BarDataList = json.load(json_file)
        with open('../pilot_study/data/new_pietestData.json') as json_file: 
            self.m_PieDataList = json.load(json_file)
        with open('../pilot_study/data/new_bubbletestData.json') as json_file: 
            self.m_BubbleDataList = json.load(json_file)
            # print('newdata', self.m_DataList)
            # print('Data Length=', len(self.m_DataList))
            # for p in self.m_DataList:
            #     print(p)
            #     break
    def getTestData(self, userId, testChart):
        reader = 0
        userId = int(userId)
        print(self.m_mapUserIdReader)
        if(userId in self.m_mapUserIdReader):
            reader = self.m_mapUserIdReader[userId];
        print('userid', userId, 'reader', reader)

        if(testChart == 'bar'):
            self.m_DataList = self.m_BarDataList
        elif(testChart == 'pie'):
            self.m_DataList = self.m_PieDataList
        elif(testChart == 'bubble'):
            self.m_DataList = self.m_BubbleDataList

        if(reader >= len(self.m_DataList)):
            return {}, (str(reader)) + '/' + str(len(self.m_DataList))
        data = self.m_DataList[reader]
        reader += 1
        self.m_mapUserIdReader[int(userId)] = reader;
            # self.m_reader = 0
        return data, (str(reader)) + '/' + str(len(self.m_DataList))
