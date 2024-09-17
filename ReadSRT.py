from datetime import datetime

class SRTReader:
    def __init__(self, srt_file: str) -> None:
        try:
            with open(srt_file, 'r') as file:
                srt_text: str = file.read()
        except Exception as error:
            print(f'Error occurred while opening the file: {error}')
            return

        srt_lines: list[str] = srt_text.split('\n')
        self.srt_blocks = []

        i = 0
        while i < len(srt_lines) - 1:
            block = {
                'index': int,
                'start_time': datetime,
                'end_time': datetime,
                'text_line': []
            }

            block['index'] = int(srt_lines[i])

            time_stamps = srt_lines[i + 1].split(' ')
            block['start_time'] = datetime.strptime(time_stamps[0], '%H:%M:%S,%f').time()
            block['end_time'] = datetime.strptime(time_stamps[2], '%H:%M:%S,%f').time()

            i += 2

            while i < len(srt_lines) - 1:
                if srt_lines[i] == '':
                    break
                block['text_line'].append(srt_lines[i])
                i += 1

            self.srt_blocks.append(block)
            i += 1

    def get_text_lines(self) -> list[str]:
        text_lines: list[str] = []

        for block in self.srt_blocks:
            text_lines.append(block['text_line'])

        return text_lines

    def get_blocks_count(self) -> int:
        return len(self.srt_blocks)

    def get_block_duration(self, index: int) -> datetime:
        start_time = self.srt_blocks[index - 1]['start_time']
        end_time = self.srt_blocks[index - 1]['end_time']

        difference = datetime.combine(datetime.today(), end_time) - datetime.combine(datetime.today(), start_time)
        return difference

    def get_text_by_index(self, index: int) -> str:
        return self.srt_blocks[index - 1]['text_line']

    def get_text_by_time(self, timestamp: str) -> str:
        timestamp = datetime.strptime(timestamp, '%H:%M:%S,%f').time()

        for block in self.srt_blocks:
            if block['start_time'] <= timestamp <= block['end_time']:
                return block['text_line']

        return 'The timestamp does not exist.'
