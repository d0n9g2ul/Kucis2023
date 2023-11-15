import re
import pandas as pd
import func.web as web
import func.file_stat as stat
import func.journal as journal
import func.last as last
import func.lastb as lastb
import func.nets as nets
import func.top as top


def read_csv(file):
    return pd.read_csv(file)


class Parser:
    def __init__(self, log_file, pattern=None):
        self.log_file = log_file
        self.log_data = []
        self.log_pattern = pattern
        self.df = None
        self.parse_logs()

    def __repr__(self):
        if self.df is not None:
            return repr(self.df)
        else:
            return "Dataframe does not exist. Call 'parse_logs' method first."

    def re_log(self):
        try:
            with open(self.log_file, "r") as file:
                log_lines = file.readlines()

        except FileNotFoundError:
            raise Exception(f"File not found: {self.log_file}")

        for line in log_lines:
            match = re.search(self.log_pattern, line)
            if match:
                self.log_data.append(match.groupdict())

        self.df = pd.DataFrame(self.log_data)


    def parse_logs(self):
        if self.log_pattern is None:
            print("No log pattern specified. Please provide a valid log pattern.")
            return

        elif self.log_pattern == "web":
            self.log_pattern = r'(?P<IP>[\d\.]+) - - \[(?P<DateTime>[^\]]+)\] "(?P<Request>[^"]+)" (?P<Status>\d+) (?P<Bytes>\d+) "(?P<Referrer>[^"]+)" "(?P<UserAgent>[^"]+)"'
            self.re_log()

        elif self.log_pattern == "stat":
            self.log_pattern =  r'(?P<Date>\d{4}-\d{2}-\d{2}) (?P<Time>\d{2}:\d{2}:\d{2}.\d+) [+-]\d{4} (?P<FilePath>.+)'
            self.re_log()
        
        elif self.log_pattern == "journal":
            self.log_pattern = r'(?P<Date>\w{3} \d{2}) (?P<Time>\d{2}:\d{2}:\d{2}) (?P<User>\w+) (?P<Process>\w+\[\d+\]): (?P<Message>.+)$'
            self.re_log()

        elif self.log_pattern == "last":
            self.log_pattern = r'(?P<User>\S+)\s+(?P<Terminal>\S+)\s+(?P<OS>\S+)\s+(?P<DateTime>\w{3} \w{3} \d{1,2} \d{2}:\d{2})\s+(?P<Status>.+)'
            self.re_log()

        elif self.log_pattern == "lastb":
            self.log_pattern = r'(?P<User>\S+)\s+(?P<Terminal>\S+)\s+(?P<Session>\S+)\s+(?P<DateTime>.+?\d{2}:\d{2}) - (?P<End>\d{2}:\d{2})\s+\((?P<Duration>.+)\)'
            self.re_log()

        elif self.log_pattern == "netstat":
            self.log_pattern = r'(?P<Proto>\S+)\s+(?P<RecvQ>\d+)\s+(?P<SendQ>\d+)\s+(?P<LocalAddress>[\S+]+)\s+(?P<ForeignAddress>[\S+]+)\s+(?P<State>\S+)\s+(?P<PIDProgramName>.+)'
            self.re_log()

        elif self.log_pattern == "top":
            with open(self.log_file, "r") as infile:
                with open(self.log_file+'_replace.txt', "w") as outfile:
                    header_written = False
                    for line in infile:
                        # 공백을 제거하고 ,로 대체
                        line = line.strip().replace(" ", ",")
                        
                        # 중복된 쉼표를 하나로 줄이기
                        line = re.sub(r',+', ',', line)
                        
                        if not header_written:
                            # 첫 번째 행은 컬럼 이름으로 처리하지 않음
                            header_written = True
                        else:
                            outfile.write(line + "\n")

            self.log_file = self.log_file+'_replace.txt'
            self.df = pd.read_csv(self.log_file, skiprows=6, delimiter=',', names=["PID", "USER", "PR", "NI", "VIRT", "RES", "SHR", "S", "%CPU", "%MEM", "TIME+", "COMMAND"])
    

    def head(self, n=None):
        df = pd.DataFrame(self.df)
        if n == None:
            n = 5
        return df.head(n)
    

    def tail(self, n=None):
        df = pd.DataFrame(self.df)
        if n == None:
            n = 5
        return df.tail(n)


    def to_csv(self, output_file_name):
        if self.df is not None:
            self.df.to_csv(output_file_name, index=False)
        else:
            print("Dataframe does not exist. Call 'parse_logs' method first.")


class WebParser(Parser):
    def __init__(self, log_file=None, pattern="web", dataframe=None):
        if dataframe is not None:
            self.df = dataframe
        else:
            super().__init__(log_file, pattern=pattern)


    def total_ip_count(self):
        return web.total_ip_count(self.df)


    def ip_count(self):
        return web.ip_count(self.df)


    def status_count(self, code=None):
        return web.status_count(self.df, code)
    

    def filter_by_status(self, status_code):
        return WebParser(log_file=None, pattern="web", dataframe=web.filter_by_status(self.df, status_code))


class StatParser(Parser):
    def __init__(self, log_file=None, pattern="stat", dataframe=None):
        if dataframe is not None:
            self.df = dataframe
        else:
            super().__init__(log_file, pattern=pattern)


    def min_max_time(self):
        return stat.min_max_time(self.df)


    def file_count(self):
        return stat.file_count(self.df)


    def filter_by_date(self, date=None):
        return stat.filter_by_date(self.df, date)
    

class JournalParser(Parser):
    def __init__(self, log_file=None, pattern="journal", dataframe=None):
        if dataframe is not None:
            self.df = dataframe
        else:
            super().__init__(log_file, pattern=pattern)


    def by_date(self, start_date, end_date=None):
        return JournalParser(dataframe=journal.by_date(self.df, start_date, end_date))
    

    def by_time(self, start_time, end_time=None):
        return JournalParser(dataframe=journal.by_time(self.df, start_time, end_time))
    

    def by_message(self, keyword):
        return JournalParser(dataframe=journal.by_message(self.df, keyword))
    

    def by_process(self, keyword):
        return JournalParser(dataframe=journal.by_process(self.df, keyword))


class LastParser(Parser):
    def __init__(self, log_file=None, pattern="last", dataframe=None):
        if dataframe is not None:
            self.df = dataframe
        else:
            super().__init__(log_file, pattern=pattern)


    def connect_user(self):
        return last.connect_user(self.df)


    def connect_time(self):
        return last.connect_time(self.df)
    

class LastbParser(Parser):
    def __init__(self, log_file=None, pattern="lastb", dataframe=None):
        if dataframe is not None:
            self.df = dataframe
        else:
            super().__init__(log_file, pattern=pattern)


    def failed_attp(self):
        return lastb.failed_attp(self.df)


    def all_ips(self):
        return lastb.all_ips(self.df)


    def attempt_date(self, date=None):
        return lastb.attempt_date(self.df, date)


class NetsParser(Parser):
    def __init__(self, log_file=None, pattern="netstat", dataframe=None):
        if dataframe is not None:
            self.df = dataframe
        else:
            super().__init__(log_file, pattern=pattern)


    def all_PID(self, date=None):
        return nets.all_PID(self.df)


    def local_ips(self, date=None):
        return nets.local_ips(self.df)


    def foreign_ips(self, date=None):
        return nets.foreign_ips(self.df)


    def state_count(self):
        return nets.state_count(self.df)


    def established_ports(self):
        return nets.established_ports(self.df)


    def established_PID(self, date=None):
        return nets.established_PID(self.df)


class TopParser(Parser):
    def __init__(self, log_file=None, pattern="top", dataframe=None):
        if dataframe is not None:
            self.df = dataframe
        else:
            super().__init__(log_file, pattern=pattern)
        

    def cpu_usage(self, threshold):
        return TopParser(dataframe=top.cpu_usage(self.df, threshold))


    def mem_usage(self, threshold=None):
        return TopParser(dataframe=top.mem_usage(self.df, threshold))


    def high_memory(self, n):
        return TopParser(dataframe=top.high_memory(self.df, n))


    def is_running(self):
        return TopParser(dataframe=top.is_running(self.df))


    def pie_chart(self, resource_col=None, command_col="COMMAND", title=None):
        top.pie_chart(self.df, resource_col, command_col, title)


    def bar_chart(self, resource_col=None, command_col='COMMAND', title=None):
        top.bar_chart(self.df, resource_col, command_col, title=None)