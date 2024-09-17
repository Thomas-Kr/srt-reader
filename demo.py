from ReadSRT import SRTReader

# Create reader for SRT file
reader = SRTReader('example.srt')

# Get array of all text lines from SRT file
text_lines = reader.get_text_lines()
print(text_lines, '\n')

# Get number of blocks in SRT file
blocks_count = reader.get_blocks_count()
print(blocks_count, '\n')

# Get duration of block (returns datetime.timedelta)
third_block_duration = reader.get_block_duration(3)
print(third_block_duration, '\n')

# Get text lines (array of strings) by block index
second_text_line = reader.get_text_by_index(2)
print(second_text_line, '\n')

# Get text lines (array of strings) by timestamp
first_sec_text_line = reader.get_text_by_time('00:00:03,500')
print(first_sec_text_line, '\n')

'''
srt_blocks = [block, block, block, ...]

block = {
    'index': int,
    'start_time': datetime,        
    'end_time': datetime,
    'text_line': []
}
'''
