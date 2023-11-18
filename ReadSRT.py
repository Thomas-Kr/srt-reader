from datetime import datetime

class SRTReader:
    def __init__(self, srtFile: str) -> None:
        try:
            file = open(srtFile, 'r')
            srtText: str = file.read()
        except Exception as error:
            return f'Error occured while opening the file: {error}'
        
        srtLines: [str] = srtText.split('\n')
        self.srtBlocks = []
        
        i = 0
        
        while i < len(srtLines) - 1:
            block = {
                'index': int,
                'startTime': datetime,
                'endTime': datetime,
                'textLine': []
            }
            
            block['index'] = int(srtLines[i])
            
            timeStamps = srtLines[i+1].split(' ')
            block['startTime'] = datetime.strptime(timeStamps[0], '%H:%M:%S,%f').time()
            block['endTime'] = datetime.strptime(timeStamps[2], '%H:%M:%S,%f').time()
            
            i += 2
            
            while i < len(srtLines) - 1:
                if srtLines[i] == '':
                    break
                block['textLine'].append(srtLines[i])
                i += 1
                
            self.srtBlocks.append(block)
                
            i += 1
                
    
    def getTextLines(self) -> [str]:
        textLines: [str] = []
        
        for block in self.srtBlocks:
            textLines.append(block['textLine'])
            
        return textLines
    
    def getBlocksCount(self) -> int:
        return len(self.srtBlocks)
    
    def getBlockDuration(self, index: int) -> datetime:     
        startTime = self.srtBlocks[index]['startTime']
        endTime = self.srtBlocks[index]['endTime']
        
        difference = datetime.combine(datetime.today(), endTime) - datetime.combine(datetime.today(), startTime)
        return difference
            
    def getTextByIndex(self, index: int) -> str:
        return self.srtBlocks[index]['textLine']
    
    def getTextByTime(self, timestamp: str) -> str:
        timestamp = datetime.strptime(timestamp, '%H:%M:%S,%f').time()
        
        for block in self.srtBlocks:
            if timestamp >= block['startTime'] and timestamp <= block['endTime']:
                return block['textLine']
            
        return 'The timestamp does not exists.'
    
reader = SRTReader('example.srt')

print(reader.getTextLines())