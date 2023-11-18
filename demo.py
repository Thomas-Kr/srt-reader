from ReadSRT import SRTReader

# Create reader for SRT file
reader = SRTReader('example.srt')

# Get array of all text lines from SRT file
textLines = reader.getTextLines()
print(textLines, '\n')

# Get number of blocks in SRT file
blocksCount = reader.getBlocksCount()
print(blocksCount, '\n')

# Get duration of block (returns datetime.timedelta)
thirdBlockDuration = reader.getBlockDuration(3)
print(thirdBlockDuration, '\n')

# Get text lines (array of strings) by block index
secondTextLine = reader.getTextByIndex(2)
print(secondTextLine, '\n')

# Get text lines (array of strins) by timestamp
firstSecTextLine = reader.getTextByTime('00:00:03,500')
print(firstSecTextLine, '\n')

'''
srtBlocks = [block, block, block, ...]

block = {
    'index': int,
    'startTime': datetime,        
    'endTime': datetime,
    'textLine': []
}
'''